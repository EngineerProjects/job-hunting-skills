---
name: linkedin-cv-reviewer
description: CV review and scoring skill. Accepts a PDF or LaTeX CV, scores it across 5 dimensions (clarity, impact metrics, ATS-friendliness, length, AI tells), flags specific weaknesses with line-level suggestions, and optionally rewrites weak sections. Works as a standalone audit or as a prep step before linkedin-outreach. Nothing is changed without explicit approval.
---

# linkedin-cv-reviewer

Score your CV, fix what's weak, name it right before it goes anywhere.

## When this skill fires

User says any of:
- "score mon CV"
- "analyse mon CV"
- "revois mon CV"
- "j'ai déposé mon CV en PDF, qu'est-ce que tu en penses ?"
- "mon CV est bon ?"
- "prépare mon CV pour les candidatures"
- "corrige mon CV"
- "review my CV"

---

## Input formats accepted

| Format | How to provide |
|---|---|
| PDF | Drop the file path: `profile/cv.pdf` or `/tmp/my_cv.pdf` |
| LaTeX | Drop the path: `profile/cv.tex` (agent reads source directly) |
| Paste | Paste the raw text content of the CV into the chat |

For PDF: use the Read tool to extract text content. If the PDF is scanned (not text-selectable), ask the user to paste the text manually.

---

## Step 1 — Extract and read

Read the CV content fully before scoring anything.

For PDF input: read all text, preserve section structure.
For LaTeX input: read `.tex` source, ignore LaTeX commands — focus on the actual content text.
For pasted text: use as-is.

Confirm to the user: "Lu — [N] expériences, [N] projets, [N] lignes de formation."

---

## Step 2 — Score across 5 dimensions

Score each dimension 1–10. Be strict. A 7 means genuinely good, not "it's fine".

### Dimension 1 — Impact & Metrics (weight: high)

- Are achievements quantified? (numbers, %, time saved, scale)
- Are bullets outcome-focused ("reduced X by Y%") or task-focused ("responsible for X")?
- Is there at least one number per experience entry?

**Common failure**: "Développement de pipelines ETL" with no scale, no outcome, no metric.

### Dimension 2 — Clarity & Readability (weight: high)

- Does each bullet say ONE thing clearly?
- Are bullets under ~200 chars?
- Is the visual structure clean (consistent dates, alignment)?
- Is the profile/summary specific or generic?

**Common failure**: 3-line bullets that mix context + task + result into one unreadable block.

### Dimension 3 — ATS Compatibility (weight: medium)

- Are key technical skills visible as plain text (not buried in graphics or tables)?
- Are section headers standard ("Expériences", "Formation", "Compétences") — not invented labels?
- Are job titles recognizable? ("Data Engineer" not "Data Craftsman")
- Is the file a real text PDF (not scanned image)?

**Common failure**: skills in a visual tag cloud that ATS parsers skip entirely.

### Dimension 4 — Length & Density (weight: medium)

- Is it 1 page? (required for < 5 years XP, strongly preferred for < 10 years)
- Is there wasted whitespace that could fit another bullet?
- Are there filler words that add length but no information?

**Common failure**: 2-page CV where page 2 is 60% empty.

### Dimension 5 — AI Tells (weight: medium)

Check for vocabulary from `references/voice-rules.md` blacklists (both EN and FR).
Flag any of:
- "notamment", "particulièrement", "il convient de", "mettre en lumière"
- "leverage", "utilize", "seamlessly", "robust", "impactful"
- Adjective doublets: "efficace et efficient", "innovant et avant-gardiste"
- Openers: "Dans un monde où...", "À l'ère de..."
- Generic profile summary with no specific claim

**Common failure**: profile written by AI that sounds impressive but says nothing specific.

---

## Step 3 — Present the scorecard

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CV SCORECARD — [Name]
Reviewed: [date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Impact & Metrics        [N]/10
Clarity & Readability   [N]/10
ATS Compatibility       [N]/10
Length & Density        [N]/10
AI Tells                [N]/10

OVERALL                 [N]/10
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TOP 3 ISSUES (fix these first):

1. [Dimension] — [Specific problem]
   Where: [Section / bullet]
   Fix: [Concrete suggestion, ideally a rewrite]

2. [Dimension] — [Specific problem]
   Where: [Section / bullet]
   Fix: [Concrete suggestion]

3. [Dimension] — [Specific problem]
   Where: [Section / bullet]
   Fix: [Concrete suggestion]

GOOD (keep these):
  - [1-3 things that are actually working well]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type "fix [issue number]" to rewrite that section.
Type "fix all" to get a full corrected version.
Type "save" to store this version to profile/.
```

---

## Step 4 — Fixes (on request)

When the user says "fix 1", "fix all", or "corrige le profil" :

- Rewrite only the flagged section(s)
- Show the before/after side by side
- Do NOT change metrics or facts — only rephrase or restructure
- Do NOT invent new achievements
- Apply voice rules (no blacklisted words)
- Wait for approval before saving

---

## Step 5 — Save (on approval)

When the user approves a fixed version:

**If the input was a PDF** — save the corrected content as:
```
profile/cv_reviewed_[YYYYMMDD].md   ← corrected text for reference
```
And tell the user: "Pour rebuilder en PDF avec ce contenu, mets-le dans profile/cv.tex et lance le build."

**If the input was LaTeX** — propose to overwrite `profile/cv.tex` or save as a new version:
```
profile/cv_v2_[YYYYMMDD].tex
```

**CV naming rules** (apply every time a CV file is created or saved):

Read the user's initials from `profile/profile.md` (Name field).
First letter of first name + first letter of last name, lowercase. Stéphane KPOVIESSI → `sk`.

| Situation | Name pattern | Example |
|---|---|---|
| Base CV, no adaptation | `cv_[initials]_base_[YYYYMMDD].pdf` | `cv_sk_base_20260528.pdf` |
| Adapted for a company | `cv_[initials]_[company-slug]_[YYYYMMDD].pdf` | `cv_sk_mistral-ai_20260528.pdf` |
| Reviewed/corrected version | `cv_[initials]_reviewed_[YYYYMMDD].pdf` | `cv_sk_reviewed_20260528.pdf` |

**Slug rules:**
- Lowercase only
- Spaces → hyphens
- Remove accents, special chars, dots
- Max 20 chars for the company part
- Examples: `mistral-ai`, `hugging-face`, `back-market`, `alan-health`

---

## Constraints

- Never invent metrics or achievements — only restructure existing content
- Never claim a score of 9–10 unless the CV is genuinely exceptional
- Score 1–5 = broken, needs major work. Score 6–7 = functional but weak. Score 8+ = send it.
- A 1-page CV scoring 7+ on all dimensions = ready for outreach
- If the CV is 2 pages and the user has < 5 years XP: flag this as the #1 issue regardless of other scores
