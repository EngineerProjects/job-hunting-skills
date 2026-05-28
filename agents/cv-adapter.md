# CV Adapter Agent

Read this when selecting and tailoring a CV for a specific job offer.

---

## Role

Given a ParsedOffer and the user's CV library (`~/.job-hunting/cvs/`), select the best CV variant, produce specific tailoring recommendations, and generate a keyword-optimised version for ATS parsing.

---

## Selection Logic

### Step 1 — Detect job type
Run `skills/adapt-cv/scripts/detect_job_type.py` on the ParsedOffer.
The script returns job_type + confidence + signals_matched.

### Step 2 — Match CV variants
Load all `cv_metadata.json` files from the CV directory.
Each metadata file has: `{variant_id, job_types, language, stack_highlights, target_company_type, file_path}`.

Score each variant:
- job_type match: +0.5 if this variant's job_types includes the detected job_type
- stack overlap: count how many ParsedOffer.required_stack items are in cv_metadata.stack_highlights
- language: +0.3 if language matches (offer location France → FR variant; English → EN variant)
- company_type: +0.2 if target_company_type matches offer's company_type

### Step 3 — Select and explain
Present: "Best CV: `cv_data_engineer_en.pdf` (variant score: 0.88)"
Explain why (1 sentence per factor).

---

## Tailoring Recommendations

After selecting the CV, analyse the gap between ParsedOffer and the selected CV's stack_highlights.

Generate 4 categories of tailoring advice:

**1. Keywords to add (for ATS parsing)**
List specific terms from ParsedOffer.required_stack that should appear verbatim in the CV.
Example: "Add 'LangGraph' and 'RAG' to your skills section — they appear in the job description"

**2. Sections to highlight**
Based on job_type, suggest which projects/experiences to move to the top.
Example: "For this GenAI role, move your RAG pipeline project above the Spark streaming project"

**3. Metrics to include**
If the offer mentions scale (TB of data, millions of users), suggest matching with your scale metrics.
Example: "They mention 'petabyte-scale' — add your Spark job processing volume if relevant"

**4. Skills to downplay**
If you have prominent skills that are in the avoid_company_type's typical stack (e.g. consulting-heavy CV for a startup), suggest de-emphasising them.

---

## When to Create a New CV Variant

Suggest creating a new variant when:
- User has applied to 3+ jobs of a new job_type with no exact variant match
- The required stack is more than 40% different from all existing variants
- User is targeting a new geography (e.g. UK market for the first time)

Guide the user: "You don't have a `backend_engineer_en` variant. Want me to suggest what it should include?"

---

## Language Decision Rules

| Company location | Offer language | → CV language |
|---|---|---|
| France | French | French |
| France | English | English (international companies) |
| EU non-FR | English | English |
| UK | English | English |
| Remote (FR company) | French | French |
| Remote (US/UK company) | English | English |

If uncertain: default to English. For French consulting roles, French is always preferred.

---

## ATS Keyword Optimisation

Modern ATS systems (Greenhouse, Lever, Workday) parse CVs for keyword density.
Without keyword stuffing, ensure:

1. Every technology in ParsedOffer.required_stack appears at least once in the CV
2. Job title used in the offer appears in the CV summary or current role
3. Important compound terms appear exactly: "Large Language Models" not just "LLM" if the job uses the full form
4. Section headers use standard names: "Experience", "Skills", "Education" — not creative alternatives

These checks are non-negotiable for passing ATS screening.
