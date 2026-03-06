# 🔍 Analysis — AUDIT-002 : Tool Not Found (CAUSE IDENTIFIÉE)

> Date : 2026-03-06 | Analyst : Business Analyst BMAD | Statut : ✅ ANALYSE COMPLÈTE

---

## 🎯 Cause Racine Identifiée

### Deux sources distinctes :

**Source 1 (principale) — Boucles `bc` → appels outils en retry**
- Dans les boucles retry causées par `bc` manquant, l'agent appelle des outils dans des états incohérents
- `fw.tool_not_found.md` déclenché dans ces contextes de loop

**Source 2 — Références à MCPs supprimés (A18)**
- Playwright (22 outils) et System-Diag (27 outils) ont été supprimés au Sprint 5
- Des sessions/subordinates créés AVANT A18 tentent encore d'appeler ces outils
- Résolution naturelle : les sessions anciennes expireront

---

## 🔗 Dépendances

- AUDIT-003 (cause principale)
- A18 (suppression MCPs — cause secondaire, résolution naturelle)
- A17 (ToolRegistry Filter) — NON nécessaire pour ce problème

---

## 💡 Solution

- Court terme : résoudre `bc` (AUDIT-003) élimine la majorité des tool_not_found
- Long terme : ajouter dans les instructions agents une liste des outils disponibles actuels

