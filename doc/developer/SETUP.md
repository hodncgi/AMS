# Setup — Week 4 (backend + HTML chat + LM Studio)

Week 3 delivered the **FastAPI backend** (`/health`, `/chat`). Week 4 adds the **HTML chat UI** at `/ui/`. See [ROADMAP.md](ROADMAP.md).

---

## Prerequisites

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.10+ | FastAPI backend |
| LM Studio | Latest | Mistral for `/chat` |

---

## 1. LM Studio

1. Load **Mistral 7B Instruct** → **Developer** → **Start Server** on port **1234**.

```powershell
curl http://localhost:1234/v1/models
```

---

## 2. Backend + chat UI

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload --app-dir backend
```

Optional: copy `backend/.env.example` to `backend/.env`.

### Verify API

```powershell
curl http://localhost:8000/health

curl -X POST http://localhost:8000/chat ^
  -H "Content-Type: application/json" ^
  -d "{\"messages\":[{\"role\":\"user\",\"content\":\"What is AMS intake?\"}]}"
```

### Verify chat UI (Week 4)

Open **http://localhost:8000/ui/** in a browser. Try a suggested question or type your own.

API docs: http://localhost:8000/docs

### Tests

```powershell
pytest tests/ -v
```

---

## Upcoming

| Week | Task |
|------|------|
| 5 | NBQ + Change Risk |
| 6 | G2 API alignment |
| 7 | Knowledge base + RAG in chat |
| 8 | React UI — POC complete |
