# Week 3 — Progress summary (manager)

**Project:** Group 3 AMS Algorithmic Intelligence Engine  
**Week:** 3 of 11 — Backend skeleton & health check  
**Team:** Hugo Davion & Axel Brazeau  
**Repository:** https://github.com/hodncgi/AMS

## Executive summary

Week 3 delivers the **first runnable backend** in this repository: a FastAPI application with **`GET /health`**, **CORS** for the future React UI, **LM Studio connectivity probe**, and **pytest** coverage. Algorithm endpoints (`/nbq/next`, `/change-risk`, `/chat`) remain on schedule for Weeks 4–8 per the API contract drafted in Week 2.

## Completed deliverables

| # | Deliverable | Evidence in repo |
|---|-------------|------------------|
| 1 | FastAPI project skeleton | `backend/main.py`, `config.py`, `ai_service.py` |
| 2 | `GET /health` operational | `curl http://localhost:8000/health` |
| 3 | LM Studio status in health payload | `ai.lm_studio` field |
| 4 | CORS for `localhost:3000` | `main.py` middleware |
| 5 | OpenAPI auto-docs | http://localhost:8000/docs |
| 6 | Pytest suite | `tests/test_health.py` |
| 7 | Run instructions | `docs/developer/SETUP.md`, `backend/README.md` |

## What to demo in a 20-minute review

1. `uvicorn main:app --reload --app-dir backend` — start API  
2. `curl http://localhost:8000/health` — show `api: online` + LM Studio status  
3. Open **http://localhost:8000/docs** — live OpenAPI from implemented route  
4. `pytest tests/ -v` — automated health checks  
5. Revisit **openapi-draft.yaml** — `/health` now matches running service  

## Week 4 commitment

- Implement `POST /nbq/next` (deterministic algorithm)  
- Unit tests for NBQ scoring rules  
- Begin Phase B report draft (Backend & NBQ)  

## Risks

| Risk | Mitigation |
|------|------------|
| LM Studio offline during demo | Health still returns `api: online`; explain `lm_studio: offline` |
| G2 API feedback delayed | NBQ uses Week 2 contract; no breaking changes without notice |
| Scope creep into full chat | Chat explicitly Week 8 per roadmap |
