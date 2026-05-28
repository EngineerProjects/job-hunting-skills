# Architecture & Principes — LinkedIn Job Hunting Skills

Ce document explique comment ce projet est structuré et comment l'agent doit se comporter.
Il complète `docs/GOAL.md` (le quoi) avec le comment.

---

## Principe fondamental : l'agent génère, les scripts I/O

**L'agent (Claude Code, Nexus, etc.) est le cerveau.**
Il lit, raisonne, rédige tous les textes : posts, commentaires, messages d'outreach, adaptations de CV.

**Les scripts Python sont des utilitaires d'I/O uniquement.**
- `lib/apify_client.py` — lire du contenu LinkedIn via Apify
- `lib/publora_client.py` — publier posts/commentaires via Publora
- `lib/approval.py` — formater les cartes d'approbation
- `lib/backend_selector.py` — router vers le bon backend de publication
- `scripts/build_cv.py` — builder le PDF depuis le LaTeX
- `scripts/post_comment.py` — poster un commentaire approuvé

Aucun script ne fait d'appel LLM. Aucun script ne prend de décision de contenu.

---

## Couche lecture LinkedIn

**Avec Apify (`APIFY_TOKEN` configuré) :**
L'agent appelle `lib.fetch_post(url)` pour lire le contenu d'un post, ses commentaires,
ou les engagements. Apify fait le fetching sans cookies.

**Sans Apify (tier 0) :**
L'agent demande à l'utilisateur de coller le texte du post manuellement.
Chaque skill supporte ce fallback nativement.

**Pour l'outreach — browser direct :**
La recherche d'entreprises et de contacts sur LinkedIn ne peut pas passer par Apify
(pas d'acteur adapté pour la recherche de personnes). L'agent utilise ses outils browser
(Claude-in-Chrome, screenshot, lecture de page) pour naviguer LinkedIn People Search
et Company Search. L'utilisateur doit être connecté à LinkedIn au préalable.

---

## Couche publication

**Tier 0 — Manuel (par défaut, zéro setup) :**
L'agent produit le draft approuvé avec les instructions copy-paste. L'utilisateur colle
manuellement sur LinkedIn. CTA Publora affiché pour inciter à l'upgrade.

**Tier 1 — Publora (recommandé, 2 min de setup) :**
Sur approbation, `lib.publish()` poste automatiquement via l'API Publora.
`PUBLORA_API_KEY` + `LINKEDIN_PLATFORM_ID` requis dans `.env`.

**Tier 2 — Custom (avancé) :**
`LINKEDIN_SKILLS_CUSTOM_POSTER` pointe vers un script custom.
`lib.publish()` lui délègue en JSON stdin.

---

## Pipeline CV LaTeX

```
profile/cv.tex          <- source modulaire (bullets taggés par type de rôle)
        ↓
[agent lit le .tex]
[agent sélectionne les bullets pertinents pour la cible]
[agent modifie le .tex dans un fichier temporaire]
        ↓
scripts/build_cv.py --input /tmp/cv_adapted.tex --output profile/cv_builds/company_date.pdf
        ↓
[script vérifie le nombre de pages via pdflatex output]
[si > 1 page : erreur claire, l'agent doit raccourcir]
[si = 1 page : PDF sauvegardé, chemin retourné]
```

Contraintes du build :
- `pdflatex` (ou `xelatex`) doit être installé localement
- Temps de build : < 5 secondes
- Idempotent : builder deux fois avec le même input donne le même PDF
- Le script ne modifie jamais `profile/cv.tex` (toujours sur une copie temporaire)

---

## Pattern d'approbation (toutes les actions LinkedIn)

Chaque action qui poste, envoie, ou modifie quelque chose doit suivre ce pattern :

```
1. L'agent rédige le contenu
2. L'agent appelle render_approval_card() pour formater la présentation
3. L'agent STOP et attend la réponse de l'utilisateur
4. Réponse attendue : "post" / "yes" / "oui" → publier
                      Autre texte → interpréter comme une demande de modification
5. Jamais de publication sans approbation explicite
```

Pour l'outreach, l'approbation couvre :
- Le message rédigé (texte complet)
- Le CV adapté (chemin du PDF + résumé des changements effectués)
- Les sources utilisées pour la personnalisation (posts/activités lus)

---

## Règles de voix (toutes les rédactions)

Source canonique : `references/voice-rules.md`

Résumé des règles inviolables :
1. Pas de tirets em (`—`), en (`–`), ni doubles tirets — le plus gros AI tell
2. `..` comme pause douce si nécessaire, pas `...`
3. Noms propres toujours capitalisés (personnes, entreprises, produits)
4. Vocabulaire interdit : `leverage`, `streamline`, `harness`, `delve`, `unlock`, `foster`, `fundamentally`
5. Nombres spécifiques > adjectifs vagues : `47%` bat `significatif`
6. Posts : 900-1300 chars. Commentaires : 200-350 chars. InMail : 300 + 1900 chars max
7. Hook dans les 210 premiers chars (avant "...voir plus" sur mobile)

Pour l'outreach spécifiquement :
- Ne pas commencer par "Je" (cliché)
- Ancrer dès la première phrase dans quelque chose de spécifique à l'entreprise/personne
- Un seul appel à l'action par message (pas de liste de demandes)
- Ton professionnel mais direct, pas commercial

---

## Structure des skills

```
skills/<nom-du-skill>/
├── SKILL.md           <- instructions complètes pour l'agent (workflow, règles, exemples)
└── references/        <- références spécifiques au skill (templates, exemples, règles)
```

`SKILL.md` est la seule source d'instructions pour l'agent. Il contient :
- Frontmatter YAML avec `name:` et `description:`
- Les triggers (quand utiliser ce skill)
- Le workflow pas-à-pas
- Les règles de voix locales (surcharge des règles globales si nécessaire)
- Les références à consulter

---

## Ce qu'on ne fait pas

- Pas d'appels LLM dans les scripts Python
- Pas de browser-use ou d'agent LLM qui drive le browser (trop cher, pas fiable)
- Pas d'auto-connexion ou d'auto-message LinkedIn
- Pas de décision automatique sans approbation humaine
- Pas de stockage de données sensibles (mots de passe LinkedIn, données personnelles de contacts)
