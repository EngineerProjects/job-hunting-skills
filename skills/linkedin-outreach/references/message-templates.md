# Message Templates — linkedin-outreach

Templates for InMail, DM, and connection request notes. Each template has a slot for the anchor (research signal from step 4) and is pre-calibrated for voice rules.

**Before using**: replace all `[ANCHOR]`, `[COMPANY]`, `[ROLE]` placeholders with real content. Templates are starting points — rewrite the anchor line entirely for each target.

---

## Template 1 — InMail to Technical Recruiter (EN)

**When**: 2nd-degree recruiter at international / remote-first company.
**Char target**: 600-900 chars.

```
[ANCHOR sentence — about something specific they announced, posted, or hired for recently]

I've been following [COMPANY]'s work on [specific product/project] for a while and the direction feels like a strong fit for where I want to go next.

Background: [N] years as a Senior Data Engineer, mainly on [top 2-3 stack items from profile]. Most recently [one concrete achievement with number]. I also work at the intersection of data and GenAI, which feels relevant given [company signal].

If there's a fit, I'd be glad to have a 20-min call to see. I'm attaching my CV.

[Name]
```

---

## Template 2 — InMail to Technical Recruiter (FR)

**When**: 2nd-degree recruiter at French company.
**Char target**: 600-900 chars.

```
[ANCHOR — phrase concrète sur ce qui vient de se passer chez eux]

Je suis le travail de [COMPANY] depuis quelques mois, surtout [signal produit/technique], et la direction prise colle vraiment avec ce que je cherche.

Mon profil : [N] ans en tant que Senior Data Engineer, surtout sur [top 2-3 stack]. Dernièrement, [réalisation concrète avec chiffre]. Je travaille aussi sur des sujets GenAI, ce qui me semble pertinent au vu de [signal].

Si c'est le bon moment pour en parler, une visio de 20 min serait parfaite. Je joins mon CV.

[Prénom]
```

---

## Template 3 — DM to Engineering Manager / Head of Data (EN)

**When**: 1st or 2nd degree, technical manager. More direct than recruiter outreach.
**Char target**: 500-800 chars.

```
[ANCHOR — reference their recent post, a talk they gave, or a technical decision they shared]

I've been doing [brief description of relevant work — 1 sentence] and your post/talk/article resonated because [specific reason, not generic].

Quick context: [N] years on [top 2 stack items], most recently [one number that proves it]. Currently open to [type of role] at the right team.

Not sure if you have bandwidth for a 15-min chat but happy to sync if there's a mutual fit.

[Name]
```

---

## Template 4 — DM to Engineering Manager / Head of Data (FR)

**When**: 1st ou 2nd degré, manager technique dans une boite française.
**Char target**: 500-800 chars.

```
[ANCHOR — référence concrète à ce qu'ils ont posté, dit, ou construit récemment]

Je travaille sur des sujets proches ([description courte]) et ce que vous avez partagé sur [sujet] a retenu mon attention parce que [raison précise, pas générique].

Contexte rapide : [N] ans sur [top 2 stack], dernièrement [réalisation + chiffre]. Je suis ouvert à [type de poste] dans la bonne équipe.

Si vous avez 15 min pour en parler, je suis disponible — sinon aucun souci.

[Prénom]
```

---

## Template 5 — Connection Request Note (EN)

**When**: 3rd degree or no connection. Hard 300-char limit.
**Char target**: 200-280 chars.

```
[ANCHOR — 1 sentence max, ultra specific]

[N]-year Senior DE (Python/Spark/[top stack]). Interested in [COMPANY]'s direction. Happy to connect.

[Name]
```

Example (real):
```
Saw your Series B announcement and the data platform role caught my eye.

6-year Senior DE, mostly Python/Spark/dbt. Keen on Mistral's direction. Happy to connect.
```

---

## Template 6 — Connection Request Note (FR)

**When**: 3ème degré ou pas de connexion. Limite stricte 300 chars.
**Char target**: 200-280 chars.

```
[ANCHOR — 1 phrase, très spécifique]

[N] ans en Data Engineering (Python/Spark/[stack]). Intéressé par [COMPANY] et [ce qui est spécifique]. Ravi de connecter.
```

Exemple (réel) :
```
J'ai vu votre annonce de Série B et le poste Data Platform m'a interpellé.

6 ans en Data Engineering, surtout Python/Spark/dbt. Très intéressé par Mistral. Ravi de connecter.
```

---

## Template 7 — Follow-up (no reply after N days) (EN)

**When**: `follow_up_due` date reached, original message sent, no reply.
**Char target**: 200-350 chars.
**Rule**: One follow-up max. Never follow up a follow-up.

```
Quick follow-up on my message from [N] days ago — no worries if the timing isn't right.

If there's a better person to reach out to at [COMPANY] for [type of role], happy to be pointed in the right direction.

[Name]
```

---

## Template 8 — Follow-up (no reply) (FR)

**When**: relance après `follow_up_days` jours sans réponse.
**Char target**: 200-350 chars.

```
Relance rapide sur mon message de [il y a N jours] — pas de souci si le timing ne convient pas.

Si quelqu'un d'autre chez [COMPANY] est la bonne personne pour [type de poste], je suis preneur d'une redirection.

[Prénom]
```

---

## Anti-patterns — never use these

These openings get filtered mentally by every recruiter after the 50th copy-paste:

| ❌ Never | ✅ Instead |
|---|---|
| "Je me permets de vous contacter" | Jump straight to the anchor |
| "I hope this message finds you well" | Jump straight to the anchor |
| "Je suis actuellement à la recherche de nouvelles opportunités" | Anchor first, context second |
| "I came across your profile and was impressed" | Be specific about what and why |
| "I would love to learn more about potential opportunities" | State what you want in one sentence |
| "Please find attached my CV for your consideration" | "I'm attaching my CV" — active voice |
| "Do not hesitate to contact me" | "Happy to sync for 20 min if there's a fit" |
| "Looking forward to hearing from you" | Nothing, or a light CTA |

---

## Length calibration

| Type | Min | Target | Max |
|---|---|---|---|
| InMail (recruiter) | 500 | 650-850 | 1,000 |
| DM (EM/manager) | 350 | 500-700 | 900 |
| Connection note | 150 | 200-270 | 300 |
| Follow-up | 100 | 200-280 | 350 |

Under the min = looks lazy. Over the max = looks desperate. Sweet spot = reads in 20 seconds.
