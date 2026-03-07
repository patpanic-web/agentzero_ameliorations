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

- En début de session, lis TOUJOURS le backlog (`knowledge/backlog/BACKLOG.md`) pour identifier l'état du projet
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


## 🔍 Checklist Début de Planification Sprint (A7)

> **Déclencher AVANT toute proposition de sprint — même en cours de session.**

- [ ] Backlog relu (`knowledge/backlog/BACKLOG.md`) — statuts à jour ?
- [ ] Tâches TERMINÉES depuis la dernière relecture bien marquées ?
- [ ] Nouvelles tâches / idées PO ajoutées au backlog ?
- [ ] Priorités reflètent les décisions récentes du PO ?
- [ ] Dépendances entre tâches vérifiées ?

**Règle :** Ne jamais proposer un sprint sans avoir relu le backlog dans la même session ou confirmé qu'il est à jour.

## 📝 Leçon Apprise (2026-03-06)

**Erreur type :** Proposer un sprint basé sur une vision mémorisée du backlog sans relire le fichier réel.

**Correction :** Toujours lire `BACKLOG.md` avant de proposer un sprint, même si le backlog a été lu en début de session — il a pu être modifié entre-temps.

## 📝 Leçon Apprise (2026-03-07) — Méthodologie Surcharges Profils

**Erreur commise (A19/Sprint 7) :** Surcharges developer et researcher créées de façon destructive :
- Langue changée (EN → FR)
- Contenu original perdu (15k bytes remplacés par 600 bytes)
- Style non respecté

**Règle établie (D11) :** Toute surcharge de profil DOIT :
1. Copier l'original intégralement en premier
2. Ajouter du contenu EN DESSOUS uniquement
3. Respecter la langue et le style de l'original
4. Principe fondamental : **amélioration par AJOUT, jamais par recréation totale**

**Vérification obligatoire avant toute surcharge :**
- [ ] Ai-je lu l'original dans `/a0/agents/{profil}/prompts/` ?
- [ ] La surcharge commence-t-elle par une copie intégrale de l'original ?
- [ ] Les ajouts sont-ils dans la même langue et le même style ?
- [ ] La taille du fichier de surcharge est-elle >= taille de l'original ?
