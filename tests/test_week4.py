"""Week 4 — HTML chat UI served by FastAPI."""

import sys
from pathlib import Path

from fastapi.testclient import TestClient

BACKEND_DIR = Path(__file__).resolve().parent.parent / "backend"
sys.path.insert(0, str(BACKEND_DIR))

from main import app  # noqa: E402

client = TestClient(app)


def test_chat_ui_index_served():
    response = client.get("/ui/")
    assert response.status_code == 200
    assert "Onboarding Assistant" in response.text
    assert "suggested" in response.text.lower() or "Ask the assistant" in response.text


def test_chat_ui_lists_suggested_questions():
    response = client.get("/ui/index.html")
    assert response.status_code == 200
    assert "What is this assistant for?" in response.text
    assert "How does AMS intake work?" in response.text
