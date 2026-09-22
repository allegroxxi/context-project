# 📜 Coding Standards: Context Router

## ⚖️ Core Philosophies
1. **Explicit Over Implicit:** No `None` returns, no unhandled exceptions for domain errors, and no hidden side effects. Everything must be encoded in the function signature.
2. **Immutability by Default:** State is never modified; it is transformed into new instances.
3. **Async-First:** All I/O-bound operations must be asynchronous to prevent thread blocking.
4. **Type-Driven Development:** The type system (via `pyright`/`mypy`) is the primary tool for enforcing correctness and preventing runtime errors.

---

## 🛠️ 1. Functional Programming Patterns

We adopt the **[`returns`](https://github.com/dry-python/returns)** library to provide robust, type-safe monadic composition.

### 🧩 The Monadic Toolkit
| Pattern | Type/Monad | Purpose |
| :--- | :--- | :--- |
| **Optionality** | `Maybe[T]` | Replaces `Optional[T]`. Used when a value may be absent. |
| **Error Handling** | `Result[T, E]` | Replaces `try/except`. A function returns either `Success(T)` or `Failure(E)`. |
| **Void/Side-Effects** | `Unit` | A specialized return value for functions that perform an action but return no data. |
| **Async Flow** | `FutureResult[T, E]` | The async version of `Result`. Used for all I/O-bound operations that can fail. |

### 🔄 Example: The "Poetic" Async Pipeline
```python
from returns.io import FutureResult

async def optimized_context_flow(doc_id: str) -> FutureResult[RoutedContext, Error]:
    return await (
        fetch_document(doc_id)                 # Stage 1: Async fetch
        .map(strip_whitespace)                 # Stage 2: Pure transformation
        .bind(rerank_top_n)                    # Stage 3: Async reranking
        .bind(compress_tokens)                 # Stage 4: Async compression
        .bind(log_and_cache)                   # Stage 5: Side-effect tracking
    ).unwrap()
```

---

## 📦 2. Immutability & Data Integrity

All data carriers must be immutable to ensure thread-safety and predictable transformations.

* **Standard:** Use `dataclasses` with `frozen=True`.
* **Deep Immutability:** Avoid mutable collections (e.g., `list`, `dict`) as fields. Use `tuple` or `Mapping` instead.

```python
from dataclasses import dataclass
from typing import Tuple

@dataclass(frozen=True)
class Document:
    doc_id: str
    content: str
    metadata: Tuple[str, ...] 
```

---

## ⚡ 3. Side-Effect Management

To maintain functional purity, we must track whether a function has altered the system state. Functions that perform side effects must return a `Result` that explicitly includes status metadata.

### The `SideEffectMetadata` Pattern
```python
@dataclass(frozen=True)
class SideEffectMetadata:
    was_persisted: bool
    cache_invalidated: bool

@dataclass(frozen=True)
class ProcessResult:
    data: str
    metadata: SideEffectMetadata

def update_cache(key: str, value: str) -> Result[ProcessResult, str]:
    # ... logic ...
    meta = SideEffectMetadata(was_persisted=True, cache_invalidated=True)
    return Success(ProcessResult(data=value, metadata=meta))
```

---

## 🚀 4. Summary of Mandatory Rules

1. **Async Compliance:** Every function performing network, disk, or database access **MUST** be `async def` and return an `Async` monadic type.
2. **No `None`:** The use of `None` as a return value for logic is strictly forbidden. Use `Maybe` or `Result` instead.
3. **No `raise`:** Exceptions should only be used for unrecoverable system failures. Domain errors **MUST** use `Failure`.
4. **Strict Typing:** Every public function must have full type annotations, including generic parameters for monads.
