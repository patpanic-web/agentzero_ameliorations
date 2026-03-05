# 📋 BACKLOG — Améliorations Agent-Zero
> Dernière mise à jour : 2026-03-05 (Sprint 3 clôturé)

## 📁 AXE PROJET — Gouvernance & Git/GitHub

### A8 — Gouvernance Git dans prompts projet
- **Objectif** : Injecter automatiquement les règles Git dans le system prompt via le mécanisme `instructions/*.md`
- **Statut** : ✅ TERMINÉ (Sprint 3)
- **Fichier** : `instructions/GIT_GOVERNANCE.md`
- **Livrable** : Règles Git concises (14 lignes) : commit par livrable, Conventional Commits, push après commit, branche main uniquement, workflow en 4 étapes

### A10 — Template gouvernance projet Niv.1/2
- **Objectif** : Créer un skill `project-governance` avec templates pour initialiser la gouvernance des projets
- **Statut** : ✅ TERMINÉ (Sprint 3)
- **Skill** : `/a0/usr/skills/project-governance/`
- **Livrable** : SKILL.md + script d'initialisation + templates Niv.1 (léger) et Niv.2 (BMAD)
### A12 — Backlog SSOT + checklist fin de sprint
- **Objectif** : Déclarer le backlog comme source de vérité unique (SSOT) et ajouter une checklist de fin de sprint
- **Statut** : ✅ TERMINÉ (Sprint 3)
- **Fichier** : `instructions/BMAD_PROCESS.md`
- **Livrable** : Règles SSOT + checklist ajoutées aux instructions BMAD


## 📋 Tableau de Suivi des Tâches Actives

### A13 — Instruction bootstrap session
- **Objectif** : Ajouter une instruction pour que l'agent lise le backlog en début de session
- **Statut** : ✅ TERMINÉ (Sprint 3)
- **Fichier** : `instructions/BMAD_PROCESS.md`
- **Livrable** : 1 ligne ajoutée dans section SSOT

| ID | Title | Priority | Impact | Effort | Status |
|----|-------|----------|--------|--------|--------|
| T1 | Créer skill 'project-governance' avec templates de gouvernance à 2 niveaux | 🔴 P1 | 🔴 HIGH | ⏱️ 1h | ✅ DONE |

## 📊 Legend
- 📋 TODO | 🔄 IN PROGRESS | ✅ DONE | ⏸️ DEFERRED | ❌ DROPPED
- 🔴 P0 = Critical | 🔴 P1 = High | 🟡 P2 = Medium | 🟢 P3 = Low

## 🏆 Sprints Complétés

- **Sprint 1** (2026-03-04) : "Fondation" — Création structure projet, découverte mécanismes A0, premières overrides
- **Sprint 2** (2026-03-05) : "Les Profils" — A3 (hacker) + A4 (orchestrator) + A9 (Tool Registry filter) + skill bmad-method
- **Sprint 3** (2026-03-05) : "La Gouvernance" — A8 + A10 (git governance + project templates)
