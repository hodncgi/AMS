# Architecture diagrams (Week 2)

Visual reference for manager and Group 2 presentations. Implementation follows in Weeks 3–9.

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
| 1–2 | Design, API contract, Figma analysis, LM Studio |
| 3 | FastAPI + `/health` |
| 4–5 | NBQ + Change Risk |
| 6–7 | Knowledge base + RAG |
| 8 | `/chat` |
| 9 | Figma → React Onboarding tab |

See [ARCHITECTURE.md](ARCHITECTURE.md) for narrative detail.
