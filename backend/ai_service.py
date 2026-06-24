"""AI health checks — LM Studio probe (Week 3)."""

from __future__ import annotations

import requests

from config import LM_STUDIO_MODEL, LM_STUDIO_URL

_resolved_model: str | None = None


def resolve_lm_studio_model(force_refresh: bool = False) -> str:
    """Pick the chat model id exposed by LM Studio (skips embedding models)."""
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
