# Week 2 — Progress summary (manager)

**Project:** Group 3 AMS Algorithmic Intelligence Engine  
**Week:** 2 of 11 — Architecture & API design  
**Team:** Hugo Davion & Axel Brazeau  
**Repository:** https://github.com/hodncgi/AMS

## Executive summary

Week 2 focused on **technical design and stakeholder alignment**. We analysed the **Figma template** provided by management, defined the **system architecture**, drafted the **REST API contract** for Group 2, selected **LM Studio + Mistral** as the local AI stack, and documented the **chatbot knowledge scope**. A **static UI preview** demonstrates template ingestion; backend and live chat follow the agreed roadmap from Week 3 onward.

## Completed deliverables

| # | Deliverable | Evidence in repo |
|---|-------------|------------------|
| 1 | Architecture note | `docs/developer/ARCHITECTURE.md` |
| 2 | Architecture diagrams | `docs/developer/ARCHITECTURE_DIAGRAM.md` |
| 3 | API contract draft + OpenAPI | `docs/developer/API.md`, `openapi-draft.yaml` |
| 4 | G2 workshop notes | `docs/management/G2_API_WORKSHOP_NOTES.md` |
| 5 | Stack decision (LM Studio vs Ollama) | `docs/developer/STACK_DECISION.md` |
| 6 | LM Studio ready | `docs/developer/SETUP.md` |
| 7 | Chatbot knowledge scope | `docs/developer/KNOWLEDGE_SCOPE.md` |
| 8 | Figma template review | `docs/design/FIGMA_TEMPLATE_REVIEW.md` |
| 9 | UI → API mapping | `docs/design/UI_TO_API_MAPPING.md` |
| 10 | Static design preview | `frontend/design-preview/index.html` |
| 11 | User stories & roadmap | `deliverables/management/*.pdf` |
| 12 | Phase A manager report | `docs/management/progress/01_*.pdf` |

## Figma template — what we did

Management provided the onboarding UI template. This week we:

- Inventoried all tabs and agreed **Onboarding** is the only live AI surface in v1  
- Produced a **browser-openable HTML preview** (no build tools required)  
- Mapped each screen to future API calls for Group 2 visibility  

## What to demo in a 20-minute review

1. Walk through **ARCHITECTURE_DIAGRAM.md** (context + sequence)  
2. Open **design-preview/index.html** — show CGI shell from Figma  
3. Show **openapi-draft.yaml** in Swagger Editor (paste file) — professional API artifact  
4. Run `curl http://localhost:1234/v1/models` — LM Studio ready  
5. Highlight **G2_API_WORKSHOP_NOTES.md** — open questions for Group 2  

## Week 3 commitment

- FastAPI project in `backend/`  
- `GET /health` operational on port 8000  
- Initial pytest + README run instructions  

## Risks

| Risk | Mitigation |
|------|------------|
| G2 API feedback delayed | Proceed with Week 3–5; contract marked draft |
| Manager expects full UI now | Static preview + explicit Week 9 plan |
| LM Studio blocked on some laptops | Documented fallback strategy in AI.md |
