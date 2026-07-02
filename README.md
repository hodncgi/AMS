# AMS — Group 3 AI Engine

**Current status: Week 4 in progress** (Week 3 complete)  
**Authors:** Hugo Davion & Axel Brazeau — Group 3  
**Repository:** https://github.com/AMSNextGen25-26/chatbot-AMS

Group 3 algorithmic intelligence engine for AMS intake — **11-week roadmap** (8 core + 3 stabilization). **Week 3** delivered the runnable backend (`GET /health`, `POST /chat`). **Week 4** adds the **HTML chat UI** with suggested starter questions.

**All project documentation is in [`doc/`](doc/).**

## Week 3 deliverables (complete)

| Deliverable | Location |
|-------------|----------|
| FastAPI + `/health` + `/chat` | [backend/](backend/) |
| Setup & tests | [doc/developer/SETUP.md](doc/developer/SETUP.md), [tests/test_week3.py](tests/test_week3.py) |
| Manager summary | [doc/management/WEEK3_PROGRESS_SUMMARY.md](doc/management/WEEK3_PROGRESS_SUMMARY.md) |

## Week 4 focus (in progress)

| Work in progress | Location |
|------------------|----------|
| HTML chat page wired to `POST /chat` | [frontend/chat-live/](frontend/chat-live/) |
| Suggested starter questions (US-02) | `frontend/chat-live/index.html` |
| Progress summary | [doc/management/WEEK4_PROGRESS_SUMMARY.md](doc/management/WEEK4_PROGRESS_SUMMARY.md) |

## Quick start

```powershell
pip install -r requirements.txt
uvicorn main:app --reload --app-dir backend
```

- API docs: http://localhost:8000/docs  
- **Live chat UI:** http://localhost:8000/ui/

```powershell
curl http://localhost:8000/health
pytest tests/ -v
```

## Week 4 still to close

- End-to-end browser demo with LM Studio  
- Manager review of Week 4 scope  

## Documentation

**[doc/README.md](doc/README.md)** · [doc/developer/ROADMAP.md](doc/developer/ROADMAP.md)

```
AMS/
├── README.md
├── doc/
├── backend/
├── frontend/
│   ├── design-preview/     # Week 2 static mock
│   └── chat-live/          # Week 4 live HTML chat
└── tests/
```
