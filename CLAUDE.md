# Project conventions

This file is for any Claude Code agent working on this repository.
Read it before making changes. These conventions are mandatory.

---

## Project identity

This is a personal LinkedIn job-hunting skill suite, forked from linkedin-skills.
Two pillars: **content** (10 inherited skills) + **outreach** (spontaneous applications).
See `docs/GOAL.md` for the full vision.

---

## Versioning

- Bump the PATCH segment (`0.0.X`) by default for every shippable commit.
- Bump MINOR or MAJOR only when the user explicitly asks.
- After bumping:
  1. `git tag -a v<X.Y.Z> -m "..."`
  2. `gh release create v<X.Y.Z> --title "v<X.Y.Z>" --notes "<changelog>" --latest`

---

## Commits

- Co-author trailer is fine: `Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>`
- Verify locally before push: library smoke import passes, no broken refs in SKILL.md files.

---

## Skill structure

- No fixed number of skills. Add skills as needed.
- Frontmatter `description:` target <= 500 chars.
- No em dashes (`—`) in `description:` frontmatter fields.
- Skill names are public surface — renaming requires updating all cross-references.

---

## Voice rules + reference layout

- Canonical voice rules: `references/voice-rules.md`
- Skill-local overrides in `skills/<skill>/references/voice-rules.md` if needed.
  Start local overrides with: `Global voice rules: see root references/voice-rules.md`
- Root references shared across skills: `references/hook-formulas.md`, `references/algorithm-heuristics.md`
- Cite root references from skills with `../../references/X.md`

---

## Layer separation

- **Read layer (Apify):** `lib/apify_client.py` — fetch post bodies, comment threads, engagers.
  Skills call `lib.fetch_post(url)` which handles the APIFY_TOKEN-or-paste fallback.
- **Write layer (Publora):** `lib/publora_client.py` — post and comment publishing.
  Skills call `lib.publish(kind, draft_text, target_url, ...)`.
- **CV build:** `scripts/build_cv.py` — LaTeX to PDF, 1-page enforcement.
- No LLM calls in scripts. All content generation happens in the running agent.

---

## Profile

- User profile: `profile/profile.json`
- CV source: `profile/cv.tex`
- CV builds (gitignored): `profile/cv_builds/`
- Outreach log: `profile/outreach_log.json`

---

## testing/ is gitignored

Local scratch directory for API keys, sample responses, integration scripts.
Never write secrets above `testing/`.

---

## Validation before push

```bash
python3 -c "from lib import publish, fetch_post, ApifyClient, PubloraClient; print('OK')"
grep -rn "Sergey\|bulaev" SKILL.md skills/*/SKILL.md CLAUDE.md AGENTS.md 2>/dev/null  # must be empty
```
