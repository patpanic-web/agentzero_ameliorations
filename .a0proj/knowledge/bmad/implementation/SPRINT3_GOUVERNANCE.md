# 🔄 Sprint 3 — "La Gouvernance" — Implémentation
> Date : 2026-03-05
> Statut : ✅ TERMINÉ

## Objectif
Mettre en place la gouvernance Git et les templates de gouvernance projet.

## Fichiers Créés

### A8 — Gouvernance Git dans prompts projet

#### GIT_GOVERNANCE.md (NOUVEAU)
- **Fichier :** `/a0/usr/projects/agentzero_ameliorations/.a0proj/instructions/GIT_GOVERNANCE.md`
- **Mécanisme :** Injection automatique dans le system prompt via le mécanisme `instructions/*.md`
- **Contenu :** 14 lignes — Règles Git concises :
  - Commit par livrable (fin de tâche/sprint)
  - Conventional Commits (feat:, fix:, docs:, chore:)
  - Push après chaque commit
  - Branche main uniquement
  - Workflow en 4 étapes
- **Rollback :** `rm .a0proj/instructions/GIT_GOVERNANCE.md`

### A10 — Template gouvernance projet Niv.1/2

#### Skill project-governance (NOUVEAU)
- **Dossier :** `/a0/usr/skills/project-governance/`
- **Composants :**
  - `SKILL.md` — Documentation et instructions du skill
  - `scripts/init-governance.sh` — Script d'initialisation (exécutable)
  - `templates/niv1/` — Templates Niveau 1 (léger)
    - `instructions/GIT_GOVERNANCE.md`
    - `knowledge/backlog/BACKLOG.md`
    - `knowledge/decisions/DECISIONS.md`
  - `templates/niv2/` — Templates Niveau 2 (BMAD, additif)
    - `instructions/BMAD_PROCESS.md`
    - `knowledge/bmad/{analysis,planning,solutioning,implementation}/README.md`

#### Fonctionnement
- **Niv.1 (défaut)** : `bash init-governance.sh /path/to/project`
- **Niv.2 (BMAD)** : `bash init-governance.sh /path/to/project bmad`
- Le script ne remplace jamais les fichiers existants (idempotent)
- Activation : Niv.1 par défaut, Niv.2 si PO mentionne "bmad"

- **Rollback :** `rm -rf /a0/usr/skills/project-governance/`

## Vérification
- Persistance : ✅ Tous les fichiers dans /a0/usr/ (volume Docker monté)
- No-Core-Change : ✅ Aucun fichier core modifié
- Réversibilité : ✅ Suppression simple pour rollback
- Tests : ✅ Script testé en Niv.1 et Niv.2 (création + idempotence)

## Métriques

| Composant | Fichiers créés | Lignes totales |
|-----------|---------------|----------------|
| A8 (GIT_GOVERNANCE.md) | 1 | 14 |
| A10 (skill project-governance) | 10 | ~120 |
| Documentation Sprint 3 | 2 | ~50 |
| **Total** | **13** | **~184** |
