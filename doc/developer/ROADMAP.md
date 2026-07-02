# Eleven-week roadmap — Group 3 AMS Engine

Aligned with `doc/deliverables/G3_11_Week_Roadmap.pdf`.

**Current position:** **Week 3 complete** · **Week 4 in progress** — HTML chat UI + suggested questions; **Week 5** = NBQ + Change Risk.

## Structure: 8 + 3

| Block | Weeks | Purpose |
|-------|-------|---------|
| **Core delivery** | 1–8 | POC feature-complete at end of Week 8 |
| **Stabilization** | 9–11 | Manager feedback, G2 integration, adaptations |

## Delivery principles

1. **Chat first** — usable assistant from Weeks 3–4 (before algorithms).
2. **Compressed algorithms** — NBQ + Change Risk in Week 5.
3. **G2 handover** — Week 6: receive API routes (collaborating team not yet in contact).
4. **Buffer weeks** — 9–11 for critiques and cross-project alignment.

## Week-by-week plan

| Week | Theme | Key deliverables |
|------|-------|------------------|
| **1** | Project launch | User stories, personas |
| **2** | Architecture & API design | **Complete** |
| **3** | Backend + minimal chat | **Complete** — `/health`, `/chat` |
| **4** | Usable chat UI | **In progress** — HTML chat page, suggested questions |
| **5** | NBQ + Change Risk | Both algorithm endpoints |
| **6** | G2 API alignment | Route mapping when G2 connects |
| **7** | Knowledge, RAG & chat quality | Sources, fallback |
| **8** | React UI — **POC complete** | Port 3000, `/g3-test`, pytest |
| **9–11** | Stabilization | Feedback, G2 live tests, final delivery |

## API routes by week

| Route | Week |
|-------|------|
| `GET /health` | 3 |
| `POST /chat` | 3 (minimal) → 7 (RAG) |
| `POST /nbq/next` | 5 |
| `POST /change-risk` | 5 |
| G2 routes intake | 6 |
| `GET /g3-test` | 8 |

See [G2_INTEGRATION.md](G2_INTEGRATION.md) for Group 2 timeline.
