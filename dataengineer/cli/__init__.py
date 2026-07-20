# Copyright 2025-present DatusAI, Inc.
# Licensed under the Apache License, Version 2.0.
# See http://www.apache.org/licenses/LICENSE-2.0 for details.

"""
Datus-CLI package initialization.
"""

from .autocomplete import SQLCompleter

__all__ = ["DataEngineerCLI", "SQLCompleter"]


def __getattr__(name: str):
    """Lazy import to avoid circular dependency with agent modules."""
    if name == "DataEngineerCLI":
        from .repl import DataEngineerCLI

        return DataEngineerCLI
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
