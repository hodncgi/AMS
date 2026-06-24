"""Backend configuration — LM Studio (Week 3)."""

import os

LM_STUDIO_URL = os.getenv(
    "LM_STUDIO_URL",
    "http://localhost:1234/v1/chat/completions",
)
LM_STUDIO_MODEL = os.getenv("LM_STUDIO_MODEL", "auto")
LM_STUDIO_TIMEOUT = int(os.getenv("LM_STUDIO_TIMEOUT", "300"))
LM_STUDIO_MAX_TOKENS_CHAT = int(os.getenv("LM_STUDIO_MAX_TOKENS_CHAT", "384"))
AI_FALLBACK_ENABLED = os.getenv("AI_FALLBACK_ENABLED", "true").lower() == "true"
