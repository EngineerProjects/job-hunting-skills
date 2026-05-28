# CV Adapter Agent

Read this when adapting `profile/cv.tex` for a specific company target.

---

## Role

Given a target company's context (what they build, their stack, the contact's role),
modify the LaTeX CV source to surface the most relevant bullets and build a 1-page PDF.

The source is always `profile/cv.tex`. Never modify it directly — work on a copy.

---

## Adaptation Logic

### Step 1 — Understand the target context

Collect before touching the .tex:
- What does the company build? (product type, domain)
- What stack signals did you find? (from their posts, job listings, About page)
- What role are you applying for? (data engineer, GenAI engineer, backend, etc.)
- What did the contact post about recently? (technical depth? culture? specific problems?)

### Step 2 — Read the CV source

Open `profile/cv.tex`. Identify:
- `% @tag` annotations on bullet points (e.g., `% @data_engineer`, `% @genai`, `% @backend`)
- The summary/objective section (usually 2-3 lines at the top)
- The skills/stack section
- Experience sections with their bullets

### Step 3 — Select relevant content

**Include bullets where:**
- Tags match the target role type
- Technology names overlap with the company's known stack
- Project scale / domain matches the company's context

**De-prioritize or hide bullets where:**
- Tags don't match (e.g., hide consulting-heavy bullets for a startup target)
- Stack is in profile.stack.avoid
- Experience is older than 5 years AND there are more recent equivalent bullets

**Summary section:** rewrite 1-2 lines to match the company's focus.
Example: for a RAG-heavy company, bring "LLM pipeline" language to the top.
Keep it factual — no buzzword inflation.

### Step 4 — Build the PDF

Save modified content to `/tmp/cv_adapted_{company_slug}.tex`, then:

```bash
python scripts/build_cv.py \
  --input /tmp/cv_adapted_{company_slug}.tex \
  --output profile/cv_builds/cv_{company_slug}_{YYYYMMDD}.pdf
```

If the build fails with "> 1 page":
1. Remove 1-2 bullets from the oldest / least relevant experience
2. If still too long: shorten the summary by 1 line
3. Rebuild
4. Never touch layout/spacing to force fit — fix content instead

### Step 5 — Report changes

Tell the user exactly what was adapted:

```
CV adapted for [Company]:
- Summary: replaced "data platform" focus with "LLM/RAG pipeline" focus
- Foregrounded: [Project X] (matches their RAG use case)
- De-emphasized: [Project Y] (legacy ETL, irrelevant here)
- Removed: 1 consulting bullet from 2021 (not relevant for startup)
- Built: profile/cv_builds/cv_mistral_20260528.pdf — 1 page ✓
```

---

## LaTeX Annotation Convention

Bullets in `profile/cv.tex` should follow this pattern:

```latex
\item Built a real-time feature store serving 50M events/day % @data_engineer @backend
\item Fine-tuned Mistral-7B on internal codebase for code review % @genai @llm
\item Led migration from Airflow to Prefect across 3 data teams % @data_engineer @platform
```

The agent reads the `% @tag` comment at end of line to decide inclusion.
If a bullet has no tag: include by default (generic experience).

---

## 1-Page Constraint

This is non-negotiable. Every CV sent is 1 page.

Reasons:
- Recruiters in France and Europe spend < 30 seconds on a first read
- 1-page forces prioritization — the best bullets surface, the noise disappears
- A 2-page CV from a 6-year engineer signals poor editing judgment

If the CV cannot fit in 1 page even after removing lower-priority bullets:
Stop and tell the user which section needs manual shortening in `profile/cv.tex`.
Do not send a 2-page CV.
