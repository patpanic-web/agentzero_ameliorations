# 🔍 Analysis — AUDIT-002 : Tool Registry Awareness Enhancement

> Date : 2026-03-06 | Analyst : Business Analyst BMAD | Statut : 🔄 EN COURS
> Source : Skill self-audit (A21) — 23 erreurs d'outils inconnus détectées

---

## 📌 Contexte & Besoin

**Constat** : Le self-audit a détecté 23 appels à des outils inconnus ou indisponibles. Les agents appellent des outils qui n'existent pas dans leur contexte actuel, ce qui génère des erreurs et des retries coûteux.

**Besoin** : Améliorer la conscience des agents quant aux outils disponibles dans leur contexte.

---

## 🎯 Critères de Succès

- [ ] Réduction des appels à des outils inconnus à < 3
- [ ] Les agents savent toujours quels outils sont disponibles
- [ ] Solution No-Core-Change
- [ ] Mesurable via le prochain self-audit

---

## ❓ Questions de Découverte

1. **Quels outils** : Quels outils sont appelés à tort ? (outils supprimés ? outils de profils différents ?)
2. **Qui appelle** : Agent principal ou subordinates ?
3. **Lien avec A18** : Les suppressions Playwright/SysDiag ont-elles contribué à ces erreurs ?
4. **Lien avec A17** : Le ToolRegistry Filter reporté est-il la bonne solution ici ?
5. **Fréquence** : Ces 23 erreurs sont-elles concentrées ou distribuées ?

---

## 🔗 Dépendances

- A17 (ToolRegistry Filter) — potentiellement lié
- A18 (suppression MCPs Playwright+SysDiag) — peut être source d'erreurs
- Skill self-audit (A21)

---

## ⚠️ Risques

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| Nécessite A17 (effort 2h) | Moyen | Moyen | Évaluer solution plus légère |
| Erreurs dues à des agents legacy | Faible | Faible | Nettoyer les instructions obsolètes |

---

## 📋 Livrables Attendus

- Liste des outils appelés à tort (avec contexte)
- Lien ou non avec A17
- Proposition de correction (prompt override ou ToolRegistry)

