"""Override parent's parameterized fixture. rdb/ tests are SQLite-specific."""

import pytest

from dataengineer.storage.backend_holder import init_backends
from dataengineer.storage.registry import clear_storage_registry


@pytest.fixture(autouse=True)
def _init_storage_backends(tmp_path):
    """Always use default backends — no parameterization for backend-specific tests."""
    init_backends(data_dir=str(tmp_path))
    yield
    clear_storage_registry()
