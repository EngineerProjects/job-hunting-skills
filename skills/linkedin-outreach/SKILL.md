---
name: linkedin-outreach
description: Spontaneous job application skill for LinkedIn. Builds target company list (manual + auto-discovery), finds the right contact (recruiter, engineering manager, or VP), researches company activity for a personal anchor, adapts the LaTeX CV to one page for the role, drafts a personalized InMail or DM, and presents a full approval dossier before the user sends manually. Nothing is sent without explicit "send" confirmation.
---

# linkedin-outreach

Spontaneous application workflow. You research, adapt, draft — the user decides and sends.

## When this skill fires

User says any of:
- "je veux postuler chez X"
- "trouve-moi un contact chez X"
- "adapte mon CV pour X"
- "rédige un InMail pour X"
- "cherche des boites qui recrutent des data engineers"
- "lance une session de candidatures spontanées"
- "fais une prospection LinkedIn"

---

## Prerequisites

Read `profile/profile.md` before step 1. All decisions (language, salary filter, stack match, avoid list) come from it.

Required fields:
- `personal.name`, `personal.linkedin_url`
- `preferences` (remote, locations, salary, avoid_company_types)
- `stack` (must_have, strong, avoid)
- `cv.source` (path to .tex file)
- `cv.builds_dir` (output directory)

If any required field is missing or still set to placeholder values ("Ton Nom", "toi@example.com"), stop and ask the user to fill in `profile/profile.md` first.

---

## Step 1 — Load profile

Read `profile/profile.md`.

Extract and confirm aloud:
- Target role: `experience.current_title`
- Locations: `preferences.locations`
- Stack highlight: top 3 from `stack.must_have` + `stack.strong`
- Avoid: `preferences.avoid_company_types`
- Salary floor: `preferences.salary_min_eur`
- Message language: `preferences.message_language` ("auto" = detect company language; FR for French companies, EN for international)

---

## Step 2 — Build the target list

Combine two sources:

### Manual targets (from profile.json)

Read `targets.manual`. For each entry, note `company`, `linkedin_company_url`, `notes`.

### Auto-discovery (if `targets.auto_discovery.enabled == true`)

Use your browser tools to search LinkedIn for companies matching the profile. Cap at `targets.auto_discovery.max_per_session` new companies per session.

**Search query template** (adapt to profile preferences):
```
LinkedIn URL: https://www.linkedin.com/search/results/companies/
Filters:
  - Industry: [from targets.auto_discovery.industries]
  - Location: [from targets.auto_discovery.locations]
  - Company size: [from targets.auto_discovery.company_size]
```

For each company found, check:
1. Does it appear in `preferences.avoid_company_types`? Skip if yes.
2. Does it have open positions that match the profile stack? Note the signal.
3. Any recent public activity (funding round, product launch, hiring spike)? Note it.

Build a ranked list: manual targets first (user-curated), then auto-discovery hits sorted by stack match.

**Dedup against outreach log**: Read `profile/outreach_log.json` if it exists. Skip any company that has an entry with `status != "closed"` and `last_contact_date` within the last `outreach.cooldown_days`.

Present the list to the user before proceeding:
```
Target list for this session (max 5):

1. Mistral AI         — manual target, Paris/remote, LLM stack
2. Hugging Face       — manual target, remote, open-source AI
3. Dataiku            — auto-discovery, Paris, data/ML platform
4. Artefact           — auto-discovery, Paris, data consulting (check avoid list?)
5. Pennylane          — auto-discovery, Paris/remote, fintech+data

Continue with all 5, or drop/add?
```

Wait for confirmation before proceeding.

---

## Step 3 — Find the right contact

For each target company, find one contact. Priority order:

1. **Technical Recruiter** (titre contient: Recruiter, Talent Acquisition, Talent Partner, RH Tech)
2. **Engineering Manager / Head of Data** (titre contient: Head of Data, Engineering Manager, Lead Data, Staff Engineer)
3. **VP / Director** (fallback only — use if no recruiter or EM found)

**Search method** (LinkedIn People Search):
```
https://www.linkedin.com/search/results/people/
Query: "[role keyword]" + company name
Filter: Current company = [company name]
```

