# 📋 BACKLOG — Agent-Zero Modular Optimizer
> Dernière mise à jour : 2026-03-05 (Sprint 3 clôturé)

<!-- ⚠️ FORMAT IMPOSÉ — NE PAS RESTRUCTURER CE FICHIER
     Conserver le format tableau. Ne pas convertir en sections ###.
     Seules les VALEURS dans les cellules peuvent être modifiées. -->

---

## 🌐 AXE GLOBAL — Comportement fondamental Agent Zero

| ID | Titre | Priorité | Impact | Effort | Statut |
|----|-------|----------|--------|--------|--------|
| A1 | Override `solving.md` → delegate-first | 🔴 P0 | 🔴 MAJEUR | ⏱️ 15 min | ✅ TERMINÉ (Sprint 1) |
| A2 | Override `call_sub.md` → MUST delegate | 🔴 P0 | 🔴 MAJEUR | ⏱️ 15 min | ✅ TERMINÉ (Sprint 1) |
| A3 | Enrichir profil Hacker (14 → 200 lignes) | 🔴 P1 | 🔴 HAUT | ⏱️ 1h | ✅ TERMINÉ (Sprint 2) |
| A4 | Renforcer rôle orchestrateur Agent0 | 🟡 P1 | 🟡 HAUT | ⏱️ 30 min | ✅ TERMINÉ (Sprint 2) |
| A5 | Documentation & config LLM par agent | 🟡 P2 | 🟡 MOYEN | ⏱️ 1h | 📋 À FAIRE |
| A7 | Rigueur documentation/backlog (processus) | 🟢 P3 | 🟢 MOYEN | ⏱️ 30 min | 📋 À FAIRE |

## 📁 AXE PROJET — Gouvernance & Git/GitHub

| ID | Titre | Priorité | Impact | Effort | Statut |
|----|-------|----------|--------|--------|--------|
| A8 | Gouvernance Git dans prompts projet | 🔴 P1 | 🔴 HAUT | ⏱️ 30 min | ✅ TERMINÉ (Sprint 3) |
| A10 | Template gouvernance projet Niv.1/2 | 🔴 P1 | 🔴 HAUT | ⏱️ 1h | ✅ TERMINÉ (Sprint 3) |
| A12 | Backlog SSOT + checklist fin de sprint | 🔴 P1 | 🔴 HAUT | ⏱️ 15 min | ✅ TERMINÉ (Sprint 3) |
| A13 | Instruction bootstrap session (lire backlog) | 🔴 P1 | 🔴 HAUT | ⏱️ 5 min | ✅ TERMINÉ (Sprint 3) |
| A6 | Corriger Git MCP default path | 🟡 P2 | 🟡 MOYEN | ⏱️ 5 min | 📋 À FAIRE |
| A9 | Remplir git_url dans project.json | 🟡 P2 | 🟡 MOYEN | ⏱️ 2 min | 📋 À FAIRE |

## 🔒 AXE SÉCURITÉ

| ID | Titre | Priorité | Impact | Effort | Statut |
|----|-------|----------|--------|--------|--------|
| A11 | Audit de sécurité complet du système | 🟡 P2 | 🔴 HAUT | ⏱️ 2-3h | 📋 À FAIRE |

---

## 🏛️ ANCIENNES TÂCHES (Historique)

| # | Titre | Statut | Note |
|---|-------|--------|------|
| T1 | Stratégie Multi-Modèles | ✅ TERMINÉ | Configs dans /a0/usr/agents/ |
| T2 | Fallback Tavily Recherche Web | ⏸️ REPORTÉ | Réaligner avec nouveaux axes |
| T3 | Tool Description Augmenter | ❌ ABANDONNÉ | — |
| T4 | Lazy MCP Tool Loading | ⏸️ REPORTÉ | Aucune implémentation trouvée |
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

## 🏆 Sprints Complétés
- **Sprint 1** (2026-03-05) : "La Fondation" — A1 + A2 (delegate-first behavior)
- **Sprint 2** (2026-03-05) : "Les Profils" — A3 + A4 (hacker enrichment + orchestration)
- **Sprint 3** (2026-03-05) : "La Gouvernance" — A8 + A10 + A12 + A13 (git governance + templates + SSOT + bootstrap)

