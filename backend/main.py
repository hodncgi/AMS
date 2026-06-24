"""G3 AI Engine — FastAPI entry point (Week 3: /health)."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ai_service import check_ai_health
from config import AI_FALLBACK_ENABLED

app = FastAPI(
    title="G3 AI Engine",
    description="AMS intake decision engine — NBQ, change risk, and onboarding chat",
    version="0.3.0-week3",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    return {
        "api": "online",
        "ai": check_ai_health(),
        "fallback_enabled": AI_FALLBACK_ENABLED,
    }