Try these query variants in order, stop at first result:
1. `recruiter "Mistral AI"` filtered to current company
2. `talent acquisition "Mistral AI"` filtered to current company
3. `head of data "Mistral AI"` filtered to current company
4. `engineering manager "Mistral AI"` filtered to current company

For each candidate found, extract:
- Full name
- Current title
- Profile URL
- Connection degree (1st / 2nd / 3rd)
- Mutual connections count (if visible)

**If no contact found**: Note "no contact found" for this company. Draft a connection request to a relevant person instead of InMail.

---

## Step 4 — Research company activity

For each target, find 1-2 concrete anchors to personalize the message. This makes the message feel researched, not templated.

**Signal sources** (check in order, stop when you have 1-2 anchors):

1. **LinkedIn company page** — recent posts, job postings, announcements
   ```
   https://www.linkedin.com/company/[slug]/posts/
   ```
2. **LinkedIn job postings** — what stack/role are they actively hiring for?
   ```
   https://www.linkedin.com/company/[slug]/jobs/
   ```
3. **Contact's recent posts** — what has the EM/recruiter posted in the last 30 days?
4. **Public news** (funding, product launch, acquisition) — use WebSearch if needed

**Anchor quality criteria:**
- Specific: "your Series B last month" beats "you're growing fast"
- Relevant: connects to why YOU specifically fit
- Recent: last 90 days preferred

Extract exactly 1-2 anchors. Note them for step 6.

---

## Step 5 — Adapt the CV

Read the LaTeX source: `profile.cv.source` (default: `profile/cv.tex`).

**Tag system**: bullets in the .tex are annotated with `% @tag` comments:
```latex
\item Built a real-time feature store serving 50M events/day % @data_engineer @backend
\item Fine-tuned Mistral-7B for internal code review % @genai @llm
\item Reduced Spark job cost by 40% via adaptive query execution % @data_engineer @cost
```

**Adaptation logic:**

1. Read all bullets and their `% @tag` annotations
2. Determine relevant tags for this target company (infer from job posting, company stack, sector)
3. Keep all bullets tagged with relevant tags
4. For bullets with no tag (untagged = always-include anchors like education, key metrics)
5. For bullets tagged with `% @avoid` or clearly irrelevant tags: comment out or remove
6. Reorder sections if needed (put most relevant experience first)
7. Do NOT invent new bullets. Do NOT change numbers. Only include/exclude and reorder.

**Build the PDF:**
```bash
python scripts/build_cv.py \
  --input /tmp/cv_[company_slug]_adapted.tex \
  --output profile/cv_builds/cv_[company_slug]_[date].pdf
```

If the script returns exit code 1 (page count > 1):
- Remove 1-2 bullets from the least-relevant experience
- Re-run the build
- Repeat until 1 page, max 3 attempts
- If still failing after 3 attempts: report what was cut and ask user to manually slim the .tex

Report clearly:
```
CV adapted for Mistral AI:
  Kept:   @genai (4 bullets), @data_engineer (3 bullets), untagged (2 bullets)
  Removed: @backend (2 bullets), @cost (1 bullet)
  Result: 1 page ✓
  Saved:  profile/cv_builds/cv_mistral-ai_20260528.pdf
```

---

## Step 6 — Draft the message

Draft ONE message per target. Type depends on contact's connection degree:

| Connection | Message type | Char limit |
|---|---|---|
| 1st degree | Direct message (DM) | 1,900 |
| 2nd degree | InMail or connection request + note | InMail: 1,900 / Note: 300 |
| 3rd degree / no connection | Connection request note | 300 |

**Message structure:**

```
[Anchor line — 1 sentence, references the research signal from step 4]

[Why them — 1-2 sentences: what about this company/team makes you want to join specifically]

[Why you — 2-3 sentences: the 1-2 stack matches most relevant to this company, one concrete number]

[CTA — 1 sentence: low-friction ask, not "do you have openings?"]
```

