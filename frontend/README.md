# Frontend — Week 2

## Design preview (Week 2 deliverable)

**[design-preview/index.html](design-preview/index.html)** — static mockup from the manager Figma template. Open in any browser.

## React application (Week 9)

```mermaid
flowchart LR
    subgraph FE["frontend/chatbot-onboarding/"]
        Vite[Vite dev server :3000]
        Onb[Onboarding tab<br/>ChatInterface]
        Demo[Demo tabs<br/>static content]
    end

    subgraph BE["backend :8000"]
        Chat[POST /chat]
    end

    Onb -->|proxy /api| Chat
    Demo -.->|no API v1| Demo
```

Planned stack: React, TypeScript, Vite, shadcn/ui from Figma template.

See [../docs/design/FIGMA_TEMPLATE_REVIEW.md](../docs/design/FIGMA_TEMPLATE_REVIEW.md).
