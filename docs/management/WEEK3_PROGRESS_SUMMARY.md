# Week 3 — Progress summary (manager)

**Project:** Group 3 AMS Algorithmic Intelligence Engine  
**Week:** 3 of 11 — Backend foundation & minimal chat  
**Team:** Hugo Davion & Axel Brazeau  
**Repository:** https://github.com/hodncgi/AMS

## Executive summary

Week 3 delivers the **first runnable backend**: FastAPI with **`GET /health`**, **`POST /chat`** (direct Mistral, no RAG yet), **CORS**, and **pytest**. Stakeholders can call the chat API from curl or Swagger while the HTML UI ships in Week 4.

## Completed deliverables

| # | Deliverable | Evidence |
|---|-------------|----------|
| 1 | FastAPI skeleton | `backend/main.py`, `config.py`, `ai_service.py` |
| 2 | `GET /health` | LM Studio probe + RAG stub |
| 3 | `POST /chat` (minimal) | Mistral direct; fallback message if offline |
| 4 | CORS | `localhost:3000` |
| 5 | Pytest | `tests/test_week3.py` |
| 6 | Run instructions | `docs/developer/SETUP.md`, `backend/README.md` |

## What to demo (15 min)

1. `uvicorn main:app --reload --app-dir backend`  
2. `curl http://localhost:8000/health`  
3. Open **http://localhost:8000/docs** → try `POST /chat`  
4. Stop LM Studio → show `mode: fallback` in chat response  
5. `pytest tests/ -v`  

## Week 4 commitment

- HTML chat page wired to `POST /chat`  
- Suggested starter questions (US-02)  
- End-to-end browser demo  

## Risks

| Risk | Mitigation |
|------|------------|
| LM Studio slow on CPU | Document timeout; Week 7 adds knowledge fallback |
| Manager expects sources | Explain RAG is Week 7; Week 3 proves chat loop |
