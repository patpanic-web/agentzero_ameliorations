# Sprint T2 — Implémentation Skill Fallback Tavily

> **Date**: 2026-03-08  
> **Product Manager**: Sarah  
> **Implementeur**: James | Developer  
> **QA**: Quinn | QA Engineer  
> **Statut**: 📋 Planifié — En attente GO

---

## 🎯 Objective du Sprint

Créer le skill `tavily-fallback` avec mécanisme de fallback **per request** (stateless), permettant une bascule transparente vers `search_engine` en cas d'échec transitoire de Tavily.

---

## 📋 Définition of Done (DoD)

- [ ] Structure skill créée dans `/a0/usr/skills/tavily-fallback/`
- [ ] Wrapper `search.py` implémenté avec fallback per_request
- [ ] SKILL.md documenté avec usage et configuration
- [ ] Tests E2E fonctionnels (Tavily OK, Tavily FAIL → fallback, Tavily recovery)
- [ ] Persistance vérifiée (restart Docker)
- [ ] Commit poussé avec message conventionnel
- [ ] BACKLOG.md mis à jour (T2 → TERMINÉ)

---

## 🎬 Tâches du Sprint

| ID | Tâche | Effort | Assigné | Dépendances |
|----|-------|--------|---------|-------------|
| T2.1 | Créer structure skill et SKILL.md | 20 min | James | Aucune |
| T2.2 | Implémenter wrapper search.py (fallback per_request) | 40 min | James | T2.1 |
| T2.3 | Créer config fallback.yaml | 15 min | James | T2.1 |
| T2.4 | Tests E2E (3 scénarios: OK, FAIL→fallback, Recovery) | 30 min | James | T2.2 |
| T2.5 | Rédaction documentation installation/desactivation | 15 min | James | T2.3 |
| **Total** | | **~2h** | | |

---

## 🏁 Quality Gates

### Avant Implementation
- [x] Solution validée par PO (Option A: per_request)
- [x] Analyse cause racine effectuée (erreurs ponctuelles identifiées)
- [x] Dependances disponibles (Tavily MCP, search_engine natif)
- [x] Impact tokens évalué (~+50/session, -30% vs retry loops)

### Pendant Implementation
- [ ] Commit par tâche terminée
- [ ] Tests après chaque phase critique

### Avant Cloture (Checklist Fin de Sprint)
- [ ] Tests E2E: Scénario OK (Tavily fonctionne)
- [ ] Tests E2E: Scénario FAIL (fallback search_engine)
- [ ] Tests E2E: Scénario Recovery (Tavily re-testé sur requête suivante)
- [ ] Audit couverture tâches T2.1-T2.5
- [ ] Rapport Go/No-Go produit

---

## 💰 Budget Tokens Estimé

| Phase | Coût tokens |
|-------|-------------|
| Implementation T2.1-T2.3 | ~2,000 |
| Tests E2E T2.4 | ~1,500 |
| Documentation T2.5 | ~500 |
| **Total** | **~4,000 tokens** |

---

## 🔄 Stratégie de Rollback

| Situation | Action |
|-----------|--------|
| Fallback déclenché abusivement | Modifier config `fallback.yaml` → mode "disabled" |
| Skill créé avec erreur | `mv skill` vers `.disabled` |
| Dégradation perfs | Réduire timeout Tavily à 10s |

---

## 📊 Critères de Succès Mesurables

1. Test E2E Scénario 2: Fallback déclenché en < 16s (timeout Tavily + search_engine)
2. Test E2E Scénario 3: Tavily re-testé automatiquement sans intervention
3. 0 modification code source Agent-Zero
4. Désactivation possible en < 5s par renommage skill

---

## ⏭️ Prochain Sprint Suggéré

T4 — Lazy MCP Tool Loading (déjà reporté, fortement dépendant de la stabilité T2)

---

**Sarah | Product Manager**  
> "Sprint T2 prêt — mécanisme per_request validé par PO, estimation conservatrice 2h. En attente GO pour lancement."
