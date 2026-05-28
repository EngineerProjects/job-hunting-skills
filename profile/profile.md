# Profile — Stéphane KPOVIESSI

Agent context file. Read this entirely before any outreach session.
This is the single source of truth for all personalization decisions.

---

## Personal

| Field | Value |
|---|---|
| Name | Stéphane KPOVIESSI |
| Email | oastephanekpoviessi@gmail.com |
| Phone | +33 7 48 59 47 13 |
| Location | Île-de-France (Cergy) |
| LinkedIn | https://linkedin.com/in/stephanekpoviessi |
| GitHub | https://github.com/EngineerProjects |
| Portfolio | https://kpoviessi-stephane.vercel.app |

---

## Current situation

- **Title**: Data & AI Engineer
- **Status**: En fin de formation ingénieur (diplôme JUNIA ISEN 2026), disponible
- **Notice period**: immédiat
- **Distinction**: Major de promotion sur toute la durée du cycle préparatoire

---

## Job preferences

| Preference | Value |
|---|---|
| Target roles | Data Engineer, Data & AI Engineer, AI/ML Engineer |
| Seniority | Junior à Mid (première expérience significative Allianz + projets perso solides) |
| Work mode | Remote preferred, hybrid accepté Île-de-France |
| Contract | CDI preferred, alternance possible |
| Salary | À définir selon poste |
| Open to relocation | Non (Île-de-France) |
| Message language | auto (FR pour boites françaises, EN pour international/remote) |

**Target company types**: startup, scale-up, tech companies orientées data ou IA
**Avoid**: ESN, SSII, consulting pur sans produit, grands groupes très hiérarchiques

---

## Technical stack

### Languages
Python, SQL, Go, C (bases)

### Data Engineering
PySpark, Airflow, ETL/ELT, Architecture Médaillon (Bronze/Silver/Gold),
PostgreSQL, Pandas, Parquet, Azure DataLake, dbt, Hadoop (notions)

### AI / GenAI
LangChain, LangGraph, RAG, pgvector, systèmes multi-agents, orchestration LLM,
MCP (Model Context Protocol), embeddings, vector databases

### Machine Learning
PyTorch, GANs, Computer Vision (PIL, OpenCV), scikit-learn, MLflow (notions),
deep learning, modélisation prédictive

### Backend & Infra
FastAPI, gRPC, SSE (Server-Sent Events), Docker, Git, Linux,
AWS, Azure, Databricks, GORM, SQLite, Redis

### Frontend (secondaire)
React, TypeScript, Electron

### Visualization
Power BI, Streamlit, Matplotlib

### Avoid
PHP, WordPress, Ruby, COBOL, ABAP

---

## CV tag mapping

Tags used in `profile/cv.tex` to select bullets per target:

| Tag | When to use |
|---|---|
| `@data_engineer` | Rôles data eng, pipelines, ETL, architecture data, Spark, Airflow |
| `@genai` | Rôles LLM, agents, RAG, orchestration IA, AI engineering |
| `@llm` | LLM-specific (subset de @genai) |
| `@rag` | RAG-specific (subset de @genai) |
| `@ml_engineer` | PyTorch, GANs, Computer Vision, feature engineering, model training |
| `@backend` | Go, APIs, Docker, cloud infra, gRPC, SSE |
| `@cost` | Réduction de coûts, automation, gains mesurables, optimisation |
| `@leadership` | Mentoring, ownership technique, documentation, cross-team |

---

## Work experience (full detail)

### Data Engineer — Allianz France
**Période**: Novembre 2025 – Avril 2026 (stage)
**Lieu**: Courbevoie, Paris
**Contexte**: Migration end-to-end d'un DataMart Assurance, d'un environnement legacy SAS vers une architecture moderne PySpark/Azure.

**Réalisations clés:**
- Rétro-ingénierie et documentation de plus de **15 000 lignes de code SAS** (19 fichiers complexes) pour garantir la conservation complète de la logique métier
- Conception et implémentation d'une **architecture Médaillon** (Bronze / Silver / Gold) scalable couvrant portefeuilles, capitaux et émissions
- Développement de **pipelines PySpark modulaires** couvrant **3 flux critiques** avec **150+ règles de gestion métier**
- Pipeline de **contrôle qualité** sur données de localisation : validation GPS, reconstitution d'adresses, détection d'anomalies métier
- Stratégie de validation : tests de parité fonctionnelle SAS/Python, validation automatique de schémas
- Refonte de la logique de validation d'adresse pour réduire les faux positifs et améliorer la fiabilité du reporting

**Stack**: Python 3.9+, PySpark, SAS, SQL, Parquet, Git, Architecture Médaillon, Azure DataLake, Databricks, Pandas

---

