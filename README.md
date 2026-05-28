# LinkedIn Job Hunting Skills

Skills LinkedIn pour ingénieurs Data/AI/GenAI en recherche d'opportunités.

Fork de [linkedin-skills](https://github.com/sergebulaev/linkedin-skills) — tous les outils de content marketing existants, plus un pilier **outreach** : identifier des contacts dans des entreprises cibles, adapter le CV en LaTeX (1 page), rédiger des candidatures spontanées personnalisées.

---

## Ce que ça fait

### Content (hérité de linkedin-skills)

| Skill | Trigger |
|---|---|
| `linkedin-post-writer` | "écris un post LinkedIn sur..." |
| `linkedin-comment-drafter` | "commente ce post : [URL]" |
| `linkedin-reply-handler` | "réponds à ce commentaire : [URL]" |
| `linkedin-humanizer` | "audite ce draft / supprime les AI tells" |
| `linkedin-hook-extractor` | "extrais la formule de hook de ce post viral" |
| `linkedin-content-planner` | "planifie ma semaine LinkedIn" |
| `linkedin-thread-monitor` | "qui a répondu à mes commentaires ?" |
| `linkedin-engager-analytics` | "qui a liké/commenté ce post ?" |
| `linkedin-profile-optimizer` | "audite mon profil LinkedIn" |
| `linkedin-employee-advocacy` | coordination de contenu d'équipe |

### Outreach (en cours de construction)

| Skill | Trigger |
|---|---|
| `linkedin-outreach` | "trouve des contacts chez X et rédige un message d'approche" |

**Workflow outreach :**
1. Cibles manuelles (liste fournie) + auto-discovery (LinkedIn search par profil)
2. Recherche de l'activité récente de chaque entreprise cible
3. Adaptation du CV LaTeX pour le contexte (1 page max, build PDF)
4. Rédaction d'un message personnalisé ancré dans l'actualité de la cible
5. Validation humaine — jamais d'envoi automatique

---

## Setup

### Requis (zéro setup — mode draft)

Aucune clé API nécessaire. Les skills rédigent des drafts que tu copies-colles manuellement sur LinkedIn.

```bash
git clone <repo>
cd job-hunting-skills
pip install -r requirements.txt
```

### Optionnel — Publora (auto-post en 2 min)

Sur approbation, les skills publient automatiquement sur LinkedIn.

1. Crée un compte gratuit : **https://app.publora.com/signup** (15 posts/mois offerts)
2. Connecte ton compte LinkedIn (Channels → Add Channel)
3. Copie ta clé API
4. Dans `.env` :
   ```
   PUBLORA_API_KEY=sk_...
   LINKEDIN_PLATFORM_ID=linkedin-...
   ```

### Optionnel — Apify (lecture de contenu LinkedIn)

Permet aux skills de lire le texte des posts, threads de commentaires, et listes d'engageurs sans cookies.

1. Compte gratuit : **https://console.apify.com/sign-up** ($5/mois offerts, ~1000 fetches)
2. Token : Console → Settings → Integrations
3. Dans `.env` :
   ```
   APIFY_TOKEN=apify_api_...
   ```

Sans Apify, les skills demandent de coller le texte manuellement.

### Pour le pilier outreach (LaTeX CV)

```bash
# pdflatex doit être installé pour builder les CVs adaptés
# Windows : MiKTeX (https://miktex.org)
# Mac     : MacTeX (https://www.tug.org/mactex/)
# Linux   : apt install texlive-full

# Créer le dossier profil
mkdir -p profile/cv_builds

# Copier le template CV et le remplir
cp profile/cv.template.tex profile/cv.tex
```

---

## Structure du projet

```
job-hunting-skills/
│
├── docs/
│   ├── GOAL.md              # Vision et roadmap du projet
│   └── prompts.md           # Architecture et principes
│
├── profile/
│   ├── profile.json         # Tes préférences, stack, localisations cibles
│   ├── cv.tex               # CV source en LaTeX (modulaire, max 1 page)
│   └── cv_builds/           # PDFs générés par adaptation (gitignored)
│
├── skills/
│   ├── linkedin-post-writer/
│   ├── linkedin-comment-drafter/
│   ├── linkedin-humanizer/
│   ├── linkedin-hook-extractor/
│   ├── linkedin-content-planner/
│   ├── linkedin-reply-handler/
│   ├── linkedin-thread-monitor/
│   ├── linkedin-engager-analytics/
│   ├── linkedin-profile-optimizer/
│   ├── linkedin-employee-advocacy/
│   └── linkedin-outreach/       # <- à construire (Phase 2)
│
├── lib/
│   ├── apify_client.py      # Lecture LinkedIn via Apify
│   ├── publora_client.py    # Publication via Publora
│   ├── approval.py          # Carte d'approbation standardisée
│   ├── backend_selector.py  # Router tier 0/1/2
│   └── url_parser.py        # Parsing URLs LinkedIn → URNs
│
├── scripts/
│   ├── build_cv.py          # pdflatex wrapper + vérification 1 page
│   └── post_comment.py      # Post commentaire approuvé
│
├── references/
│   ├── voice-rules.md       # Règles de voix LinkedIn (canoniques)
│   ├── hook-formulas.md     # 10 formules de hook éprouvées
│   ├── algorithm-heuristics.md  # Heuristiques algo LinkedIn 2026
│   ├── industry-benchmarks.md   # Benchmarks engagement
│   └── engagement-metrics-taxonomy.md
│
├── agents/
│   ├── orchestrator.md      # Logique d'orchestration end-to-end
│   ├── job-scorer.md        # Instructions agent de scoring
│   └── cv-adapter.md        # Instructions agent d'adaptation CV
│
├── SKILL.md                 # Router principal (entry point)
├── .env.example             # Variables d'environnement
└── requirements.txt         # requests, python-dotenv (3 packages)
```

---

## Profil utilisateur

Crée `profile/profile.json` :

```json
{
  "personal": {
    "name": "Ton Nom",
    "email": "toi@example.com",
    "phone": "+33 6 00 00 00 00",
    "linkedin_url": "https://linkedin.com/in/ton-handle",
    "location": "Paris, France"
  },
  "preferences": {
    "seniority": "senior",
    "remote": "remote",
    "locations": ["Paris", "Remote", "Europe"],
    "company_types": ["startup", "scale_up"],
    "avoid": ["consulting", "ESN"],
    "salary_target_eur": 85000
  },
  "stack": {
    "must_have": ["python", "sql"],
    "strong": ["spark", "dbt", "langchain", "fastapi", "docker", "kafka"],
    "nice_to_have": ["go", "databricks", "rag"],
    "avoid": ["php", "wordpress"]
  },
  "cv_variants": {
    "data_engineer": "profile/cv_builds/cv_data_engineer.pdf",
    "genai_engineer": "profile/cv_builds/cv_genai.pdf"
  }
}
```

---

## Roadmap

| Phase | Statut | Ce que ça apporte |
|---|---|---|
| Content (10 skills) | Opérationnel | Posts, commentaires, profil, analytics |
| Outreach manuel | En cours | Candidatures spontanées sur cibles connues |
| Auto-discovery | Planifié | L'agent trouve les entreprises selon le profil |
| Matching d'offres | Planifié | Scorer les offres LinkedIn/Greenhouse vs profil |
| Application auto | Long terme | Soumission via playwright-cli avec confirmation |

---

## Principes

**Draft-first, approbation humaine toujours.** Rien n'est publié, envoyé, ou soumis sans confirmation explicite.

**L'agent génère, les scripts font l'I/O.** Tout le contenu est rédigé par l'agent courant. Les scripts gèrent uniquement : appels API Apify/Publora, build PDF LaTeX. Aucun appel LLM dans les scripts.

**Ancrage réel.** Les messages d'outreach sont toujours ancrés dans un élément concret de l'entreprise cible (post récent, stack annoncé, actualité). Pas de messages génériques.

**1 page max.** Le CV adapté ne dépasse jamais une page. Le build script échoue si c'est le cas.

---

## Références

- [docs/GOAL.md](docs/GOAL.md) — Vision complète et roadmap
- [docs/prompts.md](docs/prompts.md) — Architecture et principes détaillés
- [references/voice-rules.md](references/voice-rules.md) — Règles de voix
- [Publora API](https://docs.publora.com) — Documentation publication
- [Apify console](https://console.apify.com) — Gestion tokens et acteurs
