# 🎯 Project Purpose
Implement token-efficient, dynamic context routing to optimize LLM performance by selecting and injecting only the most relevant information into prompts, reducing latency and token consumption for RAG and multi-agent systems.

# 📂 Project Context
## 🛠 Development Environment
- **Python Interpreter:** `/Users/christopherfleck/Projects/Context/venv/bin/python`
- **Rule:** Always use the absolute path to the `Context/venv/` interpreter/pip.
- **Verify:** Run `ls -F Context/` to confirm `venv/` exists before Python tasks.

## 📜 Standards & Documentation
- **Coding Standards:** [CODING_STANDARDS.md](../docs/CODING_STANDARDS.md)
- **Implementation Roadmap:** [technical_proposal.md](../docs/technical_proposal.md)

## 🤖 Agent Instructions
- **Imports:** On `ModuleNotFoundError`, check `Context/venv/bin/pip list` instead of guessing.
- **Anti-Loop:** If a command fails twice with the same error, stop, diagnose (e.g., `sys.path`), and report. No third attempts.
- **Research:** Use `agent` with web-search/fetch for real-time info; do not rely on internal synthesis for unknown data.

### 🧠 Reasoning & Interaction
- **CoT:** Decompose complex tasks into reasoning steps before tool use.
- **Communication:** Use precise, structured formats (Markdown tables/JSON) and maintain professional tone.
- **Inquiry:** Use neutral, non-leading questions for clarification.
- **Hierarchy:** Highlight critical info (blockers, root causes) prominently.
- **Adversarial Analysis:** Perform adversarial analysis (identifying edge cases, potential failures, or logical vulnerabilities) with every change.
