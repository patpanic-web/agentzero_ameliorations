# 🔍 Analysis — AUDIT-004 : Optimiser la gestion des timeouts

> Date : 2026-03-06 | Analyst : Business Analyst BMAD | Statut : 🔄 EN COURS
> Source : Skill self-audit (A21) — 17 erreurs de timeout détectées

---

## 📌 Contexte & Besoin

**Constat** : Le self-audit a détecté 17 erreurs de timeout. Ces erreurs interrompent les tâches et génèrent des retries coûteux.

**Besoin** : Ajuster les valeurs de timeout ou implémenter une gestion asynchrone pour éviter ces erreurs.

---

## 🎯 Critères de Succès

- [ ] Réduction des timeouts de ≥ 70%
- [ ] Solution No-Core-Change
- [ ] Pas de dégradation des performances pour les tâches rapides
- [ ] Mesurable via le prochain self-audit

---

## ❓ Questions de Découverte

1. **Source des timeouts** : Outils MCP, appels LLM, outils terminal, ou browser ?
2. **Valeurs actuelles** : Quels sont les timeouts configurés actuellement ?
3. **Modifiables sans core-change ?** : Les timeouts sont-ils dans des fichiers de config accessibles ?
4. **Pattern** : Les timeouts touchent-ils toujours les mêmes types de tâches ?
5. **Lien avec suppression MCPs** : La suppression de Playwright/SysDiag (A18) a-t-elle réduit ou déplacé les timeouts ?

---

## 🔗 Dépendances

- A18 (suppression MCPs) — impact potentiel sur les timeouts
- Configuration `settings.json` du framework
- AUDIT-003 (retry loops) — les timeouts peuvent déclencher des boucles

---

## ⚠️ Risques

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| Timeouts dans le core (non modifiable) | Moyen | Haut | Identifier les timeouts configurables |
| Augmenter timeout = augmenter latence | Moyen | Moyen | Timeout adaptatif selon la tâche |

---

## 📋 Livrables Attendus

- Inventaire des timeouts par type (MCP, LLM, terminal)
- Liste des timeouts modifiables sans core-change
- Recommandation de valeurs optimales

