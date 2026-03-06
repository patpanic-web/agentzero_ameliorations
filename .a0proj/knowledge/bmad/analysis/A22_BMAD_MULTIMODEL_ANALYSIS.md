# 🔍 Analysis — A22 : BMAD Personas Multi-Model

> Date : 2026-03-06 | Analyst : Business Analyst BMAD | Statut : 🔄 EN COURS

---

## 📌 Contexte & Besoin

**Constat** : Actuellement, tous les personas BMAD (BA, PM, Architect, Developer, QA, Scrum) utilisent le même LLM (claude-sonnet-4.6) avec les mêmes outils disponibles. Or :
- Certaines phases (Analysis, Planning) nécessitent surtout du raisonnement léger
- D'autres (Solutioning, Implementation) nécessitent un LLM puissant
- La liste d'outils complète est chargée pour TOUTES les phases → surcoût tokens systématique

**Besoin exprimé** : Assigner un LLM optimal + liste d'outils filtrés à chaque persona BMAD.

---

## 🎯 Critères de Succès

- [ ] Chaque persona BMAD utilise le LLM le plus adapté à son rôle
- [ ] La liste d'outils est réduite selon la phase active
- [ ] Impact mesuré : réduction coût tokens par session ≥ 30%
- [ ] Solution compatible No-Core-Change
- [ ] Activation/désactivation sans rupture de service

---

## ❓ Questions de Découverte

1. **LLM disponibles** : Quels modèles sont actuellement configurés dans Agent Zero ? (openrouter, local ?)
2. **Contrôle modèle** : La sélection de LLM par phase est-elle faisable sans modifier le core ?
3. **Seuil rentabilité** : À partir de combien de sessions/mois l'économie justifie-t-elle l'effort (~10h) ?
4. **Risques** : Que se passe-t-il si le LLM léger fait une erreur en phase Analysis ? Repli possible ?
5. **Scope** : Concerne-t-il tous les projets ou uniquement les projets BMAD Niveau 2 ?
6. **Filtrage outils** : Le filtrage doit-il être automatique (basé sur la phase) ou manuel (PO décide) ?

---

## 🔗 Dépendances

- A17 (ToolRegistry Filter) — reporté, mais potentiellement nécessaire pour le filtrage d'outils
- Configuration `agents.json` du projet
- Profils BMAD dans `BMAD_PERSONAS.md`

---

## ⚠️ Risques Identifiés

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| LLM léger insuffisant en Analysis | Moyen | Haut | Fallback au LLM principal configurable |
| Complexité d'implémentation >10h | Moyen | Moyen | Décomposer en sous-tâches |
| Incompatibilité No-Core-Change | Faible | Critique | Vérifier avant solutioning |

---

## 📋 Livrables Attendus

- Matrice LLM × Phase × Outils
- PoC de sélection de modèle par phase
- Rapport coût/bénéfice chiffré

