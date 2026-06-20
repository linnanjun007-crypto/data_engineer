#!/bin/sh
# install-dev.sh - dev/source installer for DataEngineer-Agent on Linux and macOS.
# Installs directly from GitHub (git+https), so you can pick up unreleased
# changes on main or any branch/tag/commit.
#
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/datus-ai/datus-agent/main/install-dev.sh | sh
#
# For a stable PyPI install, use install.sh instead.
#
# Optional environment variables (set on the receiving shell, e.g.
#   curl -fsSL ... | DATAENGINEER_REF=feature/foo sh
# ):
#   DATAENGINEER_REF              Git ref to install: branch, tag, or commit SHA. Default: main.
#   DATAENGINEER_HOME             Base dir for the venv. Default: $HOME/.dataengineer.
#   DATAENGINEER_BIN_DIR          Where shims are written. Default: $HOME/.local/bin.
#   DATAENGINEER_FORCE=1          Delete and recreate $DATAENGINEER_HOME/venv if it already exists.
#   DATAENGINEER_NO_MODIFY_PATH=1 Skip appending PATH export to shell rc files.

set -eu

GIT_REPO="https://github.com/datus-ai/datus-agent.git"
# Console scripts declared in pyproject.toml [project.scripts].
CONSOLE_SCRIPTS="dataengineer dataengineer-agent dataengineer-cli dataengineer-api dataengineer-mcp dataengineer-gateway"

DATAENGINEER_HOME="${DATAENGINEER_HOME:-$HOME/.dataengineer}"
DATAENGINEER_BIN_DIR="${DATAENGINEER_BIN_DIR:-$HOME/.local/bin}"
DATAENGINEER_REF="${DATAENGINEER_REF:-main}"
DATAENGINEER_FORCE="${DATAENGINEER_FORCE:-}"
DATAENGINEER_NO_MODIFY_PATH="${DATAENGINEER_NO_MODIFY_PATH:-}"

VENV_DIR="$DATAENGINEER_HOME/venv"

# Snapshot the user's PATH before we mutate it for uv lookup, so later
# "is bin dir already on PATH" checks reflect the user's real environment.
ORIGINAL_PATH="${PATH:-}"

MARKER_BEGIN="# >>> dataengineer-agent installer >>>"
MARKER_END="# <<< dataengineer-agent installer <<<"

_color_init() {
    if [ -t 1 ] && command -v tput >/dev/null 2>&1 && [ "$(tput colors 2>/dev/null || echo 0)" -ge 8 ]; then
        BOLD=$(tput bold)
        RED=$(tput setaf 1)
        GREEN=$(tput setaf 2)
        YELLOW=$(tput setaf 3)
        BLUE=$(tput setaf 4)
        RESET=$(tput sgr0)
    else
        BOLD=""; RED=""; GREEN=""; YELLOW=""; BLUE=""; RESET=""
    fi
}

info()  { printf '%s==>%s %s\n' "$BLUE" "$RESET" "$1"; }
warn()  { printf '%swarn:%s %s\n' "$YELLOW" "$RESET" "$1" >&2; }
error() { printf '%serror:%s %s\n' "$RED" "$RESET" "$1" >&2; }
die()   { error "$1"; exit 1; }

need_cmd() {
    command -v "$1" >/dev/null 2>&1 || die "required command not found: $1"
}

check_os() {
    uname_s=$(uname -s 2>/dev/null || echo unknown)
    case "$uname_s" in
        Linux|Darwin) ;;
        *)
            error "unsupported OS: $uname_s"
            error "Linux and macOS are supported. On Windows, please install manually:"
            error "    pip install git+${GIT_REPO}@${DATAENGINEER_REF}"
            exit 1
            ;;
    esac
}

validate_env() {
    if [ -z "${HOME:-}" ] || [ ! -d "$HOME" ]; then
        die "\$HOME is not set or not a directory"
    fi
}

_extend_path_for_uv() {
    for candidate in "$HOME/.local/bin" "$HOME/.cargo/bin"; do
        case ":$PATH:" in
            *":$candidate:"*) ;;
            *) PATH="$candidate:$PATH"; export PATH ;;
        esac
    done
}

ensure_uv() {
    _extend_path_for_uv
    if command -v uv >/dev/null 2>&1; then
        info "uv already available: $(command -v uv)"
        return 0
    fi
    info "installing uv (astral.sh/uv)..."
    need_cmd curl
    curl -LsSf https://astral.sh/uv/install.sh | sh
    _extend_path_for_uv
    command -v uv >/dev/null 2>&1 || die "uv installation failed; install manually from https://astral.sh/uv"
    info "uv installed: $(command -v uv)"
}

create_venv() {
    mkdir -p "$DATAENGINEER_HOME"
    if [ -d "$VENV_DIR" ]; then
        if [ -n "$DATAENGINEER_FORCE" ]; then
            info "DATAENGINEER_FORCE=1: removing existing venv at $VENV_DIR"
            rm -rf "$VENV_DIR"
        elif [ -x "$VENV_DIR/bin/python" ] && \
             "$VENV_DIR/bin/python" -c 'import sys; sys.exit(0 if sys.version_info[:2]==(3,12) else 1)' >/dev/null 2>&1; then
            info "reusing existing Python 3.12 venv at $VENV_DIR (set DATAENGINEER_FORCE=1 to recreate)"
        else
            warn "existing venv at $VENV_DIR is not Python 3.12; recreating"
            rm -rf "$VENV_DIR"
        fi
    fi
    if [ ! -d "$VENV_DIR" ]; then
        info "creating venv at $VENV_DIR (Python 3.12)"
        # --seed installs pip/setuptools/wheel into the venv so the dataengineer-pip
        # shim and any tool that shells out to `pip` keep working.
        uv venv --python 3.12 --seed "$VENV_DIR"
    fi
    VENV_PY="$VENV_DIR/bin/python"
    [ -x "$VENV_PY" ] || die "venv python not found at $VENV_PY"
}

