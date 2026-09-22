# 🏗️ Technical Proposal: Context Router Implementation

## 1. Architecture Overview
The system will follow a **multi-stage pipeline** designed to filter and compress information as it moves from raw retrieval to the final LLM prompt. The goal is to maximize the **Signal-to-Noise Ratio (SNR)** while minimizing token overhead.

### The Routing Pipeline
1.  **Input:** User Query + Raw Retrieved Documents (from an external Vector DB).
2.  **Stage 1: Semantic Gatekeeper (Bi-Encoder):** Use fast embeddings to filter the initial set of $k$ candidates.
3.  **Stage 2: Precision Reranker (Cross-Encoder):** Process the top $n$ candidates through a Cross-Encoder to produce high-precision similarity scores.
4.  **Stage 3: Information Compressor (LLMLingua-style):** Prune non-essential tokens from the highest-scoring chunks to minimize prompt size.
5.  **Output:** A compact, high-signal context block optimized for the target LLM.

---

## 2. Core Component Design

### 🧩 Data Models (`models.py`)
Using `pydantic` to ensure type safety and structured communication between components.
*   `Query`: Represents the user input and metadata.
*   `Document`: Represents a single chunk of retrieved text with its score.
*   `RoutedContext`: The final product, containing the compressed text and the routing metadata.

### 🧠 Component Interfaces

| Component | Interface | Responsible For |
| :--- | :--- | :--- |
| `BaseRouter` | `route(query: Query, docs: List[Document]) -> List[Document]` | Abstract base class for routing logic. |
| `SemanticRouter` | `route(...)` | Fast, embedding-based filtering (Bi-Encoder). |
| `Reranker` | `rerank(query: str, docs: List[Document]) -> List[Document]` | High-precision similarity scoring (Cross-Encoder). |
| `ContextCompressor`| `compress(text: str) -> str` | Perplexity-based token pruning. |
| `ContextRouter` | `orchestrate(query: Query, raw_docs: List[Document]) -> RoutedContext` | The main entry point that manages the pipeline. |

---

## 3. Detailed Implementation Roadmap

### 🚀 Phase 1: The Precision Router (MVP)
*Goal: Implement a working Bi-Encoder + Cross-Encoder pipeline.*
1.  **Refactor `ContextRouter`:** Transform the current skeleton into a pipeline orchestrator.
2.  **Implement `SemanticRouter`:** Integrate a lightweight embedding model (e.g., `sentence-transformers/all-MiniLM-L6-v2`).
3.  **Implement `Reranker`:** Integrate a Cross-Encoder model (e.g., `cross-encoder/ms-marco-MiniLM-L-6-v2`).
4.  **Unit Testing:** Verify that `ContextRouter.orchestrate` returns the correct top-$n$ documents.

### 📉 Phase 2: The Efficiency Engine
*Goal: Add token compression and optimization.*
1.  **Implement `ContextCompressor`:** Integrate a perplexity-based pruning mechanism.
2.  **Optimize Data Flow:** Ensure that compression only occurs on the documents that pass the reranking stage to save compute.
3.  **Benchmark:** Measure the "Token Compression Ratio" and "Latency vs. Accuracy" tradeoffs.

### 🤖 Phase 3: The Agentic Orchestrator & Evaluation
*Goal: Enable intelligent RAG decisions and automated testing.*
1.  **Implement Decision Logic:** Add a "Gatekeeper" step to decide if RAG is even necessary for the given query.
2.  **Implement Automated Evaluation Suite:** 
    *   Integrate **RAGAS** to automatically test the `faithfulness` and `relevance` of the routed context.
    *   Implement integration tests that simulate real-world RAG workflows.

---

## 4. Success Metrics (KPIs)
To verify the success of each phase, we will track:
*   **Latency:** Average time taken to process a query through the pipeline.
*   **Reduction Ratio:** $\frac{\text{Original Tokens}}{\text{Compressed Tokens}}$ (aiming for $>2\times$ reduction).
*   **Faithfulness Score:** RAGAS score ensuring the compressed context still contains the necessary truth.
*   **Hit Rate:** The percentage of relevant documents correctly identified by the reranker.