**Hard rules (outreach voice):**
- Never open with "je me permets de vous contacter" or "I hope this message finds you well"
- Never "je suis actuellement à la recherche d'opportunités" — sounds desperate
- First sentence must be about THEM, not about you
- One CTA max. Not "feel free to" — say exactly what you want
- Match language to company: French company in France = FR; international / remote-first = EN; "auto" in profile = detect from company LinkedIn page language
- No em dashes, no vocabulary blacklist items (see voice-rules.md)
- Connection request notes: 300 chars max, must fit one screen — anchor + one-liner on yourself + CTA

**See `references/message-templates.md`** for pre-built templates by contact type.

---

## Step 7 — Approval gate

Present a full dossier for each target. Nothing moves forward without explicit "send" from the user.

**Dossier format:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DOSSIER — [Company Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CONTACT
  Name:       [Full Name]
  Title:      [Current Title]
  Profile:    [LinkedIn URL]
  Degree:     [1st / 2nd / 3rd]
  Message:    [InMail / DM / Connection note]

ANCHORS
  1. [Anchor 1 — e.g. "Series B announced May 2026"]
  2. [Anchor 2 — e.g. "Hiring 3 Senior Data Engineers in Paris"]

CV
  Adapted:    profile/cv_builds/cv_[slug]_[date].pdf
  Tags kept:  @genai (4), @data_engineer (3)
  Tags cut:   @backend (2)

MESSAGE
────────────────────────────────────────
[Full message text here]
────────────────────────────────────────
Chars: [N] / [limit]

SEND INSTRUCTIONS (manual)
  1. Open: [profile URL]
  2. Click "Message" or "Connect"
  3. Paste the message above
  4. Attach CV: [pdf path]
  5. Send

Type "send" to log this as sent, or suggest edits.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Present all dossiers in sequence. User can:
- `send` — mark as sent in log, move to next
- `skip` — skip this target, move to next
- `edit [instruction]` — redraft message with the instruction, re-present
- `edit cv [instruction]` — re-adapt CV with instruction, rebuild, re-present

---

## Step 8 — Post-approval actions

After "send" confirmation for each target:

**Update outreach log** (`profile/outreach_log.json`):

```json
{
  "company": "Mistral AI",
  "contact_name": "Alice Martin",
  "contact_url": "https://linkedin.com/in/alice-martin",
  "contact_title": "Technical Recruiter",
  "message_type": "InMail",
  "cv_path": "profile/cv_builds/cv_mistral-ai_20260528.pdf",
  "anchors": ["Series B May 2026", "hiring 3 Senior DE Paris"],
  "date_sent": "2026-05-28",
  "status": "sent",
  "follow_up_due": "2026-06-04",
  "notes": ""
}
```

Create `profile/outreach_log.json` if it doesn't exist (array of entries).
Append entry. Do not overwrite existing entries.

**Follow-up reminder**: Calculate `follow_up_due = date_sent + outreach.follow_up_days`. Report it.

**Session summary** (after all targets processed):

```
Session complete.

Sent:    3 / 5 targets
Skipped: 2 (user choice)

Follow-up schedule:
  2026-06-04  Mistral AI      (Alice Martin)
  2026-06-04  Hugging Face    (Bob Chen)
  2026-06-05  Dataiku         (Sophie Leclerc)

CVs built:
  profile/cv_builds/cv_mistral-ai_20260528.pdf
  profile/cv_builds/cv_hugging-face_20260528.pdf
  profile/cv_builds/cv_dataiku_20260528.pdf

To follow up, say: "fais les relances du [date]"
```

---

## Constraints

- **Max per session**: `outreach.max_per_session` (default 5). Never send more in one session.
- **Cooldown**: Skip companies in outreach_log with status != "closed" within `outreach.cooldown_days`.
- **1-page CV**: Hard constraint. Build script enforces it. Never deliver a 2-page CV.
- **No fabrication**: Do not invent metrics, titles, or responsibilities. Only include/exclude existing bullets.
- **No auto-send**: The user always sends manually. This skill drafts, researches, and logs — never sends.
- **Draft-first**: Show the dossier before logging. Never log a "sent" entry without user confirmation.
- **Avoid list**: Never target company types in `preferences.avoid_company_types` (consulting, ESN, SSII by default).
- **Language matching**: Match message language to company nationality. When in doubt, default to EN for international companies.
