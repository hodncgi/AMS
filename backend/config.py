"""Backend configuration — LM Studio connectivity (Week 3)."""

import os

LM_STUDIO_URL = os.getenv(
    "LM_STUDIO_URL",
    "http://localhost:1234/v1/chat/completions",
)
LM_STUDIO_MODEL = os.getenv("LM_STUDIO_MODEL", "auto")
AI_FALLBACK_ENABLED = os.getenv("AI_FALLBACK_ENABLED", "true").lower() == "true"
