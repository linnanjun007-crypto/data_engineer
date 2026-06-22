# dataengineer-agent

> 基于开源项目 [datus-ai/datus-agent](https://github.com/datus-ai/datus-agent)（Apache License 2.0）的二次开发版本。

一个 AI 驱动的数据工程智能体（NL2SQL Agent），通过自然语言交互与多智能体工作流，自动化数据分析、SQL 生成、语义建模与 BI 仪表盘生成。

---

## 关于本项目（二次开发说明）

本仓库是上游 [datus-ai/datus-agent](https://github.com/datus-ai/datus-agent) 的 fork，并在其基础上做了实质性二次开发。相对上游的主要改动如下：

### 相对上游的改动

- **命名重塑**：Python 包名 `datus` → `dataengineer`，CLI 入口 `datus-*` → `dataengineer-*`
- **新增调度 / ETL 体系**：`scheduler_tools`、scheduler Prompt 模板、Airflow 工作流 skill
- **新增 Skill 元系统**：`skill_validate_tool`、`create-skill` / `optimize-skill`，让 agent 能自主生成与校验 skill
- **新增 BI 仪表盘生成**：`gen-dashboard` / `gen-metrics` / `gen-table`，以及 Grafana / Superset 平台对接
- **新增 Reference Template 检索**：`storage/reference_template/`（约 1500 行），补强 RAG 召回能力
- **扩充模型矩阵**：新增 Codex、GLM、MiniMax、OpenRouter 模型适配器，以及 LiteLLM prompt 缓存控制
- **删除 Superset 重资产**：移除原版约 4900 行手写 Superset 适配器，替换为更轻量的 BI 工具集
- **重写核心文件**：`database`、`filesystem`、`session_manager`、`claude_model` 等核心模块有较大改动

### 开发方式

本仓库的二次开发与文档编写过程中使用了 Claude Code 辅助（AI 编程工具）。

---

## 架构

DataEngineer 是一个模块化、事件驱动的智能体平台，采用分层设计：

- **表现层**：CLI（Textual TUI）、Web Chatbot、FastAPI、以及 Slack / Feishu 网关适配器
- **智能体层**：可插拔的工作流引擎，用 YAML 定义的 DAG 编排 chat / compare / dashboard / feedback 等节点
- **工具层**：按领域组织的 100+ 工具——数据库查询、语义层、MCP、搜索、日期解析、血缘图、BI 仪表盘组装
- **存储层**：SQLite、LanceDB（向量）、文件存储等多后端，覆盖文档、语义模型、Schema、指标、反馈、任务历史
- **模型层**：对 Claude、Codex、DeepSeek、Qwen、OpenRouter、LiteLLM 等 LLM 提供商的统一抽象

数据流：用户输入 → 智能体工作流（plan → execute → reflect → evaluate）→ 工具执行（DB 查询 / 语义检索 / LLM 调用）→ 结果聚合 → 响应渲染。

---

## 快速开始

环境要求：Python 3.12+，包管理器 [uv](https://docs.astral.sh/uv/)。

```bash
# 1. 安装依赖
uv sync

# 2. 初始化配置
data_engineer-agent init

# 3. 配置 LLM
data_engineer config set target.provider openai
data_engineer config set target.model gpt-4o
```

启动交互式 CLI：

```bash
data_engineer-cli --datasource demo
```

启动 REST API：

```bash
data_engineer-api --port 8080
```

常用命令示例：

```bash
data_engineer-cli /tables                 # 查看表列表
data_engineer-cli /Describe <table>       # 查看表结构
data_engineer-cli /Check <自然语言查询>    # 执行 NL 查询
data_engineer-cli /feedback <result> <correction>   # 提交反馈，供 agent 学习
```

---

## 许可

本仓库沿用上游的 [Apache License 2.0](LICENSE)。上游代码版权归 DatusAI, Inc. 所有；二次开发部分遵循同一许可证。
