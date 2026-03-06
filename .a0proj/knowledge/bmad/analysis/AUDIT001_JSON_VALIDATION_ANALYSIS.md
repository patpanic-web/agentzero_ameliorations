# 🔍 Analysis — AUDIT-001 : Améliorer la validation JSON des réponses

> Date : 2026-03-06 | Analyst : Business Analyst BMAD | Statut : 🔄 EN COURS
> Source : Skill self-audit (A21) — 21 erreurs de formatage JSON détectées

---

## 📌 Contexte & Besoin

**Constat** : Le self-audit a détecté 21 erreurs de formatage JSON dans les réponses d'Agent Zero. Ces erreurs provoquent des interruptions de traitement, des retries inutiles et une consommation de tokens supplémentaire.

**Besoin** : Mettre en place une validation JSON pré-envoi pour réduire ces erreurs à zéro.

---

## 🎯 Critères de Succès

- [ ] Réduction des erreurs JSON à < 5% du taux actuel
- [ ] Solution No-Core-Change uniquement
- [ ] Pas d'augmentation notable de la latence
- [ ] Mesurable via le prochain self-audit

---

## ❓ Questions de Découverte

1. **Nature des erreurs** : S'agit-il d'erreurs de parsing JSON (syntaxe) ou de validation de schéma (champs manquants) ?
2. **Origine** : Ces erreurs viennent-elles de l'agent principal (agent0) ou des subordinates ?
3. **Contexte déclencheur** : Dans quelles situations ces erreurs se produisent-elles le plus souvent ? (réponses longues, tool calls, délégation ?)
4. **Logs disponibles** : Le self-audit a-t-il conservé des exemples précis des erreurs ?
5. **Solution existante** : Y a-t-il déjà un mécanisme de retry JSON dans le framework ?

---

## 🔗 Dépendances

- Skill self-audit (A21) — source des données
- Logs de session Agent Zero
- Potentiellement : prompt override pour renforcer les instructions JSON

---

## ⚠️ Risques

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| Erreurs non reproductibles | Moyen | Moyen | Analyser les logs bruts |
| Solution intrusive nécessaire | Faible | Critique | Si No-Core-Change impossible → reporter |

---

## 📋 Livrables Attendus

- Rapport des types d'erreurs JSON (avec exemples)
- Solution No-Core-Change proposée
- Critère de mesure du succès

