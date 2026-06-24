# Architecture diagrams

Visual reference for manager and Group 2 presentations. Implementation follows [ROADMAP.md](ROADMAP.md) from Week 3 onward.

## System context

```mermaid
flowchart TB
    subgraph G2["Group 2 — Risk analysis site (future)"]
        Portal[AMS Portal UI]
    end

    subgraph G3["Group 3 — FastAPI engine (Week 3+)"]
        API[FastAPI :8000]
        ALG[NBQ + Change Risk]
        RAG[Knowledge retrieval]
        AI[ai_service → LM Studio]
    end

    subgraph UI["Onboarding UI — Figma template (Week 9)"]
        Onb[Onboarding tab]
        Demo[Demo tabs]
    end

    LM[(LM Studio :1234\nMistral 7B)]

    Portal -->|REST JSON| API
    Onb -->|POST /chat| API
    API --> ALG
    API --> RAG
    API --> AI
    AI --> LM
    Demo -.->|static Week 9| Demo
```

## Chat request flow (Week 8+)

```mermaid
sequenceDiagram
    participant U as New employee
    participant UI as Onboarding tab
    participant API as POST /chat
    participant RAG as Knowledge base
    participant LS as LM Studio

    U->>UI: Ask question
    UI->>API: messages[]
    API->>RAG: retrieve chunks
    RAG-->>API: context + sources
    API->>LS: prompt + context
    LS-->>API: JSON reply
    API-->>UI: reply, sources, mode
    UI-->>U: Answer + citations
```

## Deployment view (developer POC)

```mermaid
flowchart LR
    Browser[Browser :3000]
    Vite[Vite dev server]
    FastAPI[Uvicorn :8000]
    LM[LM Studio :1234]

    Browser --> Vite
    Vite -->|proxy /api| FastAPI
    FastAPI --> LM
```

## Phase timeline (aligned with roadmap)

| Weeks | Layer |
|-------|--------|
| 1–2 | Design, API contract, Figma, LM Studio — **done** |
| 3–4 | FastAPI, `/health`, minimal `/chat`, HTML chat UI |
| 5 | NBQ + Change Risk |
| 6 | G2 API route alignment |
| 7 | Knowledge base + RAG + chat quality |
| 8 | React Onboarding tab — **POC complete** |
| 9–11 | Stabilization, G2 live integration, final delivery |

See [ARCHITECTURE.md](ARCHITECTURE.md) for narrative detail.
