# 🎯 Project Purpose

**Token-efficient, dynamic context routing** optimizes LLM performance by intelligently selecting and injecting only the most relevant information into prompts. This reduces latency and token consumption, making it ideal for scaling Retrieval-Augmented Generation (RAG) and multi-agent systems.

# 📂 Project Context

## 🛠 Development Environment

### ⚙️ Environment Details
- **Interpreter Location:** `/Users/christopherfleck/Projects/Context/venv/bin/python`
- **Environment Type:** `venv`

### 🛡️ Usage Rules
- **Crucial Rule:** Always use the absolute path to the interpreter in `Context/venv/` instead of the system `python` or `pip`.
- **Verification Step:** Before starting any Python-related task, run `ls -F Context/` to confirm the `venv/` directory is present.

## 🤖 Agent Instructions

- **Import Resolution:** If encountering `ModuleNotFoundError`, do not attempt to guess the fix. First, verify if the package exists in the `Context/venv/` environment using `Context/venv/bin/pip list`.
- **Avoid Loops:** If a command fails twice with the same error, stop immediately. Diagnose the root cause (e.g., checking `which python` or `sys.path`) and report the failure to the user. Do not attempt a third variation of the same command.
- **Research & Troubleshooting:** If local investigation is insufficient to resolve an error or answer a complex question, use the `agent` tool to perform research, which may include web-based searches. **Mandate: Use web-search/fetch tools for real-time information; do not fallback to internal synthesis.**

### 🧠 Reasoning & Interaction Principles

- **Chain-of-Thought (CoT) Reasoning:** For complex tasks, decompose the problem into intermediate reasoning steps before executing tool calls or edits.
- **Positive Constraint Enforcement:** Favor positive instructions (e.g., "Maintain a professional tone") over negative ones (e.g., "Don't be rude") when communicating with subagents or describing logic.
- **Structured & Precise Communication:** Use precise language and avoid ambiguity. When reporting findings, use structured formats like Markdown tables or JSON where appropriate.
- **Neutral Inquiry:** When resolving ambiguities with the user via `ask_user_question`, use neutral, non-leading questions to avoid bias.
- **Information Hierarchy:** Place critical information (e.g., root causes, blockers) at the beginning or end of responses to ensure visibility.
