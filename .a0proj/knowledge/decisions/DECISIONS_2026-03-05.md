# 📋 Décisions Validées — Session 2026-03-05

## Phase 1 (Analysis) — Validées par PO

| # | Décision | Date |
|---|----------|------|
| D1 | P8 (Docker MCP désactivé) retiré — choix intentionnel PO | 2026-03-05 |
| D2 | LLM par agent = axe séparé (A5), modifications manuelles par PO uniquement | 2026-03-05 |
| D3 | Catégorisation Global (A1-A5,A7) vs Projet (A6,A8-A10) confirmée | 2026-03-05 |
| D4 | Gouvernance projet à 2 niveaux : Léger (tous) / BMAD complet (sur décision PO) | 2026-03-05 |
| D5 | Non-négociable PO : Backlog priorisé + Statut avancement par tâche | 2026-03-05 |
| D6 | Choix du niveau de gouvernance : PO décide, agent peut suggérer | 2026-03-05 |
| D7 | Priorité #1 = Comportement correct AVANT optimisation tokens | 2026-03-05 |
| D8 | Claude Opus maintenu comme modèle Agent0 — contrôle manuel PO | 2026-03-05 |
| D9 | Approche No-Core-Change stricte — configs, prompts, modules uniquement | 2026-03-05 |

## Axes d'amélioration identifiés

### Axe GLOBAL (indépendant du contexte projet)
| # | Axe | Impact |
|---|-----|--------|
| A1 | Override solving.md → delegate-first | 🔴 MAJEUR |
| A2 | Override call_sub.md → MUST delegate | 🔴 MAJEUR |
| A3 | Enrichir profil Hacker (8 lignes → complet) | 🔴 HAUT |
| A4 | Renforcer rôle orchestrateur Agent0 | 🟡 HAUT |
| A5 | Documentation LLM par agent (config simple, modifiable) | 🟡 MOYEN |
| A7 | Rigueur documentation/backlog | 🟢 MOYEN |

### Axe PROJET (contextuel : actif si projet, inactif sinon)
| # | Axe | Impact |
|---|-----|--------|
| A6 | Corriger Git MCP default path | 🟡 MOYEN |
| A8 | Gouvernance Git dans prompts projet | 🔴 HAUT |
| A9 | git_url renseigné dans project.json | 🟡 MOYEN |
| A10 | Gouvernance projet Niveau 1/2 (template) | 🔴 HAUT |

## Modèle de Gouvernance Projet

### Niveau 1 — Léger (TOUS les projets)
- Backlog priorisé (BACKLOG.md)
- Statut avancement par tâche
- Git/GitHub actif (init, commits, push)
- Décisions documentées (DECISIONS.md)
- Activé automatiquement à la création du projet

### Niveau 2 — BMAD Complet (sur décision PO)
- Tout le Niveau 1 +
- 4 phases BMAD (Analysis → Planning → Solutioning → Implementation)
- PO décide à la création, agent peut suggérer
