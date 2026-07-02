# Week 3 — Progress summary (manager)

**Project:** Group 3 AMS Algorithmic Intelligence Engine  
**Week:** 3 of 11 — Backend foundation & minimal chat (**complete**)  
**Team:** Hugo Davion & Axel Brazeau  
**Repository:** https://github.com/AMSNextGen25-26/chatbot-AMS

## Executive summary

**Week 3 is complete.** We delivered the first runnable backend: FastAPI with **`GET /health`**, **`POST /chat`** (direct Mistral, no RAG yet), **CORS**, and **pytest**. Stakeholders can call the API from curl or Swagger. **Week 4** adds the browser chat page.

## Completed deliverables

| # | Deliverable | Evidence |
|---|-------------|----------|
| 1 | FastAPI skeleton | `backend/main.py`, `config.py`, `ai_service.py` |
| 2 | `GET /health` | LM Studio probe + RAG stub |
| 3 | `POST /chat` (minimal) | Mistral direct; fallback if offline |
| 4 | CORS | `localhost:3000` (React Week 8) |
| 5 | Pytest | `tests/test_week3.py` |
| 6 | Run instructions | `doc/developer/SETUP.md`, `backend/README.md` |

## Demo recap

1. `uvicorn main:app --reload --app-dir backend`  
2. `curl http://localhost:8000/health`  
3. **http://localhost:8000/docs** → `POST /chat`  
4. Fallback mode when LM Studio is offline  
5. `pytest tests/ -v`  

## Week 4 handover

- HTML chat at **http://localhost:8000/ui/**  
- Suggested starter questions (US-02)  
- End-to-end browser demo  
