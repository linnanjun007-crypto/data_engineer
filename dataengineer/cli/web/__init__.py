# Copyright 2025-present DatusAI, Inc.
# Licensed under the Apache License, Version 2.0.
# See http://www.apache.org/licenses/LICENSE-2.0 for details.

"""
Web interface for DataEngineer Agent.

Serves a React-based chatbot frontend backed by FastAPI.
"""

from dataengineer.cli.web.chatbot import create_web_app, run_web_interface

__all__ = [
    "create_web_app",
    "run_web_interface",
]
