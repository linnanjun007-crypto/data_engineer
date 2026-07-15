"""Authentication plugin interface and default implementations."""

from dataengineer.api.auth.context import AppContext
from dataengineer.api.auth.loader import load_auth_provider
from dataengineer.api.auth.no_auth_provider import NoAuthProvider
from dataengineer.api.auth.provider import AuthProvider, EvictCallback

__all__ = [
    "AppContext",
    "AuthProvider",
    "EvictCallback",
    "NoAuthProvider",
    "load_auth_provider",
]
