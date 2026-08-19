"""Tests for datus.api.services.__init__ — lazy import mechanism."""

import pytest

from dataengineer.api import services


class TestLazyImports:
    """Tests for __getattr__-based lazy imports."""

    def test_dataengineer_service_cache_is_direct_import(self):
        """DataEngineerServiceCache is directly imported, not lazy."""
        from dataengineer.api.services.dataengineer_service_cache import DataEngineerServiceCache

        assert services.DataEngineerServiceCache is DataEngineerServiceCache

    def test_lazy_import_dataengineer_service(self):
        """DataEngineerService is lazy-imported on first access."""
        from dataengineer.api.services.dataengineer_service import DataEngineerService

        assert services.DataEngineerService is DataEngineerService

    def test_lazy_import_chat_service(self):
        """ChatService is lazy-imported on first access."""
        from dataengineer.api.services.chat_service import ChatService

        assert services.ChatService is ChatService

    def test_lazy_import_chat_task_manager(self):
        """ChatTaskManager is lazy-imported on first access."""
        from dataengineer.api.services.chat_task_manager import ChatTaskManager

        assert services.ChatTaskManager is ChatTaskManager

    def test_lazy_import_chat_task(self):
        """ChatTask is lazy-imported on first access."""
        from dataengineer.api.services.chat_task_manager import ChatTask

        assert services.ChatTask is ChatTask

    def test_lazy_import_cli_service(self):
        """CLIService is lazy-imported on first access."""
        from dataengineer.api.services.cli_service import CLIService

        assert services.CLIService is CLIService

    def test_lazy_import_datasource_service(self):
        """DatasourceService is lazy-imported on first access."""
        from dataengineer.api.services.database_service import DatasourceService

        assert services.DatasourceService is DatasourceService

    def test_lazy_import_explorer_service(self):
        """ExplorerService is lazy-imported on first access."""
        from dataengineer.api.services.explorer_service import ExplorerService

        assert services.ExplorerService is ExplorerService

    def test_lazy_import_mcp_service(self):
        """MCPService is lazy-imported on first access."""
        from dataengineer.api.services.mcp_service import MCPService

        assert services.MCPService is MCPService

    def test_lazy_import_kb_service(self):
        """KbService is lazy-imported on first access."""
        from dataengineer.api.services.kb_service import KbService

        assert services.KbService is KbService

    def test_lazy_import_action_to_sse_event(self):
        """action_to_sse_event is lazy-imported on first access."""
        from dataengineer.api.services.action_sse_converter import action_to_sse_event

        assert services.action_to_sse_event is action_to_sse_event

    def test_lazy_import_agent_service(self):
        """AgentService is lazy-imported on first access."""
        from dataengineer.api.services.agent_service import AgentService

        assert services.AgentService is AgentService


class TestLazyImportErrors:
    """Tests for invalid attribute access."""

    def test_nonexistent_attribute_raises(self):
        """Accessing non-existent attribute raises AttributeError."""
        with pytest.raises(AttributeError, match="has no attribute 'NonExistentService'"):
            _ = services.NonExistentService
