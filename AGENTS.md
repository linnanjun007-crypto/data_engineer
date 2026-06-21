# data_engineer

An intelligent data engineering agent platform that automates data analysis, SQL generation, semantic modeling, and BI dashboard creation through natural language interaction and multi-agent workflows.

## Architecture

DataEngineer is a modular, event-driven agent platform built on a Python async framework with a FastAPI web layer and a Textual-based TUI client. The architecture follows a layered design:

- **Presentation Layer**: CLI (Textual TUI), Web Chatbot, API (FastAPI), and Gateway adapters (Slack, Feishu)
- **Agent Layer**: A pluggable workflow engine that orchestrates specialized nodes (chat, compare, feedback, dashboard generation) using a directed acyclic graph (DAG) defined in YAML
- **Tool Layer**: Over 100 tools organized by domain — database querying, semantic layer operations, MCP (Model Context Protocol) tools, search, date parsing, lineage graph, and BI dashboard assembly
- **Storage Layer**: Multiple backends including SQLite, LanceDB (vector), and file-based storage for documents, semantic models, schemas, metrics, feedback, and task history
- **Model Layer**: Abstraction over LLM providers (Claude, Codex, DeepSeek, Qwen, OpenRouter, LiteLLM) with unified interfaces

Data flows through the system as follows: User input → Agent Workflow (plan → execute → reflect → evaluate) → Tool execution (DB queries, semantic lookups, LLM calls) → Result aggregation → Response rendering.

```
┌─────────────────────────────────────────────────────────────┐
│                      Presentation Layer                      │
│  ┌─────────┐  ┌────────────┐  ┌────────┐  ┌──────────────┐ │
│  │ TUI CLI │  │ Web Chatbot│  │  API   │  │ Slack/Feishu │ │
│  └────┬────┘  └─────┬──────┘  └───┬────┘  └──────┬───────┘ │
├───────┴──────────────┴────────────┴───────────────┴─────────┤
│                    Agent Orchestration Layer                  │
│  ┌──────────────────────────────────────────────────────┐    │
│  │  Workflow Engine (DAG: Plan → Execute → Reflect)     │    │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────┐ │    │
│  │  │Chat Node │ │Compare   │ │Dashboard│ │Feedback│ │    │
│  │  │          │ │Agentic   │ │Generator│ │Agentic │ │    │
│  │  └──────────┘ └──────────┘ └──────────┘ └────────┘ │    │
│  └──────────────────────────────────────────────────────┘    │
├─────────────────────────────────────────────────────────────┤
│                      Tool Layer                               │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────────────┐ │
│  │ DB Tools │ │Semantic  │ │  MCP     │ │ Search/Lineage │ │
│  │ (SQL,    │ │ Tools    │ │ Tools    │ │ Tools          │ │
│  │  Config) │ │(Models,  │ │(Servers, │ │                │ │
│  │          │ │ Metrics) │ │ Config)  │ │                │ │
│  └──────────┘ └──────────┘ └──────────┘ └────────────────┘ │
├─────────────────────────────────────────────────────────────┤
│                     Storage Layer                             │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌────────┐ │
│  │SQLite│ │Lance │ │Doc   │ │Schema│ │Metric│ │Feedback│ │
│  │      │ │DB    │ │Store │ │Meta  │ │Store │ │Store   │ │
│  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## Directory Map

| Directory | Purpose | Key Entry Point | Consumer |
|-----------|---------|-----------------|----------|
| `dataengineer/` | Core application package | `main.py`, `mcp_server.py` | Python importers, CLI, API |
| `dataengineer/agent/` | Agent workflow orchestration | `workflow.py`, `workflow_runner.py` | Agent execution engine |
| `dataengineer/agent/node/` | Individual workflow node implementations | `begin_node.py`, `chat_agentic_node.py`, `compare_agentic_node.py` | Workflow runner |
| `dataengineer/api/` | FastAPI web service layer | `main.py`, `routes/` | HTTP clients, web UI |
| `dataengineer/cli/` | Command-line interface (Textual TUI + rich CLI) | `agent_commands.py`, `tui/app.py` | End users |
| `dataengineer/tools/` | Tool implementations across domains | `registry/tool_registry.py` | Agent nodes, API |
| `dataengineer/tools/db_tools/` | Database connection and query tools | `config.py`, `builtin_configs.py` | SQL execution |
| `dataengineer/tools/semantic_tools/` | Semantic layer management tools | `base.py`, `registry.py`, `storage_sync.py` | Model/metric operations |
| `dataengineer/tools/mcp_tools/` | Model Context Protocol integration | `mcp_manager.py`, `mcp_server.py` | External tool access |
| `dataengineer/models/` | LLM provider abstractions | `base.py`, `claude_model.py`, `codex_model.py` | Agent reasoning |
| `dataengineer/storage/` | Persistence backends | `base.py`, `backend_holder.py` | All data operations |
| `dataengineer/storage/semantic_model/` | Semantic model storage | `store.py`, `semantic_model_init.py` | Model CRUD |
| `dataengineer/storage/schema_metadata/` | Database schema metadata | `store.py`, `local_init.py`, `benchmark_init.py` | Schema discovery |
| `dataengineer/storage/vector/` | Vector embeddings storage | `lance_backend.py` | Semantic search |
| `dataengineer/configuration/` | Configuration loading and management | `agent_config.py`, `project_config.py` | System bootstrap |
| `dataengineer/gateway/` | Chat platform integrations | `main.py`, `bridge.py` | Slack, Feishu users |
| `dataengineer/prompts/` | LLM prompt templates (Jinja2) | `prompt_templates/` | Agent node execution |
| `dataengineer/schemas/` | Data models and schemas | `agent_models.py`, `action_bus.py` | Internal data flow |
| `dataengineer/auth/` | Authentication and OAuth | `oauth_manager.py`, `token_storage.py` | User identity |
| `dataengineer/utils/` | Shared utility functions | Various utility modules | All packages |
| `conf/` | Runtime configuration files | `agent.yml`, `providers.yml` | System startup |
| `tests/` | Test suite (unit, integration, regression) | `conftest.py` | CI/CD, developers |
| `benchmark/` | Benchmarking and evaluation framework | `scripts/evaluation.py`, `scripts/gen_benchmark.py` | Performance testing |
| `docs/` | Documentation site (MkDocs) | `mkdocs.yml`, `index.md` | End users, developers |
| `sample_data/` | Demo datasets | `duckdb-demo.duckdb`, `california_schools/` | Tutorials, demos |
| `quickstart/` | Docker Compose quickstart setups | `data_engineering/airflow/`, `data_engineering/superset/` | New users |
| `build_scripts/` | Build and deployment scripts | `Dockerfile`, `build_pypi_package.py` | CI/CD, packaging |
| `ci/` | CI/CD helper scripts | `run-tests-and-coverage.py`, `run-pr-tests.py` | GitHub Actions |
| `scripts/` | Utility and debug scripts | `run_regression.sh`, `optimize_recall/` | Developers |

## Services

| Name | Type | Connection |
|------|------|------------|
| demo | DuckDB | `duckdb:///sample_data/duckdb-demo.duckdb` |

