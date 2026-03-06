# 🔍 Analysis — AUDIT-003 : Réduire les boucles de retry/répétition

> Date : 2026-03-06 | Analyst : Business Analyst BMAD | Statut : 🔄 EN COURS
> Source : Skill self-audit (A21) — 39 patterns de retry/loop détectés

---

## 📌 Contexte & Besoin

**Constat** : Le self-audit a détecté 39 patterns de retry ou de boucle dans les sessions. C'est le problème le plus fréquent identifié. Ces boucles consomment des tokens inutilement et peuvent bloquer les tâches.

**Besoin** : Implémenter une logique de retry plus intelligente avec backoff ou abandon rapide.

---

## 🎯 Critères de Succès

- [ ] Réduction des patterns retry/loop de ≥ 50%
- [ ] Les agents abandonnent après N tentatives avec un message clair au PO
- [ ] Solution No-Core-Change
- [ ] Mesurable via le prochain self-audit

---

## ❓ Questions de Découverte

1. **Types de loops** : S'agit-il de retries sur erreur outil, boucles de raisonnement, ou répétition de tâche ?
2. **Seuil actuel** : Y a-t-il déjà un mécanisme de limite de retries dans A0 ?
3. **Impact utilisateur** : L'agent se bloque-t-il ou continue-t-il quand même ?
4. **Déclencheurs** : Quels types de tâches déclenchent le plus de loops ?
5. **Solution prompt** : Un renforcement des instructions ("après 2 échecs, escalader au PO") suffit-il ?

---

## 🔗 Dépendances

- AUDIT-001 (erreurs JSON) — certains loops sont probablement dus aux erreurs JSON
- AUDIT-002 (outils inconnus) — certains loops viennent d'outils introuvables
- Prompt override `solving.md` (A1)

---

## ⚠️ Risques

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| Loops intentionnels confondus avec erreurs | Moyen | Moyen | Distinguer retry-erreur vs retry-logique |
| Fix trop agressif bloque des tâches légitimes | Faible | Haut | Seuil configurable |

---

## 📋 Livrables Attendus

- Classification des 39 patterns (type, fréquence, contexte)
- Proposition de règle de retry (prompt override)
- Seuil de retry recommandé

