# 📔 Journal des Décisions - Agent-Zero: Modular Optimizer

> **Dernière mise à jour :** 2026-03-04

---

## 🏗️ Architecture Décisionnelle

Ce journal trace toutes les décisions techniques importantes prises dans le cadre du projet.

---

## Décision #001: Structure BMAD pour Documentation Persistante

| Champ | Valeur |
|-------|--------|
| **Date** | 2026-03-04 |
| **Statut** | ✅ Adoptée |
| **Décideur** | Product Owner |
| **Contexte** | Besoin d'un état des lieux exhaustif persistant entre conversations |

### Problème
Le contexte de conversation est perdu entre sessions, rendant difficile le suivi de l'avancement du projet.

### Options Considérées
1. **Mémoire Agent-Zero** - Limitée, contextuelle
2. **Fichiers Markdown structurés** - Persistant, versionnable, accessible
3. **Base de données** - Overkill pour le besoin

### Décision
Adoption de **fichiers Markdown structurés selon BMAD** dans le dossier `knowledge/`.

### Justification
- Approche méthodologique éprouvée (BMAD)
- Fichiers persistants et versionnables
- Accessible par tout agent sans contexte préalable
- Structure claire en 4 phases

### Conséquences
- Création de la structure de dossiers BMAD
- Documentation systématique des décisions
- Mise à jour continue de l'état des lieux

---

## Décision #002: Utilisation de MCP Servers

| Champ | Valeur |
|-------|--------|
| **Date** | Pré-existante |
| **Statut** | ✅ Adoptée |

### Décision
Utilisation de serveurs MCP (Model Context Protocol) pour l'extension des capacités d'Agent-Zero.

### MCP Installés
- Tavily (recherche web)
- Playwright (automatisation navigateur)
- Git (versioning)
- Docker (conteneurs)
- System Diagnostics (monitoring)

---

## 📌 Template pour Nouvelle Décision

```markdown
## Décision #XXX: [Titre]

| Champ | Valeur |
|-------|--------|
| **Date** | YYYY-MM-DD |
| **Statut** | Proposée/Adoptée/Rejetée |
| **Décideur** | Qui a pris la décision |

### Problème
[Description du problème]

### Options Considérées
1. **Option A** - Description
2. **Option B** - Description

### Décision
[Décision finale]

### Justification
[Raisons]

### Conséquences
[Impacts]
```

---

## Décision #003: Stratégie Multi-Modèles et Délégation Active

| Champ | Valeur |
|-------|--------|
| **Date** | 2026-03-04 |
| **Statut** | ✅ Adoptée - En attente d'implémentation |
| **Décideur** | Product Owner (sur recommandation Agent 0) |
| **Source** | Analyse comparative + Recherche web validée |

### Problème
1. Agent 0 a tendance à exécuter les tâches lui-même plutôt que déléguer
2. Pas d'optimisation des coûts via modèles économiques pour les subordonnés
3. Prompts de délégation passifs ("can delegate" vs "must delegate")

### Options Considérées

1. **Option A : Rester sur GLM-5 uniquement**
   - Coût actuel : ~$1.48/1M tokens
   - Avantage : Simple, économique
   - Inconvénient : Pas d'optimisation, qualité variable

2. **Option B : Migrer vers Claude Sonnet uniquement**
   - Coût : ~$7.00/1M tokens (4.7x plus cher)
   - Avantage : Meilleure qualité
   - Inconvénient : Coût élevé sans délégation

3. **Option C : Architecture Multi-Modèles avec Délégation Active** (RECOMMANDÉE)
   - Coût estimé : $0.83-1.51/1M tokens selon niveau de délégation
   - Avantage : Qualité supérieure + coût optimisé
   - Inconvénient : Complexité setup initial

### Décision
Adoption de l'**Option C : Architecture Multi-Modèles avec Délégation Active**.

### Allocation des Modèles
| Profil | Modèle | Usage |
|--------|--------|-------|
| Agent 0 | GLM-5 (actuel) ou Claude Sonnet | Orchestration, raisonnement |
| Developer | DeepSeek V3.2 | Code, tests, boilerplate |
| Hacker | Gemini 2.0 Flash | Sécurité, scripts |
| Researcher | DeepSeek V3.2 | Recherche, documentation |

### Justification
1. **Économies documentées** : 57-80% de réduction en production (sources : Infralovers, BusinessPlusAI)
2. **Performance validée** : DeepSeek V3 supérieur de 30.7% à Claude 3 Sonnet sur benchmarks
3. **Standard industriel** : Multi-modèle = architecture standard 2025
4. **Approche non-intrusive** : Modifie prompts/settings, pas le code source

### Conséquences
- Création de `settings.json` pour chaque profil subordonné
- Modification des prompts Agent 0 pour délégation active
- Documentation de réversibilité obligatoire
- Mesure des coûts avant/après requise

