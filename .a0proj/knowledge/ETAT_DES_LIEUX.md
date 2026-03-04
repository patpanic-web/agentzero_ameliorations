# 📊 État des Lieux - Agent-Zero: Modular Optimizer

> **Dernière mise à jour :** 2026-03-04

---

## 🎯 Vision du Projet

Ce projet vise à améliorer les performances du framework Agent-Zero via une approche **strictement non-intrusive** (No-Core-Change).

### Objectifs principaux
- ⚡ Exécution plus rapide
- 🎯 Précision accrue
- 📉 Réduction drastique de la consommation de tokens

### Principes fondamentaux
| Principe | Description |
|----------|-------------|
| **No-Core-Change** | Interdiction de modifier le code source d'Agent-Zero |
| **Modularité** | Solutions "à la carte" activables/désactivables facilement |
| **Réversibilité** | Chaque amélioration doit être désactivable sans impact |
| **Audit Continu** | Justification obligatoire de la consommation de tokens |

---

## 🔒 Instructions du Product Owner

### Règles de Travail
| Règle | Description |
|--------|-------------|
| **Sous-agents** | Obligation d'utiliser les sous-agents pour maximiser l'efficacité |
| **Arbitrage** | Aucune décision d'arbitrage sans approbation du PO |
| **VPS** | Accès root disponible - NE PAS modifier la structure de fichiers core |
| **Agent Zero Core** | Interdiction formelle de modifier la structure de fichiers d'Agent Zero |

### Contraintes de Modification
| Fichier/Structure | Action |
|-------------------|--------|
| `/a0/agents/` | ❌ INTERDIT - Core Agent Zero |
| `/a0/prompts/` | ❌ INTERDIT - Core Agent Zero |
| `/a0/usr/agents/` | ✅ AUTORISÉ - Overrides utilisateur |
| `/a0/usr/prompts/` | ✅ AUTORISÉ - Overrides utilisateur |
| `/a0/usr/settings.json` | ✅ AUTORISÉ - Configuration globale |
| **VPS structure** | ❌ INTERDIT - Ne pas modifier |

### Approche de Modification
- **Jamais** créer de fichiers "from scratch" pour remplacer
- **Toujours** analyser les fichiers existants avant modification
- **Privilégier** les modifications intelligentes et incrementales
- **Documenter** chaque changement pour réversibilité

---

## 📁 Structure du Projet

```
/a0/usr/projects/agentzero_ameliorations/
├── screenshots/                    # Captures d'écran
└── .a0proj/
    ├── knowledge/                   # Documentation persistante
    │   ├── main/                     # Fichiers principaux
    │   │   ├── MCP_INSTALLES.md      # Inventaire des MCP
    │   │   └── TACHE_INSTALLATION_MCP.md
    │   ├── bmad/                     # Phases BMAD
    │   │   ├── analysis/             # Phase 1: Analyse
    │   │   ├── planning/             # Phase 2: Planning
    │   │   ├── solutioning/          # Phase 3: Solution
    │   │   └── implementation/       # Phase 4: Implémentation
    │   ├── backlog/                  # Backlog des tâches
    │   ├── decisions/                # Journal des décisions
    │   ├── solutions/                # Solutions proposées
    │   └── fragments/                # Fragments de code/idées
    ├── memory/                       # Mémoire vectorielle
    └── project.json                   # Configuration projet
```

---

## 📦 MCP Actuellement Installés

Voir détail dans `knowledge/main/MCP_INSTALLES.md`

| MCP | Status | Usage |
|-----|--------|-------|
| Tavily (Web Search) | ✅ Actif | Recherche web agentique |
| Playwright | ✅ Actif | Automatisation navigateur |
| Git | ✅ Actif | Opérations Git |
| Docker | ✅ Actif | Gestion conteneurs |
| System Diagnostics | ✅ Actif | Diagnostic système |

---

## 🤖 Configuration des Modèles Actuelle

| Rôle | Modèle | Provider | Usage |
|------|--------|----------|-------|
| **Agent 0** | z-ai/glm-5 | OpenRouter | Orchestration principale |
| **Utilitaire** | meta-llama/llama-4-scout | OpenRouter | Tâches utilitaires |
| **Browser** | deepseek/deepseek-v3.2 | OpenRouter | Automatisation navigateur |
| **Embedding** | all-MiniLM-L6-v2 | HuggingFace | Vecteurs mémoire |

---

## 📊 Phase BMAD Actuelle

**Phase en cours :** `IMPLEMENTATION` (Tâche #1: Multi-Modèles)

---

## 🔗 Liens Rapides

- [Backlog](./backlog/BACKLOG.md)
- [Décisions](./decisions/DECISIONS.md)
- [Analyse BMAD](./bmad/analysis/README.md)
