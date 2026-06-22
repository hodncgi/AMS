# UI → API mapping (Week 2)

Maps each Figma template area to Group 3 backend routes defined in [../developer/API.md](../developer/API.md).

## Onboarding tab (primary)

| UI element | User action | API call | Week |
|------------|-------------|----------|------|
| Chat input | Send message | `POST /chat` | 9 |
| Send button | Submit conversation | `POST /chat` | 9 |
| Source list under reply | Read citations | Response field `sources[]` | 9 |
| Mode badge | See full AI vs fallback | Response field `mode` | 9 |
| Pipeline / status bar | Check assistant status | `GET /health` | 9 |
| Suggested questions | Quick prompts | `POST /chat` (prefilled) | 9 |

## Management tab (demo)

| UI element | Planned behaviour | API |
|------------|-------------------|-----|
| Team overview cards | Static demo data | None (Week 2) |
| Future: risk summary | Group 2 integration | `POST /change-risk` via G2 site |

## Documentation tab (demo)

| UI element | Planned behaviour | API |
|------------|-------------------|-----|
| Document list | Static catalog | Future: Group 1 DB (US-16) |
| Search | Client-side filter on static list | None in POC |

## My Onboarding tab (demo)

| UI element | Planned behaviour | API |
|------------|-------------------|-----|
| Task checklist | Static Figma content | None in POC |

## G3 test bench (separate page — not in Figma tabs)

| Page | Purpose | API | Week |
|------|---------|-----|------|
| `/g3-test` HTML bench | Consultant algorithm testing | `POST /nbq/next`, `POST /change-risk` | 5–6 |

## Group 2 integration (future)

```
Figma shell (Onboarding) ──POST /chat──► G3 FastAPI
G2 risk site forms      ──POST /change-risk──► G3 FastAPI
G2 intake wizard        ──POST /nbq/next──► G3 FastAPI
```

See [../developer/G2_INTEGRATION.md](../developer/G2_INTEGRATION.md).
