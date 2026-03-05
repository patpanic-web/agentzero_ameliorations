# 📋 BACKLOG — Agent-Zero Modular Optimizer
> Dernière mise à jour : 2026-03-06 (Sprint 4 — ajout A14 : désactivation MCP Git)

<!-- ⚠️ FORMAT IMPOSÉ — NE PAS RESTRUCTURER CE FICHIER
     Conserver le format tableau. Ne pas convertir en sections ###.
     Ne pas créer de fichier .bak. Seules les VALEURS dans les cellules peuvent être modifiées. -->

---

## 🌐 AXE GLOBAL — Comportement fondamental Agent Zero

| ID | Titre | Priorité | Impact | Effort | Statut | Note |
|----|-------|----------|--------|--------|--------|------|
| A1 | Override `solving.md` → delegate-first | 🔴 P0 | 🔴 MAJEUR | ⏱️ 15 min | ✅ TERMINÉ (Sprint 1) | |
| A2 | Override `call_sub.md` → MUST delegate | 🔴 P0 | 🔴 MAJEUR | ⏱️ 15 min | ✅ TERMINÉ (Sprint 1) | |
| A3 | Enrichir profil Hacker (14 → 200 lignes) | 🔴 P1 | 🔴 HAUT | ⏱️ 1h | ✅ TERMINÉ (Sprint 2) | |
| A4 | Renforcer rôle orchestrateur Agent0 | 🔴 P1 | 🟡 HAUT | ⏱️ 30 min | ✅ TERMINÉ (Sprint 2) | |
| A5 | Documentation & config LLM par agent | 🟡 P2 | 🟡 MOYEN | ⏱️ 1h | ✅ TERMINÉ (Sprint 4) | |
| A7 | Rigueur documentation/backlog (processus) | 🟢 P3 | 🟢 MOYEN | ⏱️ 30 min | 📋 À FAIRE | |
| T2 | Fallback Tavily Recherche Web | 🟢 P3 | 🟡 MOYEN | ⏱️ 1h | ⏸️ REPORTÉ | À réaligner avec nouveaux axes |
| T4 | Lazy MCP Tool Loading | 🟢 P3 | 🟡 MOYEN | ⏱️ 2h | ⏸️ REPORTÉ | Aucune implémentation trouvée |
| T5 | MCP Response Caching | 🟢 P3 | 🟡 MOYEN | ⏱️ 2h | ⏸️ REPORTÉ | En attente de priorité |
| T6 | Étude A0T Token | 🟢 P3 | 🟡 MOYEN | ⏱️ 1h | ⏸️ REPORTÉ | En attente de priorité |
| T7 | Évaluation Modèle Embedding | 🟢 P3 | 🟡 MOYEN | ⏱️ 1h | ⏸️ REPORTÉ | En attente de priorité |
| T8 | Chrome / Tests Navigateur | 🟢 P3 | 🟢 FAIBLE | ⏱️ 1h | ⏸️ REPORTÉ | En attente de priorité |

| A14 | Intégration BMAD personas dans l'environnement | 🟡 P2 | 🟡 MOYEN | ⏱️ 1h | ✅ TERMINÉ (Sprint 4) | BMAD_PERSONAS.md créé + template Niv.2 mis à jour |
| A15 | Validation ToolRegistry Filter en production | 🔴 P1 | 🔴 HAUT | ⏱️ 2h | 📋 À FAIRE | Réduction ~48% tokens/msg — code prêt, validation prod requise |
## 📁 AXE PROJET — Gouvernance & Git/GitHub

| ID | Titre | Priorité | Impact | Effort | Statut | Note |
|----|-------|----------|--------|--------|--------|------|
| A8 | Gouvernance Git dans prompts projet | 🔴 P1 | 🔴 HAUT | ⏱️ 30 min | ✅ TERMINÉ (Sprint 3) | |
| A10 | Template gouvernance projet Niv.1/2 | 🔴 P1 | 🔴 HAUT | ⏱️ 1h | ✅ TERMINÉ (Sprint 3) | |
| A12 | Backlog SSOT + checklist fin de sprint | 🔴 P1 | 🔴 HAUT | ⏱️ 15 min | ✅ TERMINÉ (Sprint 3) | |
| A13 | Instruction bootstrap session (lire backlog) | 🔴 P1 | 🔴 HAUT | ⏱️ 5 min | ✅ TERMINÉ (Sprint 3) | |
| A6 | Corriger Git MCP default path | 🟡 P2 | 🟡 MOYEN | ⏱️ 5 min | ✅ TERMINÉ (Sprint 4) |
| A14 | Supprimer MCP Git (surcoût tokens) | 🟡 P2 | 🟡 MOYEN | ⏱️ 5 min | ✅ TERMINÉ (Sprint 4) | ~500 tokens économisés/requête — entrée supprimée de settings.json | |
| A9 | Remplir git_url dans project.json | 🟡 P2 | 🟡 MOYEN | ⏱️ 2 min | ✅ TERMINÉ (Sprint 4) | |

## 🔒 AXE SÉCURITÉ

| ID | Titre | Priorité | Impact | Effort | Statut | Note |
|----|-------|----------|--------|--------|--------|------|
| A11 | Audit de sécurité complet du système | 🟡 P2 | 🔴 HAUT | ⏱️ 2-3h | 📋 À FAIRE | |
| T3 | Tool Description Augmenter | 🟢 P3 | 🟢 FAIBLE | ⏱️ 1h | ❌ ABANDONNÉ | Rapport coût/bénéfice défavorable |

---

## 📊 Légende
- 📋 À FAIRE | 🔄 EN COURS | ✅ TERMINÉ | ⏸️ REPORTÉ | ❌ ABANDONNÉ
- 🔴 P0 = Critique | 🔴 P1 = Haut | 🟡 P2 = Moyen | 🟢 P3 = Faible
- ⏸️ REPORTÉ = déprioritisé temporairement, à réévaluer à chaque planification de sprint

## 📐 Décisions PO
- Priorité #1 = Comportement correct AVANT optimisation tokens
- No-Core-Change strict — configs, prompts overrides, modules uniquement
- LLM = contrôle manuel PO uniquement (modèle actuel : claude-sonnet-4.6)
- Gouvernance projet : Niveau 1 (léger/tous) + Niveau 2 (BMAD/sur décision PO)

## 🏆 Sprints Complétés
- **Sprint 1** (2026-03-05) : "La Fondation" — A1 + A2 (delegate-first behavior)
- **Sprint 2** (2026-03-05) : "Les Profils" — A3 + A4 (hacker enrichment + orchestration)
- **Sprint 3** (2026-03-05) : "La Gouvernance" — A8 + A10 + A12 + A13 (git governance + templates + SSOT + bootstrap)
- **Sprint 4** (2026-03-05/06) : "La Configuration" — A9 + A6 + A5 + A14 (git_url + MCP path + audit LLM + désactivation MCP Git)
