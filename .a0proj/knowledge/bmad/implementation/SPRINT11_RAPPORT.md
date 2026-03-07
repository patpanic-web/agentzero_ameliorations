# Sprint 11 — Rapport : Modularisation BMAD (A26)

> **Date** : 2026-03-07
> **Sprint** : 11 — "La Modularisation"
> **Taches** : A26 (complète)
> **Statut** : TERMINE

## Objectif du Sprint

Refonte complète de l'architecture BMAD dans Agent Zero :
- Modularisation des personas et du workflow via skills JIT
- Enrichissement de behaviour.md avec 4 règles clés
- Nettoyage des incohérences (skill fantôme, instructions trop longues)
- Création du BACKLOG_GLOBAL.md pour les idées hors projet

## Modifications Implémentées

| # | Modification | Commit | Gain |
|---|-------------|--------|------|
| M1 | behaviour.md +4 blocs | e09fe97 | Comportement global amélioré |
| M2 | project.json nettoyé | d4ae0f6 | Suppression skill fantôme bmad-method |
| M3 | BMAD_PERSONAS.md supprimé | 679d953 | -9 863 bytes/req |
| M4 | BMAD_PROCESS.md → BMAD_CORE.md (489b) | bce9363 | -3 576 bytes/req |
| M5 | /a0/usr/skills/bmad-personas créé | hors git | +8 personas JIT |
| M6 | /a0/usr/skills/bmad-process créé | hors git | +workflow JIT |
| M7 | /a0/usr/BACKLOG_GLOBAL.md créé | hors git | +capture idées |

## Résultats

### Gain tokens
- **Avant** : 13 962 bytes injectés à chaque requête dans le projet
- **Après** : 489 bytes (BMAD_CORE.md) + personas chargés uniquement si besoin
- **Économie** : -13 473 bytes/req sur ~80% des échanges

### Architecture résultante
```
instructions/
  ├── BMAD_CORE.md    (489b — toujours injecté)
  └── GIT_GOVERNANCE.md

/a0/usr/skills/
  ├── bmad-personas/  (12 402b — JIT via skills_tool)
  ├── bmad-process/   (4 416b — JIT via skills_tool)
  ├── project-governance/
  └── self-audit/

/a0/usr/
  └── BACKLOG_GLOBAL.md  (idées hors projet)
```

## Découvertes Notables

1. **behaviour.md n'était pas tracké par Git** (.gitignore excluait .a0proj/memory/) → Corrigé : exception ajoutée dans .gitignore
2. **BMAD officiel moins riche que notre custom** → Bonne décision de garder notre base et d'enrichir
3. **JIT natif dans A0 via skills** → Architecture élégante sans modification du core

## Vélocité
- Tâches complétées : 1 (A26, scope majeur)
- Commits : 5 commits individuels propres
- Durée réelle : ~2h (estimé 4h)

## Prochaines Priorités (backlog)
Voir BACKLOG.md pour les tâches suivantes.
