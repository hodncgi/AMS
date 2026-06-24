# Week 3 — Progress summary (manager)

**Project:** Group 3 AMS Algorithmic Intelligence Engine  
**Week:** 3 of 11 — Backend foundation & minimal chat (**in progress**)  
**Team:** Hugo Davion & Axel Brazeau  
**Repository:** https://github.com/AMSNextGen25-26/chatbot-AMS

## Executive summary

**Week 2 is complete** (architecture, API draft, Figma preview, LM Studio). **Week 3 is in progress**: we are building the first runnable backend — FastAPI with **`GET /health`**, **`POST /chat`** (direct Mistral, no RAG yet), **CORS**, and **pytest**. Stakeholders can already try the API via Swagger; the HTML chat UI is planned for **Week 4**.

## Progress so far (Week 3)

| # | Item | Status | Evidence |
|---|------|--------|----------|
| 1 | FastAPI skeleton | In progress | `backend/main.py`, `config.py`, `ai_service.py` |
| 2 | `GET /health` | In progress | LM Studio probe + RAG stub |
| 3 | `POST /chat` (minimal) | In progress | Mistral direct; fallback if offline |
| 4 | CORS | In progress | `localhost:3000` |
| 5 | Pytest | In progress | `tests/test_week3.py` |
| 6 | Run instructions | In progress | `doc/developer/SETUP.md`, `backend/README.md` |

## What to demo today (15 min)

1. `uvicorn main:app --reload --app-dir backend`  
2. `curl http://localhost:8000/health`  
3. Open **http://localhost:8000/docs** → try `POST /chat`  
4. Stop LM Studio → show `mode: fallback` in chat response  
5. `pytest tests/ -v`  

## Still to close before Week 3 sign-off

- Internal review of Week 3 deliverables against roadmap  
- Manager acknowledgment of Week 3 scope  
- Update repo status to **Week 3 complete** at end of week  

## Week 4 commitment

- HTML chat page wired to `POST /chat`  
- Suggested starter questions (US-02)  
- End-to-end browser demo  

## Risks

| Risk | Mitigation |
|------|------------|
| LM Studio slow on CPU | Document timeout; Week 7 adds knowledge fallback |
| Manager expects sources | Explain RAG is Week 7; Week 3 proves chat loop |
