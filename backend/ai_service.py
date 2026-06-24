"""AI service — LM Studio health + minimal chat (Week 3, no RAG)."""

from __future__ import annotations

import json
import re
import time

import requests

from config import (
    AI_FALLBACK_ENABLED,
    LM_STUDIO_MAX_TOKENS_CHAT,
    LM_STUDIO_MODEL,
    LM_STUDIO_TIMEOUT,
    LM_STUDIO_URL,
)

_resolved_model: str | None = None

WEEK3_CHAT_SYSTEM_PROMPT = (
    "You are the CGI Technical Onboarding AI Assistant powered by Mistral. "
    "Answer in clear, professional English. Be concise and helpful. "
    "If you do not know something, say so honestly."
)


def resolve_lm_studio_model(force_refresh: bool = False) -> str:
    global _resolved_model
    if _resolved_model and not force_refresh:
        return _resolved_model

    if LM_STUDIO_MODEL not in ("", "auto", "local-model"):
        _resolved_model = LM_STUDIO_MODEL
        return _resolved_model

    try:
        models_url = LM_STUDIO_URL.replace("/chat/completions", "/models")
        response = requests.get(models_url, timeout=5)
        response.raise_for_status()
        for item in response.json().get("data", []):
            model_id = item.get("id", "")
            if model_id and "embed" not in model_id.lower():
                _resolved_model = model_id
                return _resolved_model
    except Exception as error:
        print(f"LM Studio model auto-detection failed: {error!r}")

    _resolved_model = "mistral"
    return _resolved_model


def check_lm_studio_health() -> dict:
    model = resolve_lm_studio_model()
    try:
        response = requests.get(
            LM_STUDIO_URL.replace("/chat/completions", "/models"),
            timeout=5,
        )
        if response.status_code == 200:
            return {"status": "online", "model": model}
        return {"status": "degraded", "model": model}
    except requests.exceptions.RequestException:
        return {"status": "offline", "model": model}


def check_ai_health() -> dict:
    return {
        "lm_studio": check_lm_studio_health(),
        "rag": {
            "enabled": False,
            "method": "keyword",
            "chunks_indexed": 0,
        },
    }


def _parse_reply_json(raw: str) -> str | None:
    cleaned = raw.strip()
    cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
    cleaned = re.sub(r"\s*```$", "", cleaned)
    try:
        data = json.loads(cleaned)
        if isinstance(data, dict) and data.get("reply"):
            return str(data["reply"])
    except json.JSONDecodeError:
        pass
    return cleaned if cleaned else None


def call_lm_studio(messages: list[dict]) -> str:
    model = resolve_lm_studio_model()
    response = requests.post(
        LM_STUDIO_URL,
        json={
            "model": model,
            "messages": messages,
            "temperature": 0.2,
            "max_tokens": LM_STUDIO_MAX_TOKENS_CHAT,
        },
        timeout=LM_STUDIO_TIMEOUT,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def generate_chat_minimal(messages: list[dict]) -> dict:
    """Week 3 chat — direct Mistral, no RAG."""
    started = time.perf_counter()
    user_messages = [m for m in messages if m.get("role") in ("user", "assistant")]

    lm_messages = [
        {"role": "system", "content": WEEK3_CHAT_SYSTEM_PROMPT},
        *user_messages,
    ]

    try:
        raw = call_lm_studio(lm_messages)
        reply = _parse_reply_json(raw) or raw.strip()
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        return {
            "reply": reply,
            "sources": [],
            "mode": "mistral",
            "retrieval_method": "none",
            "response_time_ms": elapsed_ms,
        }
    except Exception as error:
        print(f"LM Studio chat error: {error!r}")
        if not AI_FALLBACK_ENABLED:
            raise
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        return {
            "reply": (
                "The AI assistant is temporarily unavailable (LM Studio offline). "
                "Please start Mistral on port 1234 and try again. "
                "Knowledge-base fallback arrives in Week 7."
            ),
            "sources": [],
            "mode": "fallback",
            "retrieval_method": "none",
            "response_time_ms": elapsed_ms,
        }
