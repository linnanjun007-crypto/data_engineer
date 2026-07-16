"""API routes for direct tool dispatch."""

from typing import Annotated, Dict, Optional

from fastapi import APIRouter, Body, Path

from dataengineer.api.deps import ServiceDep
from dataengineer.api.models.base_models import Result
from dataengineer.tools.func_tool.base import FuncToolResult

router = APIRouter(prefix="/api/v1/tools", tags=["tools"])


@router.post(
    "/{tool_name}",
    response_model=Result[FuncToolResult],
    summary="Execute Tool",
    description="Execute a tool by name with parameters passed in the request body.",
)
def execute_tool(
    tool_name: Annotated[str, Path(description="Name of the tool to execute")],
    svc: ServiceDep,
    params: Annotated[Optional[Dict], Body()] = None,
) -> Result[FuncToolResult]:
    """Execute a tool by name."""
    if params is None:
        params = {}
    return svc.tool.execute(tool_name, params)
