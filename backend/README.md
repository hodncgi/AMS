# Backend — Week 4 in progress (FastAPI + health + chat + HTML UI)

FastAPI backend on port **8000** with **`GET /health`**, **`POST /chat`** (Mistral direct, no RAG), and **HTML chat UI** at **`/ui/`**.

## Quick start

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload --app-dir backend
```

Verify:

```powershell
curl http://localhost:8000/health
```

- OpenAPI: http://localhost:8000/docs  
- Chat UI: http://localhost:8000/ui/

## Tests

```powershell
pytest tests/ -v
```

## Layout

```mermaid
flowchart TB
    ROOT[backend/] --> MAIN[main.py — API + /ui mount]
    ROOT --> CFG[config.py]
    ROOT --> AI[ai_service.py — health + chat]
    UI[frontend/chat-live/] --> MAIN
    ROOT --> ALG[algorithms.py — Week 5]
    ROOT --> KB[knowledge_base.py — Week 7]
```

See [../doc/developer/SETUP.md](../doc/developer/SETUP.md).
