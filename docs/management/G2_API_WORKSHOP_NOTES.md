# Group 2 — API alignment workshop notes (Week 2)

**Session:** G3 ↔ G2 API contract review (draft)  
**Participants:** Hugo Davion, Axel Brazeau (Group 3) — Group 2 referent TBC  
**Status:** Draft circulated for async review

## Objectives

1. Agree JSON shapes for NBQ, Change Risk, and Chat  
2. Confirm Group 3 does **not** own final risk sign-off  
3. Identify CORS / auth requirements for future integration

## Endpoints presented

| Route | Purpose | G2 use case |
|-------|---------|-------------|
| `GET /health` | Liveness + AI status | Monitoring |
| `POST /nbq/next` | Next intake question | Intake wizard |
| `POST /change-risk` | Risk score + drivers | Risk dashboard |
| `POST /chat` | Onboarding Q&A | Onboarding tab (G3 UI or embedded) |

Full contract: [../developer/API.md](../developer/API.md) and [../developer/openapi-draft.yaml](../developer/openapi-draft.yaml).

## Decisions recorded

| Topic | Decision |
|-------|----------|
| Change risk output | `score` (0–100) + `drivers[]` for audit |
| NBQ output | `id`, `text`, `weight`, `why` |
| Chat history | Array of `{ role, content }` — OpenAI-style |
| Versioning | Breaking changes → new API version + 90-day notice |
| Sign-off | AMS leads retain final change approval |

## Open questions for Group 2

- [ ] Production base URL and authentication method  
- [ ] Additional profile fields for NBQ beyond `sector` / `solution`  
- [ ] Whether chat is embedded in G2 site or calls standalone G3 UI  
- [ ] Timeline for joint integration test (roadmap Week 10)

## Next actions

| Owner | Action | Due |
|-------|--------|-----|
| G3 | Start FastAPI skeleton + `/health` | Week 3 |
| G3 | Share OpenAPI draft file with G2 | Week 2 ✓ |
| G2 | Return comments on JSON contracts | Week 3 |
| G3 | Update CORS when G2 URL known | Before integration test |

## Appendix

- UI mapping from Figma template: [../design/UI_TO_API_MAPPING.md](../design/UI_TO_API_MAPPING.md)  
- Integration overview: [../developer/G2_INTEGRATION.md](../developer/G2_INTEGRATION.md)
