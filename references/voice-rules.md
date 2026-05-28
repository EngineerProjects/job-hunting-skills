# Voice Rules for Comments

## Hard rules

1. **No em dashes** (`—`), en dashes (`–`), or double dashes (`--`). Biggest AI tell.
2. **Use `..` as soft pause** when you'd reach for an em dash. Feels human, matches the author's own rhythm.
3. **Capitalize personal names, company names, product names** (HubSpot, Claude, etc.). Lowercase reads as disrespectful.
4. **Sentence starts can be lowercase** (natural voice), but names inside are always capitalized.
5. **Don't mention the user's own product by name** in comments on third-party posts. Describe what they do instead ("our AI content system", "the platform we're building").

## Vocabulary blacklist (EN)

Sources: GPTZero frequency study, Originality.ai 10M-word corpus, alstonantony.com 283-word analysis.
Numbers in parentheses = how many times more frequent in AI text vs human text (GPTZero data).

**Statistically extreme tells (frequency multiplier):**
- "play a significant role in shaping" (182x)
- "today's fast-paced world" / "in today's digital age" (107x)
- "notable works include" (120x)
- "aims to explore" (50x)
- "showcasing" (20x), "aligns" (16x), "remarked" (18x)

**Dramatic verbs — never use:**
delve, unleash, unlock, unravel, navigate, redefine, foster, cultivate, transcend,
empower, amplify, underscore, illuminate, galvanize, pioneer, revolutionize

**Corporate jargon:**
leverage, utilize, facilitate, streamline, implement, integrate, synergy, holistic,
enable, proactive, robust, seamless, bespoke, cutting-edge, paradigm

**Filler adjectives:**
significant, crucial, essential, innovative, intrinsic, vital, dynamic, daunting,
transformative, groundbreaking, remarkable, pivotal, paramount, compelling

**Pretentious nouns:**
tapestry, labyrinth, realm, landscape, ecosystem, testament, journey, endeavor,
beacon, bastion, zeitgeist, ethos, dynamics, authenticity (as a buzzword)

**Transition fillers that read as AI:**
furthermore, moreover, consequently, subsequently, nevertheless, thus, overall,
typically, generally, specifically, clearly, obviously, importantly, essentially,
indeed, ultimately, certainly, conversely, correspondingly, cumulatively

**Killer phrases:**
- "It's important to note that"
- "It's worth mentioning that"
- "In conclusion" / "To summarize" / "In essence"
- "As previously mentioned"
- "It's not just X, it's Y"
- "Game-changer", "deep dive", "at the end of the day"

## Vocabulary blacklist (FR) — mots à ne jamais écrire

Sources: cours-ndrc.fr (2026), dubasque.org analyse lexicale, gpthuman.ai liste FR,
MIT Study 2024 ("Dans le paysage actuel" apparaît dans 23% des introductions IA).

**Ouvertures signature IA — supprimer immédiatement :**
- "Dans le paysage [actuel/moderne/contemporain] de…" (23% des intros IA selon MIT 2024)
- "À l'ère de [X]…"
- "Il est essentiel/crucial de noter que…"
- "Plongeons dans…"
- "Dans un monde où…"
- "À l'heure où…"
- "Il est indéniable que…"
- "C'est dans ce contexte que…"
- "Bien que [X], il n'en demeure pas moins que…"

**Adverbes IA (les plus fréquents en FR) :**
- particulièrement, notamment, spécifiquement
- essentiellement, fondamentalement, intrinsèquement
- indéniablement, incontestablement, véritablement
- significativement, considérablement, substantiellement
- principalement (quand utilisé comme remplissage)

**Adjectifs en doublon — l'IA empile toujours deux synonymes :**
- "crucial et essentiel", "robuste et fiable", "innovant et avant-gardiste"
- "efficace et efficient", "dynamique et évolutif", "complet et exhaustif"
Si tu as besoin des deux, l'un d'eux est de trop.

**Verbes et tournures de dissertation :**
- souligner, mettre en lumière, mettre en exergue, mettre en avant (quand c'est juste "dire")
- il convient de, il est important de noter, il est essentiel de
- permettre de (surutilisé — trouver le vrai verbe)
- s'inscrire dans, s'articuler autour, s'appuyer sur
- force est de constater
- dans ce contexte, à cet égard, en la matière, dans cette optique
- cela étant dit (faux pivot)

**Connecteurs mécaniques :**
- par ailleurs, en outre, de plus, qui plus est, de surcroît
- quoi qu'il en soit, néanmoins (sans vrai contraste derrière)
- ainsi (pour conclure une phrase banale)
- en effet (pour introduire ce qui est évident)
- dans un premier temps… dans un second temps… enfin

**Métaphores stock IA :**
- "naviguer dans la complexité"
- "au cœur de [stratégie/processus]"
- "pierre angulaire de succès"
- "écosystème de solutions"
- "tisser des liens"

**Mots valises et jargon marketing :**
- optimiser, fluidifier, dynamiser, valoriser, catalyser (sans objet concret)
- synergies, écosystème, paradigme, trajectoire, démarche (dans un sens vague)
- "solutions de pointe", "excellence inégalée", "approche innovante"
- "déverrouillez le pouvoir de", "révolutionnez la façon dont"

**Anglicismes IA en FR :**
- insights (→ "résultats", "observations")
- disruption (→ "rupture")
- pivotal (→ "décisif", "clé")

**Patterns structurels trahissant l'IA (langue-agnostique) :**
- Listes de exactement 3, 5, 7 ou 10 éléments
- Paragraphes de longueur quasi-identique (variance < 20 mots)
- Ton émotionnel uniforme du début à la fin, sans aspérités
- Cycle intro + développement + transition répété mécaniquement

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
