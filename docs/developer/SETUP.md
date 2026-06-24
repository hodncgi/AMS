# Setup — Week 2 (LM Studio readiness)

At the end of Week 2, we have **LM Studio installed and Mistral ready** on the development machine. Backend and frontend setup will be added from **Week 3** onward.

See [ROADMAP.md](ROADMAP.md) for the full 11-week plan.

---

## Prerequisites (Week 2)

| Tool | Version | Purpose |
|------|---------|---------|
| LM Studio | Latest | Local Mistral inference |
| Mistral 7B Instruct | GGUF | Recommended chat model |

Python 3.10+ and Node.js 18+ will be required from Weeks **3** and **8** respectively.

---

## LM Studio installation

1. Download [LM Studio](https://lmstudio.ai/) and open the desktop app.  
2. Left sidebar → **My Models** → download **Mistral 7B Instruct v0.3** via **Discover** if not present.  
3. Click the model to **load** it into memory.  
4. Open **Developer** → click **Start Server** (top-left) on port **1234**.

## Verify (Week 2 done criteria)

```powershell
curl http://localhost:1234/v1/models
```

You should see a JSON list including the Mistral model id (e.g. `mistral`).

---

## Roadmap — upcoming setup steps

| Week | Task |
|------|------|
| **3** | `pip install fastapi uvicorn` — backend on port 8000, `/health` + minimal `/chat` |
| **4** | HTML chat page wired to API |
| **5** | Algorithm endpoints |
| **6** | G2 API route alignment |
| **7** | Knowledge base in `backend/data/` |
| **8** | `npm install` — React onboarding UI on port 3000 |

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full plan.
