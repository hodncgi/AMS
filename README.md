# AMS — Group 3 AI Engine

**Current status: Week 3 — Backend skeleton & health check**  
**Authors:** Hugo Davion & Axel Brazeau — Group 3  
**Repository:** https://github.com/hodncgi/AMS

We are building the Group 3 algorithmic intelligence engine for AMS intake following the 11-week roadmap. Week 3 delivers the **first runnable FastAPI backend** with **`GET /health`**, LM Studio probe, CORS, and pytest.

## Week 3 deliverables (completed)

| Deliverable | Location |
|-------------|----------|
| FastAPI skeleton + `/health` | [backend/](backend/) |
| Run & test instructions | [docs/developer/SETUP.md](docs/developer/SETUP.md), [backend/README.md](backend/README.md) |
| Pytest suite | [tests/test_health.py](tests/test_health.py) |
| Manager Week 3 summary | [docs/management/WEEK3_PROGRESS_SUMMARY.md](docs/management/WEEK3_PROGRESS_SUMMARY.md) |

## Quick start

```powershell
pip install -r requirements.txt
uvicorn main:app --reload --app-dir backend
curl http://localhost:8000/health
```

OpenAPI UI: http://localhost:8000/docs

## Week 2 deliverables (completed)

| Deliverable | Location |
|-------------|----------|
| Architecture note + diagrams | [docs/developer/ARCHITECTURE.md](docs/developer/ARCHITECTURE.md), [ARCHITECTURE_DIAGRAM.md](docs/developer/ARCHITECTURE_DIAGRAM.md) |
| API contract + OpenAPI draft | [docs/developer/API.md](docs/developer/API.md), [openapi-draft.yaml](docs/developer/openapi-draft.yaml) |
| Figma template review + static preview | [docs/design/](docs/design/), [frontend/design-preview/](frontend/design-preview/) |
| User stories & roadmap PDFs | [deliverables/management/](deliverables/management/) |

## Week 4 next

`POST /nbq/next` — deterministic next-best-question algorithm.

## Documentation

[docs/README.md](docs/README.md)
