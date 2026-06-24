# AMS — Group 3 AI Engine

**Current status: Week 2 complete — ready for Week 3**  
**Authors:** Hugo Davion & Axel Brazeau — Group 3  
**Repository:** https://github.com/hodncgi/AMS

We are building the Group 3 algorithmic intelligence engine for AMS intake following the **11-week roadmap** (8 weeks core + 3 weeks stabilization). Week 2 delivered **design, architecture, API contracts, Figma analysis**, and a **static UI preview**. **Week 3** starts the FastAPI backend with **`GET /health`** and **minimal `POST /chat`**.

## Week 2 deliverables (completed)

| Deliverable | Location |
|-------------|----------|
| Architecture note + diagrams | [docs/developer/ARCHITECTURE.md](docs/developer/ARCHITECTURE.md), [ARCHITECTURE_DIAGRAM.md](docs/developer/ARCHITECTURE_DIAGRAM.md) |
| API contract + OpenAPI draft | [docs/developer/API.md](docs/developer/API.md), [openapi-draft.yaml](docs/developer/openapi-draft.yaml) |
| Roadmap (8+3) | [docs/developer/ROADMAP.md](docs/developer/ROADMAP.md) |
| G2 workshop notes | [docs/management/G2_API_WORKSHOP_NOTES.md](docs/management/G2_API_WORKSHOP_NOTES.md) |
| Figma template + static preview | [docs/design/](docs/design/), [frontend/design-preview/](frontend/design-preview/) |
| Manager Week 2 summary | [docs/management/WEEK2_PROGRESS_SUMMARY.md](docs/management/WEEK2_PROGRESS_SUMMARY.md) |
| User stories & roadmap PDFs | [deliverables/management/](deliverables/management/) |

## Quick demo (Week 2)

1. Open **`frontend/design-preview/index.html`** — Figma shell with tabs  
2. Show **`docs/developer/ARCHITECTURE_DIAGRAM.md`**  
3. Paste **`docs/developer/openapi-draft.yaml`** into [Swagger Editor](https://editor.swagger.io/)  
4. Optional: `curl http://localhost:1234/v1/models` — LM Studio ready  

## Week 3 next

FastAPI + `GET /health` + minimal `POST /chat` (Mistral direct, no RAG).

## Documentation

[docs/README.md](docs/README.md)
