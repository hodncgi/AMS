# Frontend — planned structure (implementation starts Week 9)

No React application in this Week 2 milestone. The onboarding UI will be built in Week 9 from the Figma template.

## Planned layout (Week 9+)

```
frontend/
├── chatbot-onboarding/   # React + Vite — Onboarding tab (live chat)
│   └── src/
│       └── components/
│           └── ChatInterface.tsx
└── g3-test/              # HTML test bench for NBQ + Change Risk (Week 5–6)
```

## Week 2 design decisions

- **Onboarding tab only** for the live chatbot (not Dashboard / Documentation / Manager)  
- Proxy `/api` → `http://localhost:8000`  
- Display answer mode (full AI vs fallback) and document sources (US-07, US-13)

See [../docs/developer/ARCHITECTURE.md](../docs/developer/ARCHITECTURE.md).
