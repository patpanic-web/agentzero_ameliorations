# 🔍 Sprint 3 — "La Gouvernance" — Analyse
> Date : 2026-03-05
> Phase : Analysis (validée par PO)

## Objectif
Mettre en place la gouvernance Git et les templates de gouvernance projet.

## Tâches
- A8 : Gouvernance Git dans prompts projet (🔴 P1)
- A10 : Template gouvernance projet Niv.1/2 (🔴 P1)

## Découverte technique

### Mécanisme d'injection des instructions projet
- `project.json["instructions"]` + fichiers `.a0proj/instructions/*.md` → concaténés et injectés dans `{{project_instructions}}`
- Fichiers triés alphabétiquement → contrôle d'ordre possible avec préfixes numériques
- Variable `{{project_git_url}}` disponible dans les templates de prompt

### Constat terrain
- Git actif sur le projet, remote GitHub configuré
- Sprint 2 n'avait pas été commité → preuve du besoin A8
- Le fichier BMAD_PROCESS.md dans instructions/ est déjà injecté automatiquement

## Décisions PO (validées 2026-03-05)

| # | Question | Décision PO |
|---|----------|-------------|
| D10 | Granularité commits | Par livrable (fin de tâche) |
| D11 | Convention messages | Conventional Commits courts (feat:, fix:, docs:, chore:) |
| D12 | Push | Après chaque commit (décision technique agent) |
| D13 | Branches | Travailler sur main directement |
| D14 | Format template A10 | Fichier instructions + skill Agent Zero |
| D15 | Contenu Niv.1 | Backlog + Git + Décisions (confirmé) |
| D16 | BMAD_PROCESS.md | Bon tel quel, pas de modification |
| D17 | Activation niveau | Niv.1 par défaut, Niv.2 si PO mentionne "bmad" |

## Solution retenue

### A8 — Fichier d'instructions Git
- Créer `.a0proj/instructions/GIT_GOVERNANCE.md`
- Contenu : règles de commit, convention, push, dans un format minimal
- Injection automatique via le mécanisme existant

### A10 — Template gouvernance
- Créer un skill `project-governance` avec :
  - Template Niv.1 (structure de base : backlog, décisions, git)
  - Template Niv.2 (Niv.1 + BMAD complet avec structure knowledge/bmad/)
  - Instructions d'utilisation
