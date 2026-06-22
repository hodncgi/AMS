# Backend — Week 2 (structure planned)

Backend implementation starts **Week 3** in this repository.

## Planned layout

```
backend/
├── main.py              # FastAPI app — routes /health, /nbq/next, /change-risk, /chat
├── config.py            # LM Studio, RAG, timeout settings
├── algorithms.py        # NBQ + Change Risk (deterministic)
├── ai_service.py        # Mistral + prompts + fallback
├── rag_service.py       # Knowledge retrieval
├── knowledge_base.py    # CGI topics + catalog chunks
└── data/documents/
    └── catalog.json     # Document chunks for RAG
```

## API contract

See [../docs/developer/API.md](../docs/developer/API.md) — draft under Group 2 review.

## Architecture

See [../docs/developer/ARCHITECTURE.md](../docs/developer/ARCHITECTURE.md).
