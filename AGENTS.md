# Project conventions

This file is for any Codex agent working on this repository.
Read it before making changes. Keep `CLAUDE.md` and `AGENTS.md` aligned.

---

## Project identity

Personal LinkedIn job-hunting skill suite, forked from linkedin-skills.
Two pillars: **content** (10 inherited skills) + **outreach** (spontaneous applications).
See `docs/GOAL.md` for the full vision.

---

## Versioning

- Bump PATCH (`0.0.X`) by default for every shippable commit.
- Bump MINOR or MAJOR only when the user explicitly asks.
- After bumping: tag + GitHub Release (the shields.io badge reads from Releases API).

---

## Commits

- Co-author trailer is fine when appropriate.
- Verify locally before push: library smoke import passes, no broken refs in SKILL.md files.

---

## Skill structure

- No fixed number of skills. Add skills as needed.
- Frontmatter `description:` target <= 500 chars. No em dashes in description fields.
- Skill names are public surface — renaming requires updating all cross-references.

---

## Voice rules + reference layout

- Canonical voice rules: `references/voice-rules.md`
- Skill-local overrides in `skills/<skill>/references/` if needed.
- Root references: `references/hook-formulas.md`, `references/algorithm-heuristics.md`

---

## Layer separation

- **Read layer (Apify):** `lib/apify_client.py`
- **Write layer (Publora):** `lib/publora_client.py`
- **CV build:** `scripts/build_cv.py` — LaTeX to PDF, 1-page enforcement
- No LLM calls in scripts. Agent generates all content.

---

## Profile

- `profile/profile.md` — user preferences and targets
- `profile/cv.tex` — LaTeX CV source
- `profile/cv_builds/` — generated PDFs (gitignored)

---

## testing/ is gitignored

Never write secrets above `testing/`.

---

## Validation before push

```bash
python3 -c "from lib import publish, fetch_post, ApifyClient, PubloraClient; print('OK')"
```
