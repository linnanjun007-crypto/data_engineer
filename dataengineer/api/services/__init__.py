"""API Services module.

Consolidated service layer for DataEngineer Agent API.
"""

# Core services
from dataengineer.api.services.dataengineer_service_cache import DataEngineerServiceCache

# Lazy imports - services are imported only when needed by routes
# This avoids circular dependencies and import errors

__all__ = [
    "DataEngineerServiceCache",
]


def __getattr__(name):
    """Lazy import of services on demand."""
    if name == "DataEngineerService":
        from dataengineer.api.services.dataengineer_service import DataEngineerService

        return DataEngineerService
    elif name == "ChatService":
        from dataengineer.api.services.chat_service import ChatService

        return ChatService
    elif name == "ChatTaskManager":
        from dataengineer.api.services.chat_task_manager import ChatTaskManager

        return ChatTaskManager
    elif name == "ChatTask":
        from dataengineer.api.services.chat_task_manager import ChatTask

        return ChatTask
    elif name == "CLIService":
        from dataengineer.api.services.cli_service import CLIService

        return CLIService
    elif name == "DatasourceService":
        from dataengineer.api.services.database_service import DatasourceService

        return DatasourceService
    elif name == "ExplorerService":
        from dataengineer.api.services.explorer_service import ExplorerService

        return ExplorerService
    elif name == "MCPService":
        from dataengineer.api.services.mcp_service import MCPService

        return MCPService
    elif name == "KbService":
        from dataengineer.api.services.kb_service import KbService

        return KbService
    elif name == "action_to_sse_event":
        from dataengineer.api.services.action_sse_converter import action_to_sse_event

        return action_to_sse_event
    elif name == "AgentService":
        from dataengineer.api.services.agent_service import AgentService

        return AgentService
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
