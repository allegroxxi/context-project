from abc import ABC, abstractmethod
from typing import List, Sequence

from returns.future import FutureResult
from returns.result import Success, Failure

from .models import (
    Document,
    Query,
    RoutedContext,
    RouterError,
)


class BaseRouter(ABC):
    """
    Abstract base class for all routing components.
    """

    @abstractmethod
    async def route(
        self, query: Query, documents: Sequence[Document]
    ) -> FutureResult[List[Document], RouterError]:
        """
        Routes the query to the most relevant context.
        """
        pass


class SemanticRouter(BaseRouter):
    """
    A lightweight router using embedding-based semantic similarity.
    (MVP: Mock implementation)
    """

    async def route(
        self, query: Query, documents: Sequence[Document]
    ) -> FutureResult[List[Document], RouterError]:
        # Mocking semantic filtering: return top 2 documents if they exist
        if not documents:
            return FutureResult.from_result(
                Failure(RouterError("No documents provided for routing"))
            )

        # Simulate async processing
        import asyncio

        await asyncio.sleep(0.01)

        # Mock logic: return the most relevant looking docs (top 2)
        top_docs = list(documents[:2])
        return FutureResult.from_result(Success(top_docs))


class ContextRouter:
    """
    The main orchestrator for the dynamic context routing pipeline.
    """

    def __init__(self, router: BaseRouter):
        self._router = router

    async def orchestrate(
        self, query: Query, raw_documents: Sequence[Document]
    ) -> FutureResult[RoutedContext, RouterError]:
        """
        The primary entry point that manages the routing pipeline.
        """
        # Implementation of the "Poetic" pipeline
        # 1. Route the documents
        # 2. Map the result to a RoutedContext
        
        routed_result = await self._router.route(query, raw_documents)
        return routed_result.map(self._build_routed_context)

    def _build_routed_context(
        self, routed_docs: List[Document]
    ) -> RoutedContext:
        """
        Converts filtered documents into a single RoutedContext object.
        """
        combined_text = "\n\n".join([d.content for d in routed_docs])
        token_count = len(combined_text.split())  # Crude estimate

        return RoutedContext(
            combined_text=combined_text,
            source_documents=tuple(routed_docs),
            token_count=token_count,
        )