### Contraintes Spécifiques
- ⚠️ **Préserver la configuration existante** : Ne pas recréer les agents de 0
- ⚠️ **Modifier le comportement** : Agir sur les prompts et settings uniquement

### Références
- Analyse détaillée : `knowledge/solutions/ANALYSE_MULTI_MODEL_STRATEGY.md`
- Backlog : `knowledge/backlog/BACKLOG.md` (Tâche #1)

---

---

## Décision #004: Analyse des Optimisations MCP (Lazy Loading, Caching, etc.)

| Champ | Valeur |
|-------|--------|
| **Date** | 2026-03-04 |
| **Statut** | 📋 EN ATTENTE DE VALIDATION |
| **Décideur** | Product Owner (recommandation Agent 0) |
| **Source** | Recherche web approfondie + Audit technique local |

### Problème
Optimisation de la consommation de tokens et de la qualité des réponses dans Agent-Zero via des solutions non-intrusives (No-Core-Change).

### Analyse Effectuée
1. **Recherche web approfondie** sur l'état de l'art 2025
2. **Audit technique** du code Agent-Zero (fichiers MCP)
3. **Évaluation de faisabilité** et compatibilité

### Optimisations Identifiées

| # | Optimisation | Source | Impact | Risque |
|---|--------------|--------|--------|--------|
| 1 | Tool Description Augmenter | arXiv 2025 | +25% qualité | Faible |
| 2 | Lazy MCP Tool Loading | GitHub Anthropic #11364, LinkedIn | -47% tokens | Moyen (Goose) |
| 3 | MCP Response Caching | Fast.io, Tim Kellogg | -80% latence | Moyen |
| 4 | AGENTS.md Generator | OpenAI AAIF | Portabilité | Faible |

### Risque Critique Documenté
**Goose (Block) a supprimé leur "Tool Selection Strategy"** après échec avec embeddings locaux.
- Leçon: Le lazy loading basé sur classification intention peut échouer.

### Audit Technique Local
- Fichier clé: `/a0/python/extensions/system_prompt/_10_system_prompt.py`
- Ligne 55: `get_tools_prompt()` charge TOUS les outils MCP
- Architecture compatible avec extension (pas de core change)

### Recommandation
1. **Priorité 1**: Tool Description Augmenter (faible risque)
2. **Priorité 2**: Lazy MCP Tool Loading (avec tests robustes)
3. **Priorité 3**: MCP Caching (attendre stabilisation pattern)
4. **Priorité 4**: AGENTS.md (optionnel pour distribution externe)

### Fichiers Créés
- `knowledge/bmad/analysis/OPTIMISATIONS_MCP_2025.md` - Analyse complète

### Conséquences
- Ajout au BACKLOG des tâches d'implémentation
- Tests de faisabilité requis avant implémentation Lazy Loading

### Références
- GitHub Anthropic Issue #11364
- arXiv: "MCP Tool Descriptions Are Smelly" (2025)
- Fast.io: "MCP Server Caching"
- OpenAI: AGENTS.md Standard

### Validation Requise
- [ ] Ordre des priorités validé
- [ ] Tests de faisabilité demandés
- [ ] Risque Goose accepté/refusé

---
\n| D1772735935 | Création du skill 'project-governance' avec structure complète (SKILL.md + script + 10 templates) | 2026-03-05 | Skill créé pour initialiser la gouvernance projet à 2 niveaux : niveau 1 (Backlog + Git + Decisions) et niveau 2 (BMAD 4 phases) |

## D9 — LLM principal : changement manuel PO (2026-03-05)
**Décision :** Le PO a changé manuellement le LLM principal de claude-opus à claude-sonnet-4.6 pour réduire les coûts.
**Règle :** Le choix du modèle LLM est sous contrôle exclusif du PO. L'agent ne doit pas le signaler comme incohérence.

---

## Décision #010: Désactivation MCP Git

| Champ | Valeur |
|-------|--------|
| **Date** | 2026-03-06 |
| **Statut** | ✅ Adoptée |
| **Décideur** | Product Owner |

### Problème
Le MCP Git injecte ~500 tokens de descriptions d'outils dans chaque prompt système, même quand il n'est pas utilisé. L'agent utilise le terminal git (code_execution_tool) pour 100% des opérations Git, rendant le MCP superflu.

### Options Considérées
1. **Garder le MCP Git** — Sécurité théorique, surcoût tokens constant
2. **Désactiver le MCP Git** — Économie tokens, pas de perte fonctionnelle

### Décision
Désactivation du MCP Git (`"disabled": true` dans settings.json).

### Justification
- Économie de ~500 tokens par requête LLM
- 100% des opérations Git couvertes par le terminal
- Aligné avec le principe : "Si un outil n'apporte pas un gain mesurable, il doit être écarté"
- Le PO ne vérifie pas les commits manuellement — le MCP n'apportait pas de sécurité réelle

### Réactivation si besoin
```json
// Dans settings.json > mcpServers > git
"disabled": false  // ou supprimer la clé
```
