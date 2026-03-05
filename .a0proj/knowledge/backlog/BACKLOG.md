# 📋 BACKLOG — Agent-Zero Modular Optimizer
> Dernière mise à jour : 2026-03-05 (Phase 1 Analysis complète)

---

## 🌐 AXE GLOBAL — Comportement fondamental Agent Zero

| ID | Titre | Priorité | Impact | Effort | Statut |
|----|-------|----------|--------|--------|--------|
| A1 | Override `solving.md` → delegate-first | 🔴 P0 | 🔴 MAJEUR | ⏱️ 15 min | ✅ TERMINÉ |
| A2 | Override `call_sub.md` → MUST delegate | 🔴 P0 | 🔴 MAJEUR | ⏱️ 15 min | ✅ TERMINÉ |
| A3 | Enrichir profil Hacker (8 lignes → complet) | 🔴 P1 | 🔴 HAUT | ⏱️ 1h | 📋 À FAIRE |
| A4 | Renforcer rôle orchestrateur Agent0 | 🟡 P1 | 🟡 HAUT | ⏱️ 30 min | 📋 À FAIRE |
| A5 | Documentation & config LLM par agent | 🟡 P2 | 🟡 MOYEN | ⏱️ 1h | 📋 À FAIRE |
| A7 | Rigueur documentation/backlog (processus) | 🟢 P3 | 🟢 MOYEN | ⏱️ 30 min | 📋 À FAIRE |

## 📁 AXE PROJET — Gouvernance & Git/GitHub

| ID | Titre | Priorité | Impact | Effort | Statut |
|----|-------|----------|--------|--------|--------|
| A8 | Gouvernance Git dans prompts projet | 🔴 P1 | 🔴 HAUT | ⏱️ 30 min | 📋 À FAIRE |
| A10 | Template gouvernance projet Niv.1/2 | 🔴 P1 | 🔴 HAUT | ⏱️ 1h | 📋 À FAIRE |
| A6 | Corriger Git MCP default path | 🟡 P2 | 🟡 MOYEN | ⏱️ 5 min | 📋 À FAIRE |
| A9 | Remplir git_url dans project.json | 🟡 P2 | 🟡 MOYEN | ⏱️ 2 min | 📋 À FAIRE |

---

## 🏛️ ANCIENNES TÂCHES (Historique)

| # | Titre | Statut | Note |
|---|-------|--------|------|
| T1 | Stratégie Multi-Modèles | ✅ TERMINÉ | Configs dans /a0/usr/agents/ |
| T2 | Fallback Tavily Recherche Web | ⏸️ REPORTÉ | Réaligner avec nouveaux axes |
| T3 | Tool Description Augmenter | ❌ ABANDONNÉ | — |
| T4 | Lazy MCP Tool Loading | ⏸️ REPORTÉ | Marqué EN COURS à tort, aucune implémentation trouvée |
| T5 | MCP Response Caching | ⏸️ REPORTÉ | En attente priorité |
| T6 | Étude A0T Token | ⏸️ REPORTÉ | En attente priorité |
| T7 | Évaluation Modèle Embedding | ⏸️ REPORTÉ | En attente priorité |
| T8 | Chrome / Tests Navigateur | ⏸️ REPORTÉ | En attente priorité |

---

## 📊 Légende
- 📋 À FAIRE | 🔄 EN COURS | ✅ TERMINÉ | ⏸️ REPORTÉ | ❌ ABANDONNÉ
- 🔴 P0 = Critique | 🔴 P1 = Haut | 🟡 P2 = Moyen | 🟢 P3 = Faible

## 📐 Décisions PO
- Priorité #1 = Comportement correct AVANT optimisation tokens
- No-Core-Change strict — configs, prompts overrides, modules uniquement
- LLM = contrôle manuel PO uniquement
- Gouvernance projet : Niveau 1 (léger/tous) + Niveau 2 (BMAD/sur décision PO)
