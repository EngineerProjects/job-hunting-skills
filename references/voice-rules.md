# Voice Rules for Comments

## Hard rules

1. **No em dashes** (`—`), en dashes (`–`), or double dashes (`--`). Biggest AI tell.
2. **Use `..` as soft pause** when you'd reach for an em dash. Feels human, matches the author's own rhythm.
3. **Capitalize personal names, company names, product names** (HubSpot, Claude, etc.). Lowercase reads as disrespectful.
4. **Sentence starts can be lowercase** (natural voice), but names inside are always capitalized.
5. **Don't mention the user's own product by name** in comments on third-party posts. Describe what they do instead ("our AI content system", "the platform we're building").

## Vocabulary blacklist (EN)

Never use in comments:
- leverage, utilize, facilitate, streamline, robust, seamless, delve, navigate, unlock, harness, foster, cultivate
- fundamentally, essentially, ultimately, crucially, notably
- landscape, ecosystem, paradigm, realm, tapestry, journey
- "It's not just X, it's Y"
- "In today's fast-paced world"
- "Game-changer", "deep dive", "at the end of the day"

## Vocabulary blacklist (FR) — mots à ne jamais écrire

Ces mots sonnent AI immédiatement. En français, les tells sont souvent des adverbes longs
et des tournures de dissertation.

**Adverbes et intensificateurs IA :**
- particulièrement, notamment, essentiellement, fondamentalement, principalement
- indéniablement, incontestablement, véritablement, réellement (quand utilisé pour insister)
- significativement, considérablement, substantiellement

**Verbes et expressions de dissertation :**
- souligner, mettre en lumière, mettre en exergue, mettre en avant (quand c'est juste "dire")
- il convient de, il est important de noter, il est essentiel de
- permettre de (surutilisé — trouver le vrai verbe)
- s'inscrire dans, s'articuler autour, s'appuyer sur
- force est de constater
- dans ce contexte, à cet égard, en la matière

**Connecteurs de rédaction scolaire :**
- dans un premier temps... dans un second temps... enfin
- par ailleurs, qui plus est, de surcroît
- quoi qu'il en soit, néanmoins (quand il n'y a pas de vrai contraste)
- ainsi (en début de phrase pour conclure)
- en effet (pour introduire ce qui est évident)

**Ouvertures IA typiques :**
- "Dans un monde où..."
- "À l'heure où..."
- "Il est indéniable que..."
- "Cette approche innovante..."
- "C'est dans ce contexte que..."
- "Bien que [X], il n'en demeure pas moins que..."

**Mots valises :**
- optimiser, fluidifier, dynamiser, valoriser (sans complément concret)
- synergies, écosystème, paradigme, trajectoire (dans un sens vague)
- approche, démarche (quand on peut dire le truc directement)

**Règle de remplacement :** si tu retires le mot et la phrase dit la même chose, retire-le.
"Il est important de noter que les résultats sont bons" → "Les résultats sont bons."

## Structure

- 200-350 chars. Two short paragraphs max. Line break between them.
- One concrete number or named entity per comment minimum.
- One line that could be screenshot and quoted standalone.
- Never end with "What do you think?" — dead prompt. End with a specific question or a clean landing.

## Anti-patterns

- Thesis restatement ("so true, AI is changing everything")
- Generic praise ("great insight!", "love this")
- Overused openers: "This.", "100%", "Couldn't agree more"
- Rule of three ("faster, cheaper, better")
- Passive voice over 10% of clauses

## Algorithmic Scoring Criteria (NLP-level)

LinkedIn's ranker runs NLP on comments and rewards:

- **Depth** — comments with ≥12 words and multiple sentence structures
- **New keywords** — introduce at least one noun/concept NOT already in the parent post
- **Questions** — end with one that invites a sub-thread
- **Sub-thread sparks** — comments that generate replies from the author AND other commenters count as a strong signal

**Before submitting, check:** does your comment add at least one noun/concept not already in the post? If no, rewrite.

---

# Voice Rules for Outreach (linkedin-outreach skill)

Outreach messages (InMail, DM, connection notes) have different constraints from public content. Lower stakes editorially, higher stakes personally — one bad message poisons the contact.

## Hard rules

1. **Anchor first**: the first sentence must be about the company or contact, not about you. "I saw your Series B announcement" before anything about your background.
2. **No em dashes, no vocabulary blacklist** — same as comments. If pdflatex generated it, a recruiter will feel it.
3. **One CTA max**: end with exactly one ask. "Happy to sync for 20 min if there's a fit" — not two options, not "feel free to".
4. **Active voice throughout**: "I'm attaching my CV" not "please find attached". "I'd like a call" not "I would love the opportunity to discuss".
5. **Language matching**: detect company nationality from their LinkedIn page language. French company = FR. International / remote-first = EN. Never mix languages in one message.
6. **No desperation signals**: avoid "currently seeking", "actively looking", "I would be thrilled", "dream company". State facts. Let fit speak.

## Forbidden openers (instantly discard)

- "Je me permets de vous contacter"
- "I hope this message finds you well"
- "I came across your profile"
- "Je suis actuellement à la recherche d'opportunités"
- "I am reaching out because I am passionate about"
- Any variant of "I was impressed by your company"

## Structure rules

- InMail / DM: anchor (1 sentence) + why them (1-2 sentences) + why you (2-3 sentences with one number) + CTA (1 sentence)
- Connection note: anchor (1 sentence) + one-liner on yourself + soft CTA — max 300 chars total
- Follow-up: reference original message date + one exit ramp ("no worries if timing is off") + redirect ask — never beg

## Numbers beat adjectives

"6 years in data engineering, most recently reduced Spark costs by 40%" beats "experienced data professional with a strong background". One number per message minimum.

## Character limits

| Message type | Limit |
|---|---|
| InMail / DM | 1,900 chars |
| Connection request note | 300 chars |
| Follow-up | 350 chars recommended |

Stay well under the hard limit — long messages get skimmed, not read.
