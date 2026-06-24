# AMS — Group 3 AI Engine

**Current status: Week 3 — Backend & minimal chat**  
**Authors:** Hugo Davion & Axel Brazeau — Group 3  
**Repository:** https://github.com/hodncgi/AMS

Group 3 algorithmic intelligence engine for AMS intake — **11-week roadmap** (8 core + 3 stabilization). Week 3 delivers the **first runnable API**: `GET /health` and minimal `POST /chat` (Mistral direct).

> The full POC lives in [AMSChatBot](https://github.com/hodncgi/AMSChatBot). **All documentation for this repo is in `doc/`.**

## Week 3 deliverables (completed)

| Deliverable | Location |
|-------------|----------|
| FastAPI + `/health` + `/chat` | [backend/](backend/) |
| Setup & tests | [doc/developer/SETUP.md](doc/developer/SETUP.md), [tests/test_week3.py](tests/test_week3.py) |
| Manager summary | [doc/management/WEEK3_PROGRESS_SUMMARY.md](doc/management/WEEK3_PROGRESS_SUMMARY.md) |

## Quick start

```powershell
pip install -r requirements.txt
uvicorn main:app --reload --app-dir backend
curl http://localhost:8000/health
```

API docs: http://localhost:8000/docs

## Week 4 next

HTML chat UI connected to `POST /chat`.

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
