# Backend — Week 2 (structure planned)

Backend implementation starts **Week 3** in this repository.

## Planned layout

```mermaid
flowchart TB
    ROOT[backend/] --> MAIN[main.py — FastAPI routes]
    ROOT --> CFG[config.py]
    ROOT --> ALG[algorithms.py]
    ROOT --> AI[ai_service.py]
    ROOT --> RAG[rag_service.py]
    ROOT --> KB[knowledge_base.py]
    ROOT --> DATA[data/documents/]
    DATA --> CAT[catalog.json]
```

## API contract

See [../docs/developer/API.md](../docs/developer/API.md) — draft under Group 2 review.

## Architecture

See [../docs/developer/ARCHITECTURE.md](../docs/developer/ARCHITECTURE.md).
