# Goal — LinkedIn Job Hunting Skills

## Ce qu'on construit

Un skill suite LinkedIn pour ingénieurs Data/AI/GenAI en recherche active ou passive d'opportunités.

Basé sur un fork de [linkedin-skills](https://github.com/sergebulaev/linkedin-skills), ce projet garde **tous les outils de création de contenu** existants et y ajoute un **pilier outreach** : identifier des contacts pertinents dans des entreprises cibles, adapter le CV en LaTeX, et rédiger des candidatures spontanées personnalisées basées sur l'activité réelle de l'entreprise.

---

## Les deux piliers

### Pilier 1 — Content (hérité de linkedin-skills, intact)

Créer une présence LinkedIn régulière et professionnelle pour augmenter la visibilité passive.

| Skill | Ce qu'il fait |
|---|---|
| `linkedin-post-writer` | Rédige des posts viraux selon les heuristiques 2026 |
| `linkedin-comment-drafter` | Commente des posts de managers/recruteurs cibles |
| `linkedin-reply-handler` | Répond aux commentaires sur ses propres posts |
| `linkedin-humanizer` | Supprime les AI tells avant publication |
| `linkedin-hook-extractor` | Analyse des posts viraux pour extraire les formules |
| `linkedin-content-planner` | Planifie une semaine de contenu cohérente |
| `linkedin-thread-monitor` | Suit les réponses d'auteurs à ses propres commentaires |
| `linkedin-engager-analytics` | Analyse qui a liké/commenté un post (segmentation) |
| `linkedin-profile-optimizer` | Audite et réécrit le profil LinkedIn |
| `linkedin-employee-advocacy` | Coordination de contenu pour équipes (secondaire) |

### Pilier 2 — Outreach (nouveau, à construire)

Envoyer des candidatures spontanées personnalisées directement à des managers et recruteurs, sans passer par les ATS.

**Workflow cible :**

```
1. CIBLAGE
   Cibles manuelles  : liste d'entreprises fournie directement par l'utilisateur
   Auto-discovery    : l'agent cherche des entreprises sur LinkedIn par localisation,
                       secteur, taille, selon le profil utilisateur

2. RECHERCHE
   Pour chaque cible : lire l'activité LinkedIn récente (posts, actualités publiées)
   Identifier les contacts pertinents : recruteurs, managers techniques, VP
   Comprendre ce que l'entreprise met en avant en ce moment

3. ADAPTATION DU CV
   Source LaTeX (.tex), modulaire — bullets annotés par pertinence (data_engineer, genai, etc.)
   L'agent sélectionne les bullets/sections pertinents pour ce contexte précis
   Build via pdflatex (déterministe, scriptable)
   Contrainte absolue : 1 page maximum, même après adaptation
   PDF sauvegardé dans profile/cv_builds/{company}_{role}_{date}.pdf

4. RÉDACTION DU MESSAGE
   Ancré dans un élément réel : post récent de la cible, stack annoncé, actualité entreprise
   Ton adapté selon le profil du contact (recruteur vs manager technique vs VP)
   Format : InMail (300 chars sujet + 1900 chars corps) ou DM direct (1900 chars)
   Le CV adapté est référencé / disponible en pièce jointe

5. VALIDATION HUMAINE
   L'agent présente tout : message rédigé + CV adapté + sources de recherche utilisées
   L'utilisateur relit, modifie si besoin, approuve
   L'utilisateur envoie manuellement sur LinkedIn (jamais auto-envoyé)
```

---

## Le CV LaTeX — principes de design

Le `.tex` est la source de vérité. Il doit être **modulaire** :

- Chaque bullet de chaque expérience est annoté par type de rôle
  (`data_engineer`, `genai_engineer`, `backend`, etc.)
- L'agent peut choisir les bullets pertinents sans couper au hasard
- La mise en page est conçue pour tenir en 1 page quelles que soient
  les modifications de contenu (marges fixes, tailles de polices fixées)
- `scripts/build_cv.py` wrap pdflatex, vérifie le nombre de pages,
  et échoue clairement si > 1

---

## Roadmap par phases

### Phase 1 — Content (opérationnel dès maintenant)
Les 10 skills hérités de linkedin-skills fonctionnent sans modification.

### Phase 2 — Outreach sur cibles manuelles
L'utilisateur fournit une liste d'entreprises. L'agent recherche les contacts,
adapte le CV, rédige le message. Pas encore d'auto-discovery.

### Phase 3 — Auto-discovery
L'agent cherche lui-même des entreprises sur LinkedIn selon le profil
(localisation, secteur, stack). Complète les cibles manuelles.

### Phase 4 — Matching d'offres
Ingérer des offres d'emploi (LinkedIn Jobs, Greenhouse, Lever),
scorer leur match avec le profil, préparer le dossier complet.

### Phase 5 — Application automatisée (long terme)
L'agent remplit et soumet les candidatures via playwright-cli.
L'utilisateur confirme avant envoi.

---

## Ce qu'on ne construit PAS pour l'instant

- Pas d'envoi automatique de messages ou de connexions LinkedIn
- Pas de scraping ATS en masse (Greenhouse/Lever batch)
- Pas de dashboard PostgreSQL de suivi de pipeline
- Pas de configuration de LLM provider : le skill s'exécute dans l'agent courant

---

## Profil utilisateur cible

Ingénieur senior en Data/AI/GenAI, recherche active ou passive, ciblant :
- Paris / Ile-de-France, Remote France/Europe
- Startups et scale-ups tech (pas du conseil, pas de grands groupes)
- Stack : Python, SQL, Spark, dbt, LangChain/LangGraph, FastAPI, Docker, Kafka
