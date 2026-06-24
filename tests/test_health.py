"""Week 3 — health endpoint tests."""

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
    assert "lm_studio" in body["ai"]
    assert body["ai"]["rag"]["enabled"] is False
    assert body["ai"]["rag"]["chunks_indexed"] == 0
    assert isinstance(body["fallback_enabled"], bool)


def test_openapi_docs_available():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    schema = response.json()
    assert "/health" in schema["paths"]
