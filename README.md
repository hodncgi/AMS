# AMS — Group 3 AI Engine

**Current status: Week 2 — Architecture & API design**  
**Authors:** Hugo Davion & Axel Brazeau — Group 3  
**Repository:** https://github.com/hodncgi/AMS

We are building the Group 3 algorithmic intelligence engine for AMS intake following the 11-week roadmap. At the end of Week 2, design and planning deliverables are complete; backend and UI implementation begin in Week 3.

## Week 2 deliverables (completed)

| Deliverable | Location | Status |
|-------------|----------|--------|
| Architecture note | [docs/developer/ARCHITECTURE.md](docs/developer/ARCHITECTURE.md) | Done |
| API contract draft (Group 2) | [docs/developer/API.md](docs/developer/API.md) | Draft |
| LM Studio + Mistral stack decision | [docs/developer/AI.md](docs/developer/AI.md) | Done |
| LM Studio installation guide | [docs/developer/SETUP.md](docs/developer/SETUP.md) | Done |
| User stories (planning) | [deliverables/management/G3_User_Stories.pdf](deliverables/management/G3_User_Stories.pdf) | Draft v0.1 |
| 11-week roadmap | [deliverables/management/G3_11_Week_Roadmap.pdf](deliverables/management/G3_11_Week_Roadmap.pdf) | Done |
| Manager report — Phase A | [docs/management/progress/01_Phase_A_Scoping_Design.pdf](docs/management/progress/01_Phase_A_Scoping_Design.pdf) | Done |

## Week 2 focus — user stories

- **US-08** — Documented REST APIs for Group 2 integration  
- **US-12** — Single assistant scope (onboarding + risk topics) — designed, implementation Week 8–9

## Upcoming (Week 3+)

| Milestone | Roadmap week |
|-----------|----------------|
| FastAPI backend + `/health` | Week 3 |
| NBQ algorithm + `/nbq/next` | Week 4 |
| Change Risk + `/change-risk` | Week 5 |
| Knowledge base + RAG | Weeks 6–7 |
| Chat API + Mistral integration | Week 8 |
| React onboarding chatbot | Week 9 |

See [backend/README.md](backend/README.md) and [frontend/README.md](frontend/README.md) for the planned folder layout.

## Documentation

Start here: [docs/README.md](docs/README.md)

## Product scope

- Standalone G3 engine; Group 2 integrates via REST when their site APIs are ready  
- Live chatbot on the **Onboarding** tab only (UI planned Week 9)  
- Change risk = decision support; AMS leads retain final sign-off
