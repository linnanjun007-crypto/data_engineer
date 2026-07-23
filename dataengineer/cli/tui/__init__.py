# Copyright 2025-present DatusAI, Inc.
# Licensed under the Apache License, Version 2.0.
# See http://www.apache.org/licenses/LICENSE-2.0 for details.

"""Persistent prompt_toolkit TUI shell for the DataEngineer REPL.

The TUI keeps the status bar and input TextArea pinned to the bottom of the
terminal across the entire REPL lifetime, including while agent loops run in
a worker thread. This module is only loaded when ``sys.stdin``/``sys.stdout``
are TTYs and ``DATAENGINEER_TUI`` is not explicitly disabled; non-TTY paths (CI,
pipes, ``--print`` mode) continue to use the classic ``PromptSession``.
"""

from dataengineer.cli.tui.app import DataEngineerApp, tui_enabled

__all__ = ["DataEngineerApp", "tui_enabled"]
