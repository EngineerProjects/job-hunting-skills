# Outreach Orchestrator

Read this when the user wants to run a full outreach session — targeting multiple companies,
preparing a batch of personalized applications, or asking "what should I do next for my job search".

---

## Role

Coordinate the full spontaneous-application workflow across multiple targets in one session:
load profile, build target list, research each company, adapt CV, draft messages, present for approval.

Cap at 5 targets per session (LinkedIn rate limit safety).

---

## Full Session Workflow

```
1. Load profile/profile.md
   → Verify all required fields are present
   → Check profile/cv.tex exists
   → Check pdflatex available (run: python scripts/build_cv.py --help)

2. Build target list
   → Combine: user-provided companies + auto-discovered from LinkedIn
   → Present shortlist for validation before proceeding
   → Max 5 targets for this session

3. For each target (in parallel research where possible):
   a. Find the right contact (recruiter > EM > Head of)
   b. Research company + contact activity (2-3 key anchors)
   c. Adapt CV to context (scripts/build_cv.py → 1 page enforced)
   d. Draft personalized message

4. Present all dossiers at once for batch review
   → User edits / approves each one
   → User sends manually on LinkedIn

5. Log approved outreach to profile/outreach_log.json  (append only -- never overwrite)
```

---

## Decision Points

| Situation | Action |
|---|---|
| No good contact found (company too small, no LinkedIn presence) | Flag to user, skip or use generic company page message |
| Contact is 3rd degree with no mutual connections | Lower priority, draft connection request note only (300 chars) |
| Company has zero recent LinkedIn activity | Use job postings and "About" section as anchor instead |
| CV build fails (>1 page) | Reduce bullets, rebuild — never exceed 1 page |
| User provides a job posting URL | Extract company + role context from it, use in CV adaptation AND message anchor |

---

## Session Output Template

At the end of a session, summarize:

```
=== SESSION SUMMARY ===

Targets processed: N
Dossiers approved: N
Dossiers pending: N

Approved outreach:
  1. [Company] → [Contact name, title] — [message type]
  2. ...

CVs built:
  - profile/cv_builds/cv_{company}_{date}.pdf (all 1 page ✓)

Next steps:
  - Send each message manually via LinkedIn
  - Check back in 5-7 days for responses
  - Use linkedin-outreach skill for follow-ups if no response after 10 days
```
