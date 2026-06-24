# Week 2 — Progress summary (manager)

**Project:** Group 3 AMS Algorithmic Intelligence Engine  
**Week:** 2 of 11 — Architecture & API design (**complete**)  
**Team:** Hugo Davion & Axel Brazeau  
**Repository:** https://github.com/hodncgi/AMS

## Executive summary

Week 2 focused on **technical design and stakeholder alignment**. We analysed the **Figma template**, defined the **system architecture**, drafted the **REST API contract** for Group 2, selected **LM Studio + Mistral**, and documented the **chatbot knowledge scope**. A **static UI preview** demonstrates template ingestion.

The agreed roadmap compresses core delivery into **Weeks 1–8** (chat-first from Week 3) with **Weeks 9–11** for manager feedback and G2 integration. **Week 3** starts the runnable backend.

## Completed deliverables

| # | Deliverable | Evidence in repo |
|---|-------------|------------------|
| 1 | Architecture note | `docs/developer/ARCHITECTURE.md` |
| 2 | Architecture diagrams | `docs/developer/ARCHITECTURE_DIAGRAM.md` |
| 3 | API contract draft + OpenAPI | `docs/developer/API.md`, `openapi-draft.yaml` |
| 4 | 11-week roadmap (8+3) | `docs/developer/ROADMAP.md`, `deliverables/management/G3_11_Week_Roadmap.pdf` |
| 5 | G2 workshop notes | `docs/management/G2_API_WORKSHOP_NOTES.md` |
| 6 | Stack decision | `docs/developer/STACK_DECISION.md` |
| 7 | LM Studio ready | `docs/developer/SETUP.md` |
| 8 | Chatbot knowledge scope | `docs/developer/KNOWLEDGE_SCOPE.md` |
| 9 | Figma template review | `docs/design/FIGMA_TEMPLATE_REVIEW.md` |
| 10 | Static design preview | `frontend/design-preview/index.html` |
| 11 | User stories PDF | `deliverables/management/G3_User_Stories.pdf` |

## What to demo in a 20-minute review

1. Walk through **ARCHITECTURE_DIAGRAM.md**  
2. Open **design-preview/index.html** — CGI shell from Figma  
3. Show **openapi-draft.yaml** in Swagger Editor  
4. Run `curl http://localhost:1234/v1/models` — LM Studio ready  
5. Present **ROADMAP.md** — chat-first plan, G2 handover Week 6  

## Week 3 commitment

- FastAPI project in `backend/`  
- `GET /health` + minimal `POST /chat` (Mistral direct)  
- CORS, pytest, run instructions  

## Risks

| Risk | Mitigation |
|------|------------|
| G2 not yet in contact | Week 6 milestone flexible; stabilization weeks 9–11 absorb delay |
| Manager expects live chat now | Explain Week 3–4 chat-first plan |
| LM Studio blocked on some laptops | Fallback strategy documented in AI.md |
