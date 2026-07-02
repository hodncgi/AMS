"""Week 4 — HTML chat UI served by FastAPI."""

import re
import sys
from pathlib import Path

from fastapi.testclient import TestClient

BACKEND_DIR = Path(__file__).resolve().parent.parent / "backend"
sys.path.insert(0, str(BACKEND_DIR))

from main import app  # noqa: E402

client = TestClient(app)

SUGGESTED_QUESTIONS = [
    "What is this assistant for?",
    "How does AMS intake work?",
    "What is the CI/CD process at CGI?",
    "What are the information security policies?",
]


def test_chat_ui_index_served():
    response = client.get("/ui/")
    assert response.status_code == 200
    assert "Onboarding Assistant" in response.text
    assert "Ask the assistant" in response.text


def test_chat_ui_has_four_suggested_questions():
    response = client.get("/ui/index.html")
    assert response.status_code == 200
    for question in SUGGESTED_QUESTIONS:
        assert question in response.text
    assert len(re.findall(r'SUGGESTED_QUESTIONS\s*=\s*\[', response.text)) == 1
