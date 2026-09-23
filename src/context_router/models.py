from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple, Mapping
from pydantic import BaseModel, ConfigDict

@dataclass(frozen=True)
class RouterError:
    """Base class for routing errors."""
    message: str

@dataclass(frozen=True)
class Query:
    """
    Represents the user's input request.
    """
    text: str
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Document:
    """
    Represents a single chunk of retrieved context.
    """
    content: str
    score: float
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class RoutedContext:
    """
    The final, optimized context block prepared for the LLM.
    """
    combined_text: str
    source_documents: Tuple[Document, ...]
    token_count: int
    metadata: Mapping[str, Any] = field(default_factory=dict)
