# Setup — Week 3 (backend + LM Studio)

Week 3 adds the **FastAPI backend** on port 8000 with `/health` and minimal `/chat`. See [ROADMAP.md](ROADMAP.md).

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

## 2. Backend

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload --app-dir backend
```

Optional: copy `backend/.env.example` to `backend/.env`.

### Verify

```powershell
curl http://localhost:8000/health

curl -X POST http://localhost:8000/chat ^
  -H "Content-Type: application/json" ^
  -d "{\"messages\":[{\"role\":\"user\",\"content\":\"What is AMS intake?\"}]}"
```

Docs: http://localhost:8000/docs

### Tests

```powershell
pytest tests/ -v
```

---

## Upcoming

| Week | Task |
|------|------|
| 4 | HTML chat UI |
| 5 | NBQ + Change Risk |
| 6 | G2 API alignment |
| 7 | Knowledge base + RAG in chat |
| 8 | React UI — POC complete |
