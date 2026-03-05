# 📋 Instructions BMAD - Processus de Travail

> **Règle d'or :** Toujours suivre les 4 phases BMAD avant toute action technique.

---

## 🔴 RÈGLE FONDAMENTALE

**JAMAIS de solution avant d'avoir compris le problème !**

### Comportement Correct

1. **L'utilisateur demande une tâche** → Ajouter au BACKLOG
2. **Phase Analysis** → Documenter le besoin dans `knowledge/bmad/analysis/`
3. **Phase Planning** → Prioriser et structurer
4. **Phase Solutioning** → Choisir la solution
5. **Phase Implementation** → Exécuter

### Comportement Incorrect ❌

- Essayer de résoudre immédiatement
- Passer directement à l'implémentation
- Ignorer les questions de découverte

---

## 📂 Fichiers à Mettre à Jour

| Action | Fichier |
|--------|----------|
| Nouvelle tâche | `knowledge/backlog/BACKLOG.md` |
| Analyse | `knowledge/bmad/analysis/TACHE_XXX.md` |
| Décision | `knowledge/decisions/DECISIONS.md` |
| Solution | `knowledge/solutions/SOLUTION_XXX.md` |

---

## 🎯 Checklist Avant Action

- [ ] Ai-je identifié la phase BMAD en cours ?
- [ ] Ai-je documenté le besoin dans le backlog ?
- [ ] Ai-je posé les questions de découverte ?
- [ ] Ai-je validé avec l'utilisateur avant de continuer ?

---

## 📌 Backlog = Source de Vérité Unique (SSOT)

- Le backlog (`knowledge/backlog/BACKLOG.md`) est la référence absolue de l'état du projet
- Toute décision impactant une tâche → mise à jour immédiate du backlog
- Toute nouvelle information (scope, priorité, dépendance) → refléter dans le backlog

## ✅ Checklist Fin de Sprint

- [ ] Tâches du sprint marquées TERMINÉ dans le backlog
- [ ] Revue complète du backlog : toutes les tâches restantes sont-elles toujours exactes ?
- [ ] Décisions prises pendant le sprint reflétées dans les descriptions/priorités du backlog
- [ ] Rapport de sprint créé dans `knowledge/bmad/implementation/`
- [ ] Commit et push

## 📝 Leçon Apprise (2026-03-04)

**Erreur commise :** J'ai essayé de résoudre le problème Chrome au lieu de simplement l'ajouter au backlog.

**Correction :** Toujours ajouter la tâche au backlog d'abord, puis demander des clarifications.