install_package() {
    need_cmd git
    # Full clone (not --filter=blob:none): partial clones can fail to check
    # out arbitrary commit SHAs not reachable from fetched refs, because
    # on-demand fetch via `git fetch origin <sha>` is rejected by servers
    # for non-ref OIDs. A full clone is more bytes but makes DATAENGINEER_REF
    # work reliably for any branch/tag/commit SHA.
    #
    # No submodules: benchmark/* is excluded from the wheel build (see
    # pyproject.toml), and upstream submodule chains (e.g. Spider2) may
    # fail `git submodule update --recursive` for reasons unrelated to
    # this install.
    src_dir=$(mktemp -d -t dataengineer-src-XXXXXX)
    # shellcheck disable=SC2064
    trap "rm -rf \"$src_dir\"" EXIT
    info "cloning ${GIT_REPO} @ ${DATAENGINEER_REF} -> $src_dir (no submodules)"
    git clone --quiet "$GIT_REPO" "$src_dir"
    git -C "$src_dir" -c advice.detachedHead=false checkout --quiet "$DATAENGINEER_REF"
    info "building and installing dataengineer-agent from local source"
    uv pip install --python "$VENV_PY" --upgrade "$src_dir"
}

write_shims() {
    mkdir -p "$DATAENGINEER_BIN_DIR"
    # dataengineer-pip is an extra shim so users can add packages into the global venv
    # without activating it: `dataengineer-pip install <pkg>`.
    for name in $CONSOLE_SCRIPTS dataengineer-pip; do
        target="$DATAENGINEER_BIN_DIR/$name"
        case "$name" in
            dataengineer-pip) venv_target="$VENV_DIR/bin/pip" ;;
            *)         venv_target="$VENV_DIR/bin/$name" ;;
        esac
        cat >"$target" <<EOF
#!/bin/sh
# generated by dataengineer-agent install-dev.sh; regenerated on each install
exec "$venv_target" "\$@"
EOF
        chmod +x "$target"
    done
    info "wrote shims to $DATAENGINEER_BIN_DIR: $CONSOLE_SCRIPTS dataengineer-pip"
}

path_contains_bin_dir() {
    case ":$ORIGINAL_PATH:" in
        *":$DATAENGINEER_BIN_DIR:"*) return 0 ;;
        *) return 1 ;;
    esac
}

rc_has_marker() {
    [ -f "$1" ] && grep -qF "$MARKER_BEGIN" "$1"
}

append_path_block() {
    rc="$1"
    {
        printf '\n%s\n' "$MARKER_BEGIN"
        printf 'export PATH="%s:$PATH"\n' "$DATAENGINEER_BIN_DIR"
        printf '%s\n' "$MARKER_END"
    } >>"$rc"
    info "added $DATAENGINEER_BIN_DIR to PATH in $rc"
}

maybe_update_path() {
    if path_contains_bin_dir; then
        info "$DATAENGINEER_BIN_DIR already on PATH"
        return 0
    fi
    if [ -n "$DATAENGINEER_NO_MODIFY_PATH" ]; then
        warn "DATAENGINEER_NO_MODIFY_PATH=1: not editing shell rc files"
        warn "add this line to your shell rc manually:"
        warn "    export PATH=\"$DATAENGINEER_BIN_DIR:\$PATH\""
        return 0
    fi

    updated=0
    for rc in "$HOME/.zshrc" "$HOME/.bashrc" "$HOME/.bash_profile" "$HOME/.profile"; do
        if [ -f "$rc" ]; then
            if rc_has_marker "$rc"; then
                info "$rc already contains dataengineer-agent PATH block, skipping"
            else
                append_path_block "$rc"
            fi
            updated=1
        fi
    done
    if [ "$updated" -eq 0 ]; then
        append_path_block "$HOME/.profile"
    fi
}

verify_install() {
    info "verifying installation..."
    if ! "$VENV_DIR/bin/dataengineer" --help >/dev/null 2>&1; then
        die "installed dataengineer entry is not callable: $VENV_DIR/bin/dataengineer"
    fi
    if ! "$DATAENGINEER_BIN_DIR/dataengineer" --help >/dev/null 2>&1; then
        die "shim not callable: $DATAENGINEER_BIN_DIR/dataengineer"
    fi
    info "verified."
}

print_summary() {
    cat <<EOF

${GREEN}${BOLD}DataEngineer-Agent (dev) installed from ${DATAENGINEER_REF}.${RESET}

  venv:   $VENV_DIR
  shims:  $DATAENGINEER_BIN_DIR
  entry:  $DATAENGINEER_BIN_DIR/datus
  source: ${GIT_REPO}@${DATAENGINEER_REF}

Next steps:
  1. Open a new shell, or run ${BOLD}source ~/.zshrc${RESET} (or your rc file) to pick up PATH.
  2. Run ${BOLD}dataengineer-agent init${RESET} to configure your LLM provider and database.

To install additional Python packages into the global venv:
  ${BOLD}dataengineer-pip install <package>${RESET}
  (equivalent to ${VENV_DIR}/bin/pip install <package>)

Reinstall from a different ref:
  curl -fsSL https://raw.githubusercontent.com/datus-ai/datus-agent/main/install-dev.sh | DATAENGINEER_REF=<branch-or-tag> sh

EOF
}

_color_init
check_os
validate_env
ensure_uv
create_venv
install_package
write_shims
maybe_update_path
verify_install
print_summary
