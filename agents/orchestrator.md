# Orchestrator Agent

The **Job Hunting Orchestrator** is the master coordinator for the full pipeline.
Claude reads this when asked to run an end-to-end workflow or when the user says
"start my job search", "run the full pipeline", or "what should I do next".

---

## Role

Coordinate all sub-skills in the correct sequence, apply decision logic at each gate,
and maintain state via the PostgreSQL pipeline database.

---

## Daily Discovery Workflow (automated)

Run this every morning to keep the pipeline fresh:

```
1. search-jobs
   → Run search_greenhouse.py, search_lever.py, search_ashby.py
   → Pipe all results through deduplicate.py
   → Output: JSON array of new job objects

2. parse-offer (for each job)
   → Run parse_offer.py to extract structured data
   → Output: ParsedOffer JSON

3. score-offer (for each parsed offer)
   → Run score_offer.py --profile ~/.job-hunting/profile.json
   → Output: ScoredOffer JSON with recommendation

4. Decision gate:
   → relevance_score >= 0.70: save to DB (status=wishlist) via save_job.py
   → relevance_score >= 0.85: immediately notify user "🔥 High-score job found: [title] at [company]"
   → relevance_score < 0.70: log only (do not save)

5. dashboard
   → Run show_pipeline.py to display updated pipeline
```

---

## Application Workflow (per-job, user-triggered)

Triggered when user says "I want to apply to [company/role]":

```
1. Confirm job in DB (or search for it)
   → If not in DB: run search + parse + score first

2. adapt-cv
   → detect_job_type.py → select_cv.py
   → Present: "Best CV: cv_data_engineer_en.pdf (score: 0.88)"
   → Tailoring suggestions to review

3. HUMAN GATE: "Apply this CV? Add any custom tailoring?"
   → Wait for user confirmation before proceeding

4. generate-cover-letter
   → Agent writes cover letter + email + LinkedIn message directly (no script needed for generation)
   → Calls save_draft.py to validate and persist
   → Present draft cover letter + email + LinkedIn message

5. HUMAN GATE: "Review cover letter — type 'ok' to proceed, or paste edits"
   → Wait for approval

6. apply-job
   → Detect ATS type from job URL
   → If Greenhouse: apply_greenhouse.py (API, dry-run first)
   → If Lever/Ashby/Workday/WTTJ/other: apply_playwright.py pre-flight, then playwright-cli commands
   → ALWAYS show preview before submission
   → ALWAYS require "confirm" before submitting

7. Post-application:
   → update_status.py --status applied
   → Log to activity_log
   → Suggest: recruiter-search to find the hiring manager
```

---

## Networking Workflow (for high-priority applications)

Triggered after applying to a job with score >= 0.80:

```
1. recruiter-search
   → Agent browses LinkedIn via browser tools, extracts contact profiles
   → search_recruiters.py --company [company] --role-keywords [role] --json '[...]'
   → Present scored contact list

2. HUMAN GATE: "Select contacts to reach out to"

3. linkedin-outreach
   → Agent drafts message for each selected contact
   → save_message.py to validate and persist each draft
   → Present drafts (connection request + first message)

4. HUMAN GATE: "Review messages — approve each one"
   → Never send automatically

5. After contact responds:
   → update_status.py --status screening --note "Response from [name]"
   → followup-manager if needed
```

---

## Branding Workflow (weekly)

```
1. post-generator
   → Suggest 3 post topics based on recent work, trending topics
   → Generate post for user-selected topic
   → A/B test: 3 variants

2. HUMAN GATE: User selects best variant, edits, posts manually

3. comment-generator
   → Find 3-5 relevant posts by hiring managers or thought leaders
   → Draft comments for each
   → HUMAN GATE: user reviews and posts manually
```

---

## Decision Logic Reference

### When to proceed automatically vs. pause

| Decision | Auto | Requires Human |
|---|---|---|
| Search and score jobs | ✓ | |
| Save wishlist jobs (score ≥ 0.70) | ✓ | |
| Select CV variant | Show recommendation | Final approval |
| Generate cover letter draft | ✓ | Review before use |
| Submit application | NEVER | Always confirm |
| Send LinkedIn message | NEVER | Always confirm |
| Publish LinkedIn post | NEVER | Always confirm |
| Update status to applied | After submission | |
| Log follow-up needed | ✓ | |

---

## Job Status State Machine

```
discovered (not in DB)
  ↓
wishlist     ← default when score ≥ 0.70
  ↓
applied      ← after confirmed submission
  ↓
screening    ← after HR contact / phone screen scheduled
  ↓
interviewing ← after technical / manager interview
  ↓
[offer]      ← received offer
[rejected]   ← received rejection
[withdrawn]  ← user withdrew application
```

Lateral transitions: any status → followup_needed → back to current status

---

## Error Recovery

| Error | Recovery |
|---|---|
| DB not connected | Show instructions: `export DATABASE_URL=...` + `python setup_db.py` |
| Greenhouse API 404 | Try common board token variations (lowercase, no spaces) |
| CAPTCHA on form | Pause, alert user, wait for manual solve |
| Cover letter too long | Re-generate with `--max-words 300` instruction |
| No CV variants found | Guide user to create `~/.job-hunting/profile.json` with `cv_variants` |
| Score below threshold | Show the offer anyway with explanation, let user override |

---

## Environment Setup Checklist

Before running any workflow, verify:
- [ ] `DATABASE_URL` set and DB tables created (`python skills/save-application/scripts/setup_db.py`)
- [ ] `~/.job-hunting/profile.json` exists with personal info and stack
- [ ] CV files referenced in `profile.json:cv_variants` actually exist
- [ ] `GREENHOUSE_COMPANY_TOKENS` set (for Greenhouse search)
- [ ] `playwright-cli` available (`npm install -g @playwright/cli@latest`) if using apply-job or recruiter-search
