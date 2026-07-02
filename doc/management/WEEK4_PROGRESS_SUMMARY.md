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
| 5 | Pytest | In progress | `tests/test_week4.py` |

## What to demo today (15 min)

1. Start LM Studio (Mistral) + backend  
2. Open **http://localhost:8000/ui/**  
3. Click a suggested question → show assistant reply  
4. Type a custom question  
5. Stop LM Studio → show `mode: fallback` in reply metadata  

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
| Slow Mistral on CPU | Show typing indicator; document timeout in SETUP |
| Manager expects sources in chat | RAG is Week 7 — mode badge shows `retrieval: none` today |
