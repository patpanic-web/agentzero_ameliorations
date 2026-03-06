# 📋 BACKLOG — Agent-Zero Modular Optimizer
> Dernière mise à jour : 2026-03-06 (Sprint 9 : MCP-Q1 + MCP-Q2 TERMINÉS)

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
| A7 | Rigueur documentation/backlog — relire avant chaque planification sprint | 🟢 P3 | 🟡 MOYEN | ⏱️ 30 min | ✅ TERMINÉ (Sprint 6) | Checklist début planification sprint ajoutée dans BMAD_PROCESS.md |
| T2 | Fallback Tavily Recherche Web | 🟢 P3 | 🟡 MOYEN | ⏱️ 1h | ⏸️ REPORTÉ | À réaligner avec nouveaux axes |
| T4 | Lazy MCP Tool Loading | 🟢 P3 | 🟡 MOYEN | ⏱️ 2h | ⏸️ REPORTÉ | Aucune implémentation trouvée |
| T5 | MCP Response Caching | 🟢 P3 | 🟡 MOYEN | ⏱️ 2h | ⏸️ REPORTÉ | En attente de priorité |
| T6 | Étude A0T Token / Venice AI (inférences gratuites) | 🟡 P2 | 🟡 MOYEN | ⏱️ 1h | ⏸️ REPORTÉ | À évaluer dans A18 — potentiel remplacement MCPs coûteux par Venice AI gratuit |
| T7 | Évaluation Modèle Embedding | 🟢 P3 | 🟡 MOYEN | ⏱️ 1h | ⏸️ REPORTÉ | En attente de priorité |
| T8 | Chrome / Tests Navigateur | 🟢 P3 | 🟢 FAIBLE | ⏱️ 1h | ⏸️ REPORTÉ | En attente de priorité |

| A16 | Intégration BMAD personas dans l'environnement | 🟡 P2 | 🟡 MOYEN | ⏱️ 1h | ✅ TERMINÉ (Sprint 4) | BMAD_PERSONAS.md créé + template Niv.2 mis à jour |
| A17 | Validation ToolRegistry Filter en production | 🔴 P1 | 🔴 HAUT | ⏱️ 2h | ⏸️ REPORTÉ | Déclencher si MCPs actifs > 15 outils — actuellement 5 (Tavily seul) après A18 |
| A18 | Audit utilité MCPs actifs — désactiver les non-essentiels | 🔴 P1 | 🔴 HAUT | ⏱️ 1h | ✅ TERMINÉ (Sprint 5) | Playwright (22 outils) + System-Diag (27 outils) supprimés → -12250 tokens/msg (-44.7%) |
| A19 | Enrichissement profils developer/researcher | 🟡 P2 | 🟡 MOYEN | ⏱️ 30min | ✅ TERMINÉ (Sprint 7) | Ajout section Operational Best Practices (token economy, persistance, vérification, délégation) aux profils developer + researcher |
| A20 | Consolidation BMAD universelle (personas+QA+Scrum+QualityGates+DoD+bugfix) | 🟡 P2 | 🔴 HAUT | ⏱️ 3h | ✅ TERMINÉ | Analyse BMAD v6 officiel + alternatives autonomes. Enrichissement BMAD_PERSONAS.md (+QA+SM+QualityGates+DoD+IRG). Templates niv2 synchronisés. Bug init-governance.sh corrigé (BMAD_PERSONAS.md non copié). |
| A21 | Système auto-amélioration Agent-Zero | 🟡 P2 | 🔴 HAUT | ⏱️ 3h | ✅ TERMINÉ (Sprint 7) | Skill self-audit créé (/a0/usr/skills/self-audit/) + scheduled task hebdomadaire (lundi 6h, ID: QkpuguTa) — analyse sessions, détection patterns, propositions backlog |
| A22 | BMAD Personas Multi-Model : LLM + outils par phase | 🟢 P3 | 🔴 HAUT | ⏱️ ~10h | 🔄 EN COURS (Analysis) | Assigner un LLM optimal + liste d'outils filtrés à chaque persona BMAD. BA/PM/Scrum → LLM léger (~$0.08/1M). Architect/Developer → LLM puissant. Impact estimé : -56% coût/session. Portée universelle via skill project-governance Level 2. |
| A23 | Interface Kanban PO ↔ Agent Zero | 🟢 P3 | 🔴 HAUT | ⏱️ ? | 🔄 EN COURS (Analysis) | Concept : remplacer/compléter l'interface chat par un Kanban board agile. Le PO interagit avec A0 comme avec une équipe (colonnes To Do/In Progress/Done). Sync BACKLOG.md ↔ board visuel. À explorer : intégration outil existant (Trello/GitHub Projects/Notion/Linear) vs interface custom. Phase Analysis requise. |
| A24 | Personas BMAD complets (prénoms + personnalités + outils) | 🟡 P2 | 🟡 MOYEN | ⏱️ 1h | ✅ TERMINÉ (Sprint 8) | Gap d'implémentation : BMAD_PERSONAS.md définit des rôles sans prénoms. PO veut voir "Mary (BA)", "Sarah (PM)" etc. dans les conversations. |
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

