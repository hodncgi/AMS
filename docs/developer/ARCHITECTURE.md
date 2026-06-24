# Architecture — Group 3 AI Engine

**Document type:** Architecture note (Week 2 deliverable)  
**Status:** Week 3 — `/health` and minimal `/chat` live  
**Authors:** Hugo Davion & Axel Brazeau — Group 3

## 1. Purpose

Group 3 delivers an **algorithmic intelligence engine** for AMS intake:

- **Next-Best Question (NBQ)** — prioritize intake questions by client profile  
- **Change Risk** — score 0–100 with auditable drivers (decision support only)  
- **Onboarding chat** — answer CGI process questions with cited sources  

Group 2 owns the wider risk analysis site and will call G3 REST APIs.

## 2. High-level architecture

```mermaid
flowchart TB
    subgraph G2["Group 2 — Risk analysis site (future)"]
        Portal[AMS Portal UI]
    end

    subgraph API["G3 FastAPI — localhost:8000 (Week 3+)"]
        Health[GET /health]
        NBQ[POST /nbq/next<br/>deterministic]
        Risk[POST /change-risk<br/>deterministic]
        Chat[POST /chat<br/>RAG + Mistral]
    end

    subgraph Engine["Engine components"]
        ALG[algorithms.py<br/>NBQ + Change Risk]
        KB[knowledge_base<br/>+ catalog.json]
        LM[(LM Studio :1234<br/>Mistral 7B)]
    end

    subgraph UI["React UI — localhost:3000 (Week 8)"]
        Onb[Onboarding tab<br/>live chat]
        Demo[Dashboard · Docs · Manager<br/>static Figma demo]
    end

    Portal -->|HTTPS JSON| API
    Onb -->|POST /api/chat| Chat
    NBQ --> ALG
    Risk --> ALG
    Chat --> KB
    Chat --> LM
    KB --> Chat
    Demo -.->|no API v1| Demo
```

See also [ARCHITECTURE_DIAGRAM.md](ARCHITECTURE_DIAGRAM.md) for sequence and deployment views.

## 3. Design principles

| Principle | Rationale |
|-----------|-----------|
| **Deterministic algorithms** | NBQ and Change Risk are pure Python — reproducible for audit |
| **LLM for language only** | Mistral explains answers and NBQ `why` field; does not own scoring |
| **Local AI** | LM Studio on developer machine — no cloud API keys for POC |
| **RAG before generation** | Retrieve CGI knowledge chunks, inject into prompt, cite sources |
| **Fallback path** | If Mistral offline, return knowledge excerpts + clear message |
| **API-first** | Group 2 integrates via OpenAPI-documented JSON, not shared codebase |

## 4. Component responsibilities

### 4.1 FastAPI layer (`main.py` — Week 3+)

- HTTP routing, Pydantic validation, CORS for `localhost:3000`  
- Delegates algorithms to `algorithms.py`, chat to `ai_service.py`  
- OpenAPI at `/docs` for Group 2

### 4.2 Algorithms (`algorithms.py` — Week 5)

**NBQ** and **Change Risk** ship in the same week (compressed roadmap).

### 4.3 Knowledge & RAG (Week 7)

- Curated topics + `catalog.json` chunks (Week 6)  
- Keyword retrieval default; optional semantic embeddings (v2)  
- Future: relational database (Group 1) per US-15 / US-16

### 4.4 AI service (Week 3 minimal → Week 7 full)

- Week 3: direct Mistral call for `POST /chat`  
- Week 7: RAG injection, fallback, algorithm context

### 4.5 Onboarding UI (Week 4 HTML → Week 8 React)

- Week 4: simple HTML chat wired to API  
- Week 8: Figma → React on **Onboarding** tab only

## 5. Data flows

### NBQ request (Week 5+)

```mermaid
sequenceDiagram
    participant C as Client / G2
    participant API as POST /nbq/next
    participant ALG as select_next_best_question
    participant LS as LM Studio

    C->>API: profile { sector, solution }
    API->>ALG: compute weights
    ALG-->>API: best question + weight
    API->>LS: generate why (optional)
    LS-->>API: justification
    API-->>C: { id, text, weight, why }
```

### Change Risk request (Week 5+)

```mermaid
sequenceDiagram
    participant C as Client / G2
    participant API as POST /change-risk
    participant ALG as compute_change_risk

    C->>API: { criticality, test_days }
    API->>ALG: score + drivers
    ALG-->>API: { score, drivers[] }
    API-->>C: JSON response
```

### Chat request (Week 3 minimal → Week 7 RAG)

```mermaid
sequenceDiagram
    participant U as User
    participant API as POST /chat
    participant RAG as Knowledge base
    participant LS as LM Studio

    U->>API: messages[]
    API->>RAG: retrieve chunks
    RAG-->>API: context + sources
    API->>LS: prompt + context
    LS-->>API: JSON reply
    API-->>U: { reply, sources, mode }
```

## 6. Technology stack (decided Week 2)

| Layer | Choice |
|-------|--------|
| Backend | Python 3.10+, FastAPI, Pydantic, Uvicorn |
| Algorithms | Pure Python |
| Local LLM | LM Studio + Mistral 7B Instruct |
| RAG | Keyword search (default); semantic optional v2 |
| Frontend | React, TypeScript, Vite, Tailwind (Figma template) |
| Repository | GitHub — https://github.com/hodncgi/AMS |

See [AI.md](AI.md) for stack comparison and LM Studio setup.

## 7. Security & scope boundaries

- POC runs on localhost; production auth/TLS is Group 2 responsibility  
- Change risk is **decision support** — AMS leads retain sign-off  
- No merge into Group 2 site in v1 — REST integration only

## 8. Next steps (Week 4)

1. HTML chat page calling `POST /chat`  
2. Suggested starter questions (US-02)  
3. Basic AI mode indicator in UI  
4. Update design-preview or new `frontend/chat-live/` shell
