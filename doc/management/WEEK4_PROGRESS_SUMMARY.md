# Week 4 — Progress summary (manager)

**Project:** Group 3 AMS Algorithmic Intelligence Engine  
**Week:** 4 of 11 — Usable HTML chat UI (**in progress**)  
**Team:** Hugo Davion & Axel Brazeau  
**Repository:** https://github.com/AMSNextGen25-26/chatbot-AMS

## Executive summary

**Week 3 is complete** (backend API). **Week 4 is in progress**: we are delivering a **browser-openable chat page** connected to **`POST /chat`**, with **suggested starter questions** so new employees know what to ask (US-02). Sources and RAG remain planned for **Week 7**; React UI for **Week 8**.

## Progress so far (Week 4)

| # | Item | Status | Evidence |
|---|------|--------|----------|
| 1 | HTML chat shell | In progress | `frontend/chat-live/index.html` |
| 2 | Wired to `POST /chat` | In progress | Same-origin fetch from `/ui/` |
| 3 | Suggested questions (≥4) | In progress | US-02 prompts in UI |
| 4 | Served by FastAPI | In progress | `GET /ui/` mount in `backend/main.py` |
| 5 | Pytest | In progress | `tests/test_week3.py`, `tests/test_week4.py` |
| 6 | Demo / troubleshooting notes | In progress | This file + `doc/developer/SETUP.md` |

## Manager demo checklist (~10 min)

| Step | Action | What to show |
|------|--------|--------------|
| 1 | `uvicorn main:app --reload --app-dir backend` | API starts on port 8000 |
| 2 | Start LM Studio (Mistral, port 1234) | `GET /health` → Mistral online |
| 3 | Open **http://localhost:8000/ui/** | Live chat page (not the Week 2 static preview) |
| 4 | Click a **suggested question** | Reply appears; mode `mistral` in metadata |
| 5 | Type a custom question | Conversation history preserved |
| 6 | Stop LM Studio, send again | `mode: fallback` — graceful degradation |
| 7 | `pytest tests/ -v` | Automated checks green |

**Note:** First Mistral reply on CPU may take **1–2 minutes** — the UI shows a waiting hint; this is expected for the POC.

## Still to close before Week 4 sign-off

- Manager review of chat UX vs Figma template  
- Confirm suggested questions cover onboarding scope  
- Week 5 prep: NBQ + Change Risk endpoints  

## Week 5 commitment

- `POST /nbq/next` and `POST /change-risk`  
- Algorithm test bench (HTML)  

## Risks

| Risk | Mitigation |
|------|------------|
| Slow Mistral on CPU | Typing hint + troubleshooting table in SETUP |
| Manager expects sources in chat | RAG is Week 7 — mode badge shows `retrieval: none` today |
| Confusion with static Figma preview | Banner on design-preview points to `/ui/` for live chat |
