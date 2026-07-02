"""G3 AI Engine — FastAPI entry point (Week 4)."""

from pathlib import Path
from typing import List, Literal

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from ai_service import check_ai_health, generate_chat_minimal
from config import AI_FALLBACK_ENABLED

CHAT_UI_DIR = Path(__file__).resolve().parent.parent / "frontend" / "chat-live"

app = FastAPI(
    title="G3 AI Engine",
    description="AMS intake decision engine — Week 4: health, chat API, HTML chat UI",
    version="0.4.0-week4",
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


class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str = Field(min_length=1)


class ChatRequest(BaseModel):
    messages: List[ChatMessage] = Field(min_length=1)


@app.get("/health")
async def health_check():
    return {
        "api": "online",
        "ai": check_ai_health(),
        "fallback_enabled": AI_FALLBACK_ENABLED,
    }


@app.post("/chat")
async def chat(request: ChatRequest):
    if request.messages[-1].role != "user":
        raise HTTPException(
            status_code=400,
            detail="Last message must be from the user.",
        )
    payload = [m.model_dump() for m in request.messages]
    return generate_chat_minimal(payload)


if CHAT_UI_DIR.is_dir():
    app.mount("/ui", StaticFiles(directory=str(CHAT_UI_DIR), html=True), name="chat-ui")
