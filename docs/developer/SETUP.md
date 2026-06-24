# Setup — Week 3 (backend + LM Studio)

Week 3 adds the **FastAPI backend** on port 8000. LM Studio (Week 2) remains required for full `/health` AI status.

---

## Prerequisites

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.10+ | FastAPI backend |
| LM Studio | Latest | Local Mistral inference |
| Mistral 7B Instruct | GGUF | Recommended chat model |

Node.js 18+ will be required from Week 9 (React UI).

---

## 1. LM Studio (from Week 2)

1. Download [LM Studio](https://lmstudio.ai/) and open the desktop app.  
2. Load **Mistral 7B Instruct v0.3** into memory.  
3. **Developer** → **Start Server** on port **1234**.

```powershell
curl http://localhost:1234/v1/models
```

---

## 2. Backend (Week 3)

From the repository root:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload --app-dir backend
```

Optional: copy `backend/.env.example` to `backend/.env` to override LM Studio URL or model id.

### Verify

```powershell
curl http://localhost:8000/health
```

Expected shape:

```json
{
  "api": "online",
  "ai": {
    "lm_studio": { "status": "online", "model": "mistral" },
    "rag": { "enabled": false, "method": "keyword", "chunks_indexed": 0 }
  },
  "fallback_enabled": true
}
```

Interactive docs: http://localhost:8000/docs

### Tests

```powershell
pytest tests/ -v
```

---

## Roadmap — upcoming setup steps

| Week | Task |
|------|------|
| 4–5 | `POST /nbq/next`, `POST /change-risk` |
| 6–7 | Knowledge base files in `backend/data/` |
| 8 | Connect `/chat` to LM Studio + RAG |
| 9 | `npm install` — React onboarding UI on port 3000 |

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full plan.