| MCP-Q1 | Installation + Configuration MCP QNAP | 🔴 P1 | 🔴 HAUT | ⏱️ 3h | ✅ TERMINÉ (Sprint 9) | Tests MCP passés : list_files + get_system_info OK |
| MCP-Q2 | Audit configuration QNAP (réseau, sécurité, nettoyage) | 🔴 P1 | 🔴 HAUT | ⏱️ 2h | ✅ TERMINÉ (Sprint 9) | Vérifier accès Tailscale/VPS, nettoyage config, préparer pour Agent Zero |
| MCP-Q3 | Configuration QNAP comme stockage persistant | 🟡 P2 | 🟡 MOYEN | ⏱️ 1.5h | 📋 À FAIRE | Intégrer NAS comme /a0/usr/storage (cross-restart persistence) |
## 🔒 AXE SÉCURITÉ

| ID | Titre | Priorité | Impact | Effort | Statut | Note |
|----|-------|----------|--------|--------|--------|------|
| A11 | Audit de sécurité complet du système | 🟢 P3 | 🔴 HAUT | ⏱️ 2-3h | ⏸️ REPORTÉ | |
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
- **Sprint 5** (2026-03-06) : "La Performance" — A18 (suppression MCPs Playwright+SysDiag → -12250 tokens/msg -44.7%) + A17 reporté avec monitoring MCP
- **Sprint 6** (2026-03-06) : "La Méthodologie" — A20 (consolidation BMAD universelle personas+QA+Scrum+QualityGates+DoD) + A7 (checklist planification sprint)
- **Sprint 7** (2026-03-06) : "L'Intelligence Adaptive" — A19 (enrichissement profils developer+researcher) + A21 (skill self-audit + scheduled task hebdomadaire)

## Nouvelle Tâche: Analyse d'adaptation BMAD
- **Description**: Explorer et adapter les éléments du BMAD v6 dans Agent Zero.
- **Livrables**: Rapport détaillé sauvegardé dans `knowledge/bmad/analysis/A20_BMAD_OFFICIEL_ADAPTATONS_A0.md`.
- **Priorité**: P1
- **Date de création**: 2026-03-06
| AUDIT-001 | Improve JSON response validation | 💡 P3 | Cause racine : faux positifs déclenchés par `bc` absent → fw.msg_misformat. Lié à AUDIT-003. | - | ✅ ANALYSE COMPLÈTE | bc manquant (lié AUDIT-003) |
| AUDIT-002 | Tool registry awareness enhancement | 💡 P3 | Source 1 : boucles bc→retry. Source 2 : MCPs Playwright/SysDiag supprimés (A18) encore référencés. | - | ✅ ANALYSE COMPLÈTE | bc + A18 |
| AUDIT-003 | Reduce message repetition loops | 💡 P3 | CAUSE RACINE : `bc` non installé → loop bc→misformat→nudge→repeat. Corriger bc = corriger AUDIT-001/002/004. | - | ✅ ANALYSE COMPLÈTE | bc non installé |
| AUDIT-004 | Optimize timeout handling | 💡 P3 | Boucles bc prolongées → dépassement timeout fw.code.max_time. Résoudre bc = résoudre ~80% AUDIT-004. | - | ✅ ANALYSE COMPLÈTE | bc manquant (lié AUDIT-003) |
