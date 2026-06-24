"""Week 3 — health and minimal chat tests."""

import sys
from pathlib import Path

from fastapi.testclient import TestClient

BACKEND_DIR = Path(__file__).resolve().parent.parent / "backend"
sys.path.insert(0, str(BACKEND_DIR))

from main import app  # noqa: E402

client = TestClient(app)


def test_health_returns_online():
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["api"] == "online"
    assert body["ai"]["rag"]["enabled"] is False
    assert body["ai"]["rag"]["chunks_indexed"] == 0


def test_chat_returns_json_shape():
    response = client.post(
        "/chat",
        json={"messages": [{"role": "user", "content": "Hello"}]},
    )
    assert response.status_code == 200
    body = response.json()
    assert "reply" in body
    assert body["mode"] in ("mistral", "fallback")
    assert body["retrieval_method"] == "none"
    assert isinstance(body["sources"], list)


def test_openapi_lists_week3_routes():
    schema = client.get("/openapi.json").json()
    assert "/health" in schema["paths"]
    assert "/chat" in schema["paths"]
