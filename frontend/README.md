# Frontend — Week 2

## Design preview (Week 2 deliverable)

**[design-preview/index.html](design-preview/index.html)** — static mockup from the manager Figma template. Open in any browser.

## Planned timeline

| Week | Deliverable |
|------|-------------|
| **4** | HTML chat page wired to `POST /chat` |
| **8** | React app (Figma → Onboarding tab live) |

```mermaid
flowchart LR
    subgraph W4["Week 4 — HTML chat"]
        HTML[design-preview + fetch]
    end

    subgraph W8["Week 8 — React"]
        Vite[Vite :3000]
        Onb[Onboarding tab]
    end

    subgraph BE["backend :8000"]
        Chat[POST /chat]
    end

    HTML --> Chat
    Onb -->|proxy /api| Chat
```

See [../docs/developer/ROADMAP.md](../docs/developer/ROADMAP.md) and [../docs/design/FIGMA_TEMPLATE_REVIEW.md](../docs/design/FIGMA_TEMPLATE_REVIEW.md).
