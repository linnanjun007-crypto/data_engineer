# Copyright 2025-present DatusAI, Inc.
# Licensed under the Apache License, Version 2.0.

"""Unit tests for dataengineer/tools/func_tool/fs_path_policy.py"""

from pathlib import Path

import pytest

from dataengineer.tools.func_tool.fs_path_policy import (
    PathZone,
    build_walk_patterns,
    classify_path,
    whitelist_anchors,
)


@pytest.fixture
def project(tmp_path):
    root = tmp_path / "project"
    root.mkdir()
    return root


@pytest.fixture
def fake_home(tmp_path):
    home = tmp_path / "fake_home" / ".dataengineer"
    (home / "skills").mkdir(parents=True)
    return home


class TestClassifyInternal:
    def test_relative_inside_root(self, project):
        r = classify_path("src/main.py", root_path=project, current_node="chat")
        assert r.zone == PathZone.INTERNAL
        assert r.display == "src/main.py"

    def test_dot_maps_to_root(self, project):
        r = classify_path(".", root_path=project, current_node="chat")
        assert r.zone == PathZone.INTERNAL
        assert r.display == "."

    def test_absolute_inside_root_is_internal(self, project):
        r = classify_path(str(project / "a.md"), root_path=project, current_node="chat")
        assert r.zone == PathZone.INTERNAL


class TestClassifyHidden:
    def test_dataengineer_subdir_is_hidden(self, project):
        r = classify_path(".dataengineer/sessions/foo.db", root_path=project, current_node="chat")
        assert r.zone == PathZone.HIDDEN

    def test_dataengineer_root_itself_is_hidden(self, project):
        r = classify_path(".dataengineer", root_path=project, current_node="chat")
        assert r.zone == PathZone.HIDDEN


class TestClassifyWhitelist:
    def test_project_skills_whitelisted(self, project):
        r = classify_path(".dataengineer/skills/foo/SKILL.md", root_path=project, current_node="chat")
        assert r.zone == PathZone.WHITELIST
        assert r.display.startswith(".dataengineer/skills/")

    def test_own_memory_dir_is_whitelist(self, project):
        r = classify_path(".dataengineer/memory/gen_sql/MEMORY.md", root_path=project, current_node="gen_sql")
        assert r.zone == PathZone.WHITELIST

    def test_other_node_memory_is_hidden(self, project):
        r = classify_path(".dataengineer/memory/chat/MEMORY.md", root_path=project, current_node="gen_sql")
        assert r.zone == PathZone.HIDDEN

    def test_none_node_disables_memory_whitelist(self, project):
        r = classify_path(".dataengineer/memory/any/MEMORY.md", root_path=project, current_node=None)
        assert r.zone == PathZone.HIDDEN

    def test_home_skills_whitelist(self, project, fake_home):
        r = classify_path(
            str(fake_home / "skills" / "global" / "SKILL.md"),
            root_path=project,
            current_node="chat",
            datus_home=fake_home,
        )
        assert r.zone == PathZone.WHITELIST
        assert r.display.startswith("~/.dataengineer/skills/")


class TestClassifyExternal:
    def test_relative_escape_goes_external(self, project):
        r = classify_path("../other/secret.txt", root_path=project, current_node="chat")
        assert r.zone == PathZone.EXTERNAL
        assert Path(r.display).is_absolute()

    def test_absolute_outside_root_is_external(self, project, tmp_path):
        elsewhere = tmp_path / "other"
        elsewhere.mkdir()
        target = elsewhere / "x.md"
        r = classify_path(str(target), root_path=project, current_node="chat")
        assert r.zone == PathZone.EXTERNAL


class TestRootUnderHome:
    """If the project happens to live under ``~/.dataengineer`` — e.g. someone runs
    ``datus`` inside ``~/.dataengineer/workspace/demo`` — project anchors must still
    beat the global ``~/.dataengineer/skills`` anchor so file visibility matches the
    user's intent ("writing to my project's skills dir, not the global one").
    """

    def test_project_skills_wins_over_global(self, tmp_path):
        home = tmp_path / ".dataengineer"
        home.mkdir()
        (home / "skills").mkdir()
        project = home / "workspace" / "demo"
        project.mkdir(parents=True)
        r = classify_path(
            ".dataengineer/skills/foo/SKILL.md",
            root_path=project,
            current_node="chat",
            datus_home=home,
        )
        assert r.zone == PathZone.WHITELIST
        assert r.display.startswith(".dataengineer/skills/")


class TestWhitelistAnchors:
    def test_anchor_list_contains_project_and_home(self, project, fake_home):
        anchors = whitelist_anchors(root_path=project, current_node="chat", datus_home=fake_home)
        # project_skills, home_skills (no memory since current_node without memory dir) — but current_node="chat" still adds memory anchor.
        assert (project / ".dataengineer" / "skills").resolve(strict=False) in anchors
        assert (project / ".dataengineer" / "memory" / "chat").resolve(strict=False) in anchors
        assert (fake_home / "skills").resolve(strict=False) in anchors

    def test_anchors_skip_memory_when_node_none(self, project, fake_home):
        anchors = whitelist_anchors(root_path=project, current_node=None, datus_home=fake_home)
        # Expect exactly two anchors: project .dataengineer/skills and home .dataengineer/skills.
        # No per-node memory anchor because current_node is None.
        assert len(anchors) == 2
        expected_suffixes = {(".dataengineer", "skills")}
        seen = {(a.parent.name, a.name) for a in anchors}
        assert seen == expected_suffixes


class TestBuildWalkPatterns:
    """The walker relies on these patterns to prune ``HIDDEN`` subtrees cheaply
    — ``wcmatch`` is fed ``excludes`` first and then applies ``re_includes`` so
    the two allowed subtrees under ``.dataengineer/`` (skills + per-node memory) stay
    visible. The glob strings below are the contract that the filesystem tool
    expects, so they are pinned here.
    """

    def test_excludes_prune_entire_dot_dataengineer(self, project):
        excludes, _ = build_walk_patterns(root_path=project, current_node="chat")
        # Both the directory itself and its contents must be excluded,
        # otherwise ``.dataengineer`` survives the first-level match.
        assert excludes == [".dataengineer", ".dataengineer/**"]

    def test_re_includes_default_to_skills_only(self, project):
        _, re_includes = build_walk_patterns(root_path=project, current_node=None)
        # Without a current_node we cannot scope a memory subtree — only the
        # project-local skills directory gets re-included.
        assert re_includes == [".dataengineer/skills/**"]

    def test_re_includes_add_node_memory(self, project):
        _, re_includes = build_walk_patterns(root_path=project, current_node="gen_sql")
        # Skills stays first (longest-prefix-wins isn't used here, but the
        # downstream walker iterates in list order for determinism).
        assert re_includes == [".dataengineer/skills/**", ".dataengineer/memory/gen_sql/**"]

    def test_patterns_are_posix_for_wcmatch(self, project):
        """All generated patterns are POSIX slashes; wcmatch does not normalize
        separators, so a Windows-style backslash would break globmatch."""
        excludes, re_includes = build_walk_patterns(root_path=project, current_node="chat")
        for pattern in excludes + re_includes:
            assert "\\" not in pattern
