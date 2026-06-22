# Chatbot knowledge scope (Week 2)

**Deliverable:** Document chatbot knowledge scope (RAG and API-aware answers)  
**Linked user stories:** US-12, US-13, US-14, US-16 (future DB)

## 1. Purpose

Define what the onboarding assistant **may** answer in v1 and how knowledge is sourced, before implementation (Weeks 6–8).

## 2. Topic domains

| Domain | Example questions | Source (v1 POC) | Source (v2) |
|--------|-------------------|-----------------|-------------|
| Employee onboarding | First weeks, mentors, tools | Curated topics + catalog chunks | Relational DB (US-16) |
| CI/CD & Git | Pipelines, branches, PRs | Catalog chunks | DB |
| Security & compliance | MFA, policies, incidents | Catalog chunks | DB |
| AMS intake | Transition readiness, SLAs | Catalog chunks | DB |
| Change risk (explain) | Formula, drivers, examples | Algorithm context + KB | DB + `/change-risk` |
| NBQ (explain) | Sector weights, Healthcare boost | Algorithm context + KB | DB + `/nbq/next` |
| Meta / platform | What is this assistant? | Platform topic | DB |

## 3. Out of scope for the chatbot

- Final change approval decisions (AMS leads)  
- Client-specific production data  
- Group 2 portal navigation (until integration)  
- Invented contacts, deadlines, or procedures (US-14)

## 4. Retrieval strategy (planned)

```
User question
    → keyword match on chunks (Week 6–7)
    → inject algorithm context if risk/NBQ query (Week 8)
    → Mistral generates answer with sources (Week 8)
    → if LM Studio offline: fallback excerpts + explicit message
```

## 5. Source display requirements (US-13)

Each answer should expose when possible:

- Document **title**  
- **Category** (e.g. DevOps, AMS Algorithms)  
- **Source identifier** (catalog id or DB key)

If no match: state clearly that no documentation was found (US-14).

## 6. Content governance (US-15 — Week 11+ / v2)

Knowledge managers will maintain documents in the **relational onboarding database**:

- Create / update / deactivate entries  
- Deactivated docs excluded from retrieval  
- Audit via metadata (last update date)

Week 2: file-based `catalog.json` specification drafted; DB integration scheduled with Group 1.

## 7. Estimated corpus size (target Week 6)

| Type | Count |
|------|-------|
| Business topics | 10–14 |
| Catalog chunks | 30–40 |
| Algorithm explainers | 2 (change risk, NBQ) |

## 8. Acceptance for Week 2

- [x] Topic list agreed  
- [x] Source strategy documented  
- [x] US-13 / US-14 / US-16 requirements reflected  
- [ ] Chunks authored (Week 6)  
- [ ] DB connector (v2)