**Additional detected services**:

| Service | Type | Source | Notes |
|---------|------|--------|-------|
| Apache Airflow | Workflow Orchestration | `quickstart/data_engineering/airflow/docker-compose.yml` | Optional demo integration |
| Apache Superset | BI Platform | `quickstart/data_engineering/superset/docker-compose.yml` | Optional demo integration |
| LLM Providers | External API | `conf/providers.yml` | Claude, Codex, DeepSeek, Qwen, OpenRouter, LiteLLM |
| MCP Servers | External Tools | `dataengineer/tools/mcp_tools/` | Model Context Protocol servers (configurable) |
| LanceDB | Vector Database | `dataengineer/storage/vector/lance_backend.py` | Local vector storage for semantic search |
| SQLite | Relational Database | `dataengineer/storage/rdb/sqlite_backend.py` | Primary metadata and configuration storage |

## Artifacts

| Artifact | Location | Description |
|----------|----------|-------------|
| **Agent Configuration** | `conf/agent.yml` | YAML-based agent workflow definitions, node configurations, and tool bindings |
| **Provider Configuration** | `conf/providers.yml` | LLM provider API keys, endpoints, and model settings |
| **Semantic Models** | `dataengineer/storage/semantic_model/` | Business-level data models defining metrics, dimensions, and relationships |
| **Database Schema Metadata** | `dataengineer/storage/schema_metadata/` | Cached database schemas, table structures, and column descriptions |
| **Reference SQL Templates** | `dataengineer/storage/reference_sql/`, `sample_data/` | Example SQL queries and Jinja2 templates for common patterns |
| **Benchmark Results** | `benchmark/` | CSV-based evaluation results (`success_story.csv`, `testing_set.csv`) and evaluation scripts |
| **Document Store** | `dataengineer/storage/document/` | Ingested documentation and knowledge base articles for context-aware queries |
| **Metric Store** | `dataengineer/storage/metric/` | Collected usage metrics and performance data |
| **Feedback Store** | `dataengineer/storage/feedback/` | User feedback on agent responses for continuous improvement |
| **Task History** | `dataengineer/storage/task/` | Execution logs and task state persistence |
| **Workflow Definitions** | `dataengineer/agent/workflow.yml` | YAML-defined DAGs for multi-step agent workflows |
| **Prompt Templates** | `dataengineer/prompts/prompt_templates/` | Jinja2 templates for LLM system prompts and few-shot examples |
| **API Schema** | `dataengineer/api/models/`, `dataengineer/schemas/` | Pydantic models defining API request/response contracts |
| **CLI Commands** | `dataengineer/cli/` | Rich CLI interface with autocomplete, TUI, and web chat modes |
| **MCP Server Config** | `dataengineer/tools/mcp_tools/mcp_config.py` | Configuration for external MCP tool servers |
| **Vector Embeddings** | `dataengineer/storage/vector/` | LanceDB-backed vector embeddings for semantic search |