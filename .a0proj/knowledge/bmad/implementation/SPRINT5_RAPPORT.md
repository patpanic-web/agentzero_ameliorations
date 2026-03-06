# 📋 Sprint 5 — Rapport de clôture
**Thème :** "La Performance"
**Date :** 2026-03-06

---

## ✅ Tâches réalisées

### A18 — Audit et suppression MCPs non-essentiels ✅
- **Action :** Suppression complète (pas désactivation) de Playwright (22 outils) et System-Diag (27 outils)
- **Impact :** -12 250 tokens/message estimés (-44.7%)
- **MCPs restants :** Tavily (5 outils actifs), docker-mcp (disabled)
- **Commit :** c0aca15

### A17 — ToolRegistry Filter ⏸️ REPORTÉ
- **Diagnostic :** Architecture monkey-patch incorrecte — l'extension n'était pas chargée par A0
- **Décision PO :** Reporter jusqu'à ce que MCPs actifs > 15 outils
- **Infrastructure mise en place :**
  - Script `check_mcp_count.py` — vérifie le seuil de déclenchement
  - Tâche scheduler adhoc "MCP Monitor" (ID: oaEiNqUH) — exécutable depuis l'UI
  - Fichiers archivés dans `archive_a17/`
- **Commit :** 8575948

---

## 📊 Métriques Sprint 5

| Métrique | Valeur |
|----------|--------|
| Tokens économisés (A18) | ~12 250/message |
| Réduction estimée | -44.7% |
| MCPs actifs restants | 1 (Tavily, 5 outils) |
| Outils MCP total | 5 (vs 54 avant Sprint 5) |
| Commits | 2 (c0aca15, 8575948) |

---

## 🔄 Tâches restantes au backlog

| ID | Titre | Statut |
|----|-------|--------|
| A17 | ToolRegistry Filter | ⏸️ REPORTÉ (seuil > 15 MCPs) |
| A19 | Enrichissement profils developer/researcher | 📋 À FAIRE |
| A20 | Modularisation skill BMAD | 📋 À FAIRE |
| A7 | Rigueur documentation/backlog | 📋 À FAIRE |
| A11 | Audit sécurité | 📋 À FAIRE |

---

## 💡 Leçon apprise

**A17 Sprint 5 :** L'implémentation monkey-patch n'était pas compatible avec le mécanisme d'extension A0.
Si A17 est relancé, utiliser le hook `system_prompt` avec une classe héritant de `Extension`.
Dossier `archive_a17/` contient l'ancienne implémentation pour référence.
