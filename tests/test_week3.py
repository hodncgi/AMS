"""Week 3 — health and minimal chat tests."""

import sys
from pathlib import Path
from unittest.mock import patch

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
    assert "status" in body["ai"]["lm_studio"]
    assert "model" in body["ai"]["lm_studio"]


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


def test_chat_returns_response_time_ms():
    response = client.post(
        "/chat",
        json={"messages": [{"role": "user", "content": "Hello"}]},
    )
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["response_time_ms"], int)
    assert body["response_time_ms"] >= 0


@patch("ai_service.call_lm_studio", side_effect=RuntimeError("LM Studio offline"))
def test_chat_fallback_when_lm_studio_fails(_mock_call):
    response = client.post(
        "/chat",
        json={"messages": [{"role": "user", "content": "Hello"}]},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["mode"] == "fallback"
    assert body["reply"]
    assert body["sources"] == []


def test_chat_rejects_empty_message_list():
    response = client.post("/chat", json={"messages": []})
    assert response.status_code == 422


def test_chat_rejects_empty_content():
    response = client.post(
        "/chat",
        json={"messages": [{"role": "user", "content": ""}]},
    )
    assert response.status_code == 422


def test_chat_rejects_last_message_not_user():
    response = client.post(
        "/chat",
        json={
            "messages": [
                {"role": "user", "content": "Hi"},
                {"role": "assistant", "content": "Hello"},
            ]
        },
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Last message must be from the user."


def test_openapi_lists_week3_routes():
    schema = client.get("/openapi.json").json()
    assert "/health" in schema["paths"]
    assert "/chat" in schema["paths"]