### Machine Learning Engineer — Groupe Sylvagreg
**Période**: Mai 2024 – Août 2024 (stage)
**Lieu**: Lille
**Contexte**: Développement d'une solution de génération et d'impression 3D à partir d'images 2D par IA.
**Repos**: [Sylva3D](https://github.com/EngineerProjects/sylva3D) · [Sylva3DGUI](https://github.com/EngineerProjects/Sylva3dGUI)

**Réalisations clés:**
- Analyse approfondie de l'état de l'art en reconstruction 3D (photogrammétrie, deep learning)
- Sélection et benchmark d'algorithmes IA pour la génération de modèles 3D
- Conception, implémentation et optimisation de **modèles GANs** avec PyTorch pour améliorer précision géométrique et robustesse
- Pipelines de prétraitement et d'augmentation de données (PIL, computer vision)
- Pipeline complet image 2D → modèle 3D exploitable pour impression
- Application desktop Python pour la visualisation et l'interaction
- Déploiement de workflows Computer Vision sur **AWS**
- Documentation technique complète de l'architecture et des choix techniques

**Stack**: Python, PyTorch, PIL, Computer Vision, GANs, Modélisation 3D, Photogrammétrie, AWS, Docker

---

### Analyste de Données Commerciales — Lyne et Frères SARL
**Période**: Juin 2022 – Août 2022 (stage)
**Lieu**: Bénin
**Contact référence**: ICOUTCHIKA Jean-Marc Salomon Dègnon (lyneetfreressarl@gmail.com)

**Réalisations:**
- Analyse des données historiques de ventes, livraisons et commandes par produit/client/pays
- Identification des produits, marchés et périodes les plus rentables
- Analyse de la chaîne d'approvisionnement : transport, délais, coûts logistiques
- Segmentation clients, identification des meilleurs clients, recommandations produits
- Dashboards Power BI et rapports analytiques ad hoc

**Stack**: Python, Power BI, Data Analysis

---

## Projects (full list)

### Nexus AI — AI Operating System
**GitHub**: https://github.com/EngineerProjects/Nexus_ai
**Description**: Plateforme expérimentale conçue comme un véritable "AI Operating System". Permet à des agents IA autonomes de collaborer, exécuter des outils, gérer des workflows complexes et maintenir une mémoire persistante.

**Fonctionnalités:**
- Orchestration multi-agents
- Mémoire persistante et RAG
- Gestion des permissions et sandboxing
- Streaming temps réel via SSE
- Architecture modulaire basée sur des skills/plugins
- Communication gRPC et API REST
- Sessions persistantes
- Intégration MCP (Model Context Protocol)
- Interface desktop moderne (Electron + React)

**Stack**: Go, gRPC, PostgreSQL, SQLite, GORM, React, Electron, TypeScript, RAG, Vector Databases, SSE, MCP

---

### Tech Watch Agent — Multi-Agent AI Research Platform
**GitHub**: https://github.com/EngineerProjects/tech-watch-agent
**Description**: Plateforme autonome de veille technologique multi-agents. Recherche automatisée, agrégation de sources, analyse et génération de rapports structurés.

**Fonctionnalités:**
- Recherche automatisée multi-sources (GitHub, Reddit, arXiv, YouTube)
- Pipelines RAG, synthèses IA structurées
- Génération automatique de rapports
- Veille continue programmable
- Notifications et envoi par email
- Sessions persistantes

**Stack**: Python, FastAPI, LangGraph, PostgreSQL, pgvector, Redis, Docker, React, TypeScript, SearXNG

---

### BI Retail Solution — Data Pipeline & BI
**GitHub**: https://github.com/EngineerProjects/BI_Retail
**Description**: Pipeline ETL retail complet avec orchestration, stockage, dashboards et reporting automatisé.

**Stack**: Python, Airflow, PostgreSQL, Power BI, Docker

---

### Sylva3D — 3D Engine / Procedural Forest Simulation
**GitHub**: https://github.com/EngineerProjects/sylva3D
**Description**: Moteur 3D explorant la génération procédurale d'environnements naturels et la simulation environnementale temps réel.

**Stack**: Python, OpenGL, Rendering 3D, Mathématiques 3D, Simulation procédurale

---

### Sylva3D GUI — Desktop Interface for Sylva3D
**GitHub**: https://github.com/EngineerProjects/Sylva3dGUI
**Description**: Interface desktop moderne pour interagir avec l'écosystème Sylva3D. Visualisation temps réel et contrôle de scènes 3D.

**Stack**: Python, GUI Frameworks, 3D Visualization

---

### PulseStudio — Creative AI Platform
**GitHub**: https://github.com/EngineerProjects/PulseStudio
**Description**: Plateforme expérimentale créative combinant IA, automatisation, traitement multimédia et workflows interactifs.

**Stack**: Python, AI Workflows, Interactive Systems

---

### Advanced Football Video Analysis — Computer Vision for Sports
**GitHub**: https://github.com/EngineerProjects/Advanced-Football-Video-Analysis
**Description**: Système de computer vision pour l'analyse automatique de séquences vidéo football : détection d'objets, tracking, analyse de mouvements.

**Stack**: Python, OpenCV, Computer Vision, Deep Learning, Video Processing

---

### Solar Irradiance Forecasting — ML for Renewable Energy
**GitHub**: https://github.com/EngineerProjects/solar-forecasting
**Description**: Prévision de l'irradiance solaire à partir de données météorologiques pour améliorer la gestion photovoltaïque.

**Stack**: Python, Scikit-Learn, Pandas, Machine Learning, Forecasting Models

---

### LocalIngest — LLM Repository Ingestion Tool
**GitHub**: https://github.com/EngineerProjects/LocalIngest
**Description**: Outil CLI/TUI développeur qui analyse automatiquement une codebase locale et génère des rapports Markdown optimisés pour les workflows LLM et RAG.

**Stack**: Python, CLI/TUI, Rich, Typer, Markdown Generation

---

### Shop App Service — E-Commerce Backend
**GitHub**: https://github.com/EngineerProjects/Shop-app-service
**Description**: Backend orienté services pour applications e-commerce. Modularité, APIs et gestion transactionnelle.

**Stack**: Python, Backend APIs, Databases, Service Architecture

---

### SAM Background Remover — AI Image Segmentation
**GitHub**: https://github.com/EngineerProjects/sam_background_remover
**Description**: Suppression automatique de fond par segmentation d'images avec des modèles modernes de computer vision.

**Stack**: Python, Computer Vision, Image Segmentation, Deep Learning

---

## Education

### Diplôme d'Ingénieur — Big Data & Data Science
**École**: JUNIA ISEN Lille
**Période**: 2023 – 2026
**Spécialisation**: Data Engineering, Machine Learning, IA, bases de données SQL/NoSQL, mathématiques appliquées, visualisation

---

### Licence — Électronique
**École**: JUNIA ISEN Rabat
**Période**: 2020 – 2023
**Contenu**: Algorithmique, programmation C, systèmes embarqués, mathématiques appliquées, traitement du signal, physique

---

### Cycle Préparatoire
**École**: Marie Stella
**Période**: 2020 – 2022
**Distinction**: **Major de promotion sur l'ensemble des années préparatoires**
**Contenu**: Mathématiques avancées, physique, chimie, sciences de l'ingénieur, algorithmique

---

## Target companies

### Manual targets

| Company | LinkedIn | Notes |
|---|---|---|
| Mistral AI | https://linkedin.com/company/mistral-ai | Stack LLM, Paris |
| Hugging Face | https://linkedin.com/company/huggingface | Open source AI, remote-friendly |
| Dataiku | https://linkedin.com/company/dataiku | Data platform, Paris |

### Auto-discovery parameters

- **Enabled**: yes
- **Locations**: Paris, Île-de-France, France (remote)
- **Industries**: Technology, Artificial Intelligence, Software Development, FinTech
- **Company size**: 11-50, 51-200, 201-500
- **Max per session**: 5

---

## Outreach settings

| Setting | Value |
|---|---|
| Max applications per session | 5 |
| Follow-up delay | 7 days |
| Cooldown before re-contacting same company | 30 days |
| Log file | `profile/outreach_log.json` |

---

## CV

| Field | Value |
|---|---|
| Source | `profile/cv.tex` |
| Builds directory | `profile/cv_builds/` |
| Max pages | 1 |

---

## Notes for the agent

**Sur Nexus AI**: projet phare, le plus ambitieux techniquement. AI OS from scratch en Go avec Electron+React. GitHub public. Mentionner pour des rôles AI Engineering, backend Go, ou systèmes distribués.

**Sur l'expérience Allianz**: contexte grand groupe mais stack moderne (PySpark, Azure, architecture Médaillon). Le chiffre clé : 15 000+ lignes de SAS migrées, 150+ règles métier. Transférable à n'importe quelle boite data.

**Sur le diplôme**: en cours (fin 2026). Dire "en fin de formation ingénieur" ou "diplôme d'ingénieur 2026" — pas "étudiant".

**Sur le Major de promotion**: à mentionner pour des boites qui valorisent le background académique ou dans des messages où on veut montrer la rigueur.

**Sur Lyne et Frères**: stage Bénin 2022, très tôt dans le parcours. Ne mentionner que si la boite a des opérations en Afrique de l'Ouest ou valorise explicitement la diversité.

**Sur les langues**: Yoruba, Fon, Goun sont des langues natives d'Afrique de l'Ouest (Bénin). Pertinent uniquement si l'entreprise a un angle géographique Afrique ou diversité.

**Stack Go**: Go est utilisé sur Nexus AI en production (gRPC, SSE, backend haute perf). Ce n'est pas "notions" — c'est un projet complet en production.

**Profil hybride**: Stéphane couvre data engineering classique (Allianz) ET AI engineering avancé (Nexus, Tech Watch Agent). Pour les boites qui cherchent les deux, c'est le message à faire passer.
