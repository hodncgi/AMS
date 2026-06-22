# AMS — Group 3 AI Engine

**Current status: Week 2 — Architecture & API design**  
**Authors:** Hugo Davion & Axel Brazeau — Group 3  
**Repository:** https://github.com/hodncgi/AMS

We are building the Group 3 algorithmic intelligence engine for AMS intake following the 11-week roadmap. Week 2 delivers **design, architecture, API contracts, Figma template analysis**, and a **static UI preview** — backend code starts Week 3.

## Week 2 deliverables (completed)

| Deliverable | Location |
|-------------|----------|
| Architecture note + diagrams | [docs/developer/ARCHITECTURE.md](docs/developer/ARCHITECTURE.md), [ARCHITECTURE_DIAGRAM.md](docs/developer/ARCHITECTURE_DIAGRAM.md) |
| API contract + OpenAPI draft | [docs/developer/API.md](docs/developer/API.md), [openapi-draft.yaml](docs/developer/openapi-draft.yaml) |
| G2 workshop notes | [docs/management/G2_API_WORKSHOP_NOTES.md](docs/management/G2_API_WORKSHOP_NOTES.md) |
| Stack decision (LM Studio vs Ollama) | [docs/developer/STACK_DECISION.md](docs/developer/STACK_DECISION.md) |
| Chatbot knowledge scope | [docs/developer/KNOWLEDGE_SCOPE.md](docs/developer/KNOWLEDGE_SCOPE.md) |
| LM Studio setup | [docs/developer/SETUP.md](docs/developer/SETUP.md) |
| **Figma template review** | [docs/design/FIGMA_TEMPLATE_REVIEW.md](docs/design/FIGMA_TEMPLATE_REVIEW.md) |
| **UI → API mapping** | [docs/design/UI_TO_API_MAPPING.md](docs/design/UI_TO_API_MAPPING.md) |
| **Static design preview** | [frontend/design-preview/index.html](frontend/design-preview/index.html) |
| Manager Week 2 summary | [docs/management/WEEK2_PROGRESS_SUMMARY.md](docs/management/WEEK2_PROGRESS_SUMMARY.md) |
| User stories & roadmap PDFs | [deliverables/management/](deliverables/management/) |
| Phase A report | [docs/management/progress/01_Phase_A_Scoping_Design.pdf](docs/management/progress/01_Phase_A_Scoping_Design.pdf) |

## Quick demo for management (5 min)

1. Open **`frontend/design-preview/index.html`** — Figma shell with tabs  
2. Show **`docs/developer/ARCHITECTURE_DIAGRAM.md`** — system diagrams  
3. Paste **`docs/developer/openapi-draft.yaml`** into [Swagger Editor](https://editor.swagger.io/)  
4. Optional: `curl http://localhost:1234/v1/models` — LM Studio ready  

Full walkthrough: [docs/management/WEEK2_PROGRESS_SUMMARY.md](docs/management/WEEK2_PROGRESS_SUMMARY.md)

## Week 3 next

FastAPI + `GET /health` on port 8000.

## Documentation

[docs/README.md](docs/README.md)
