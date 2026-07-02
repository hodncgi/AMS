# Live HTML chat (Week 4)

Browser chat page wired to **`POST /chat`** on the FastAPI backend.

## Run

Start the backend, then open:

**http://localhost:8000/ui/**

```powershell
uvicorn main:app --reload --app-dir backend
```

## Features (Week 4 — in progress)

- Message history sent to `/chat`
- Four suggested starter questions (US-02)
- API health badge (`GET /health`)
- Mode badge in replies (`mistral` / `fallback`)
- Slow-response hint and request guard while waiting for Mistral

Sources and RAG display ship in **Week 7**; React UI in **Week 8**.
