import pytest
from context_router.router import ContextRouter


def test_router_initialization():
    router = ContextRouter()
    assert isinstance(router, ContextRouter)


def test_router_route_basic():
    router = ContextRouter()
    query = "test query"
    result = router.route(query)
    assert result == f"Routed: {query}"
