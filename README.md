# AMS — Group 3 AI Engine

**Current status: Week 3 in progress** (Week 2 complete)  
**Authors:** Hugo Davion & Axel Brazeau — Group 3  
**Repository:** https://github.com/AMSNextGen25-26/chatbot-AMS

Group 3 algorithmic intelligence engine for AMS intake — **11-week roadmap** (8 core + 3 stabilization). **Week 2** (architecture & API design) is complete. **Week 3** focuses on the first runnable backend: `GET /health` and minimal `POST /chat` (Mistral direct).

**All project documentation is in [`doc/`](doc/).**

## Week 2 deliverables (complete)

| Deliverable | Location |
|-------------|----------|
| Architecture & API draft | [doc/developer/ARCHITECTURE.md](doc/developer/ARCHITECTURE.md), [doc/developer/API.md](doc/developer/API.md) |
| Figma / design preview | [doc/design/](doc/design/), [frontend/design-preview/](frontend/design-preview/) |
| Manager summary | [doc/management/WEEK2_PROGRESS_SUMMARY.md](doc/management/WEEK2_PROGRESS_SUMMARY.md) |

## Week 3 focus (in progress)

| Work in progress | Location |
|------------------|----------|
| FastAPI + `/health` + `/chat` | [backend/](backend/) |
| Setup & tests | [doc/developer/SETUP.md](doc/developer/SETUP.md), [tests/test_week3.py](tests/test_week3.py) |
| Progress summary | [doc/management/WEEK3_PROGRESS_SUMMARY.md](doc/management/WEEK3_PROGRESS_SUMMARY.md) |

## Quick start

```powershell
pip install -r requirements.txt
uvicorn main:app --reload --app-dir backend
curl http://localhost:8000/health
```

API docs: http://localhost:8000/docs

## Week 3 still to close

- Manager review of Week 3 scope  
- HTML chat UI moves to **Week 4**

## Documentation

**[doc/README.md](doc/README.md)** · [doc/developer/ROADMAP.md](doc/developer/ROADMAP.md)

```
AMS/
├── README.md
├── doc/                        # ← all documentation (manager + developer)
│   ├── developer/
│   ├── design/
│   ├── management/
│   └── deliverables/
├── backend/
├── frontend/
└── tests/
```
