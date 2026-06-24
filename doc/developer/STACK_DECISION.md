# Technology stack decision record (Week 2)

**Workshop date:** Week 2 — Group 3 internal review  
**Decision owners:** Hugo Davion & Axel Brazeau  
**Status:** Approved

## Context

Group 3 needs local AI for onboarding chat and NBQ `why` justifications without cloud API keys or corporate data leaving the machine during the POC.

## Options evaluated

| Criterion | LM Studio + Mistral 7B | Ollama + Mistral | Rules-only (no LLM) |
|-----------|------------------------|------------------|---------------------|
| Desktop UI for demos | Excellent | CLI-focused | N/A |
| OpenAI-compatible API | Yes (`:1234/v1`) | Yes | N/A |
| Model quality (7B) | Strong instruct model | Same models | N/A |
| Manager visibility | Easy (load model, Start Server) | Harder | Easy but poor chat |
| Offline fallback story | RAG excerpts + clear message | Same | Only option |
| Corporate laptop constraints | CPU slow but acceptable | Similar | Fast |
| **Decision** | **Selected** | Backup option | Fallback layer only |

## Selected stack

| Layer | Technology | Rationale |
|-------|------------|-----------|
| Runtime | LM Studio | Best demo UX; manager can verify server status |
| Model | Mistral 7B Instruct v0.3 (GGUF) | Balance quality / size for local CPU |
| Retrieval | Keyword RAG (default) | No Hugging Face download blocker on corporate network |
| Semantic RAG | Deferred to v2 | Optional when network allows |
| Backend (from Week 3) | FastAPI + Pydantic | OpenAPI for Group 2; team Python skills |
| Frontend (from Week 8) | React + Vite + Figma template | Manager-provided UI assets |

## Proof of readiness (Week 2)

```powershell
curl http://localhost:1234/v1/models
```

Expected: HTTP 200, Mistral model id in JSON response.

## Revisit triggers

- Corporate policy blocks local models → escalate to referent  
- Inference &gt; 5 min on target laptops → tune `LM_STUDIO_TIMEOUT` or quantize model  
- Group 2 requires cloud-hosted LLM → out of scope v1

## Related documents

- [AI.md](AI.md) — configuration plan  
- [SETUP.md](SETUP.md) — installation steps  
- [ARCHITECTURE.md](ARCHITECTURE.md) — system design
