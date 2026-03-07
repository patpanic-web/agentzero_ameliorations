# Sprint 12 — Rapport de Clôture
**Date** : 2026-03-07
**Tâche** : A27 — Refonte Architecture behaviour.md — ADN Global + Projet

## Contexte
Le PO a identifié que plusieurs règles comportementales critiques n'étaient pas capturées
dans les fichiers toujours actifs, notamment :
- Zéro Supposition (toujours vérifier avant d'affirmer)
- Clôture Sprint obligatoire avec E2E + audit couverture + go/no-go
- JIT bmad-process (checklist fin de sprint)
- D11 surcharges non destructives
- Protocole Anti-Destructeur (audit avant implémentation)

De plus, il n'existait pas de behaviour.md global (hors projet), laissant Agent Zero
sans règles comportementales dans les sessions non-projet.

## Livrables Implémentés

### M1 — behaviour.md GLOBAL créé
- Fichier : `/a0/usr/memory/default/behaviour.md`
- Taille : 3 700 bytes
- Blocs : 6 (Memory Security, Proactive, Robustness, Zero Supposition, Capture Idées, JIT Personas)
- S'applique : toutes sessions, tous contextes, hors projet

### M2 — behaviour.md PROJET enrichi
- Fichier : `.a0proj/memory/behaviour.md`
- Taille : 6 516 bytes (avant : 3 898 bytes)
- Blocs : 12 (6 originaux + 6 nouveaux)
- Nouveaux blocs : Workflow BMAD JIT, Clôture Sprint, No-Core-Change,
  Règle D11, Protocole Anti-Destructeur

### M3 — Checklist Fin de Sprint enrichie
- Fichier : `/a0/usr/skills/bmad-process/SKILL.md`
- Taille : 5 248 bytes
- Ajout : Étape 1 (Tests E2E), Étape 2 (Audit Couverture), Étape 3 (Go/No-Go)
- Règle : séquence NON NÉGOCIABLE avant toute annonce de clôture

### M4 — Template behaviour.md + init-governance.sh
- Template : `/a0/usr/skills/project-governance/templates/niv1/memory/behaviour.md`
  (5 562 bytes, 10 blocs : règles globales + blocs projet génériques)
- Script : `init-governance.sh` enrichi pour créer `.a0proj/memory/behaviour.md` auto
- Impact : tout nouveau projet hérite automatiquement de l'ADN comportemental

### M5 — Surcharges developer/researcher (vérification D11)
- Résultat : déjà conformes D11 (original EN PREMIER + Operational Context EN DESSOUS)
- developer : 14 967b original + 508b ajout = 15 475b ✅
- researcher : 15 421b original + 508b ajout = 15 929b ✅
- Aucune correction nécessaire

## Tests E2E — 7/7 PASS

| Test | Résultat | Détail |
|------|----------|--------|
| T1 behaviour.md global | ✅ PASS | 3 700 bytes, 6 blocs détectés |
| T2 behaviour.md projet | ✅ PASS | 6 516 bytes, 12 blocs détectés |
| T3 Checklist E2E bmad-process | ✅ PASS | E2E + Audit + Go/No-Go présents |
| T4 Template project-governance | ✅ PASS | 5 562 bytes |
| T5 init-governance.sh | ✅ PASS | memory/behaviour.md dans le script |
| T6 Persistance /a0/usr/ | ✅ PASS | 4 fichiers dans volumes montés |
| T7 Règle Zéro Supposition | ✅ PASS | Présente dans behaviour global |

## Audit de Couverture — Règles Sprint 12

| Règle | Avant Sprint 12 | Après Sprint 12 |
|-------|----------------|----------------|
| R4 Zéro Supposition | ❌ Absente | ✅ behaviour global + projet |
| R10 Clôture Sprint E2E | ❌ Absente | ✅ behaviour projet + bmad-process |
| R11 JIT bmad-process | ❌ Absente | ✅ behaviour global + projet |
| R12 D11 Non-Destructif | ⚠️ JIT seulement | ✅ behaviour projet (toujours actif) |
| R13 Audit avant Implémentation | ⚠️ JIT seulement | ✅ behaviour projet (toujours actif) |
| Behaviour hors projet | ❌ Absent | ✅ /a0/usr/memory/default/behaviour.md |
| Nouveau projet behaviour auto | ❌ Non créé | ✅ project-governance template |

## Verdict Go/No-Go

**✅ GO** — Sprint 12 validé.

Toutes les règles comportementales critiques sont désormais capturées dans les fichiers
toujours actifs. L'ADN comportemental d'Agent Zero est persistant et robuste peu importe
le contexte (hors projet ou dans un projet).
