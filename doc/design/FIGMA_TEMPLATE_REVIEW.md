# Figma template — review & integration plan (Week 2)

**Source:** Manager-provided Figma template (Technical Onboarding / Chatbot)  
**Authors:** Hugo Davion & Axel Brazeau — Group 3  
**Status:** Template received, analysed, static preview created

## 1. What we received

The manager provided a **Figma Make** export including:

- CGI branding (red `#e31937`, white header bar)  
- Four navigation areas: **Onboarding**, **My Onboarding**, **Documentation**, **Management**  
- shadcn/ui component library (MIT)  
- Layout structure suitable for React + Vite integration (planned **Week 8**)

## 2. Screen inventory

| Tab | Figma purpose | Week 2 decision | Backend link (planned) |
|-----|---------------|-----------------|------------------------|
| **Onboarding** | AI assistant for new employees | **Live chat target** (Week 4 HTML → Week 8 React) | `POST /chat`, `GET /health` |
| **My Onboarding** | Task checklist for new hires | Demo / static content in v1 | None in POC |
| **Documentation** | Document library browse | Demo / static content in v1 | Future Group 1 DB (US-15) |
| **Management** | Manager overview | Demo / role-gated view | Future analytics |

## 3. Week 2 work performed on the template

| Activity | Output |
|----------|--------|
| Template walkthrough with Group 3 | Tab map + scope decisions (this document) |
| Map UI areas to G3 API routes | [UI_TO_API_MAPPING.md](UI_TO_API_MAPPING.md) |
| Validate CGI branding against intake guidelines | Approved — no changes required |
| Build **static HTML design preview** | [../../frontend/design-preview/index.html](../../frontend/design-preview/index.html) |
| Define Onboarding-only live scope | Aligns with US-12 and product scope |

## 4. Static preview (Week 2 deliverable)

We created a **standalone HTML preview** from the Figma structure:

- Open `frontend/design-preview/index.html` in a browser (no build step)  
- Shows header, tabs, and placeholder panels  
- Labelled as design preview — **API wiring in Week 4 (HTML) and Week 8 (React)**

This proves template ingestion and layout understanding **without** claiming a finished chatbot in Week 2.

## 5. UI integration plan (aligned with [ROADMAP.md](../developer/ROADMAP.md))

| Step | Week |
|------|------|
| HTML chat page calling `POST /chat` | 4 |
| Suggested starter questions (US-02) | 4 |
| `npm create vite` + TypeScript in `frontend/chatbot-onboarding/` | 8 |
| Import Figma/shadcn components | 8 |
| Vite proxy `/api` → `localhost:8000` | 8 |
| Wire **Onboarding** tab only to `POST /chat` | 8 |
| AiPipelineBar for answer mode (US-07) | 8 |
| Source list under answers (US-13) — after RAG in Week 7 | 8 |

## 6. Risks & mitigations

| Risk | Mitigation |
|------|------------|
| Manager expects all tabs live | Documented: only Onboarding is API-backed in v1 |
| Figma vs React drift | Use same tab IDs as preview; single source in Week 8 |
| Heavy bundle from shadcn | Tree-shake; import only used components |

## 7. Sign-off requested

Please confirm:

1. Onboarding tab = sole live AI entry point  
2. Other tabs acceptable as demo/static for POC  
3. Figma template is the reference for Week 8 UI
