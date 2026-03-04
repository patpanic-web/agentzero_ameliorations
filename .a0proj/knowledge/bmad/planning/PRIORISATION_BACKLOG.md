# 📋 Priorisation du Backlog - Phase PLANNING (John)

> **Date:** 2026-03-04
> **Critères:** Consommation tokens + Fiabilité outils
> **Décideur:** John (PM) sur délégation PO

---

## 🎯 Critères de Priorisation

| Critère | Poids |
|---------|-------|
| **Réduction tokens** | 40% |
| **Fiabilité outils** | 40% |
| **Effort/Complexité** | 20% |

---

## 📊 Analyse par Tâche

### Tâche #3: Tool Description Augmenter
| Critère | Score |
|---------|-------|
| Réduction tokens | ⭐⭐⭐ (indirect: moins d'erreurs) |
| Fiabilité outils | ⭐⭐⭐⭐⭐ (+25% précision DIRECT) |
| Effort | ⭐⭐⭐⭐⭐ (faible - extension prompt) |
| Risque | ⭐⭐⭐⭐⭐ (faible) |

**Score global: 4.6/5**

### Tâche #4: Lazy MCP Tool Loading
| Critère | Score |
|---------|-------|
| Réduction tokens | ⭐⭐⭐⭐⭐ (-46.9% DIRECT) |
| Fiabilité outils | ⭐⭐⭐ (risque Goose) |
| Effort | ⭐⭐⭐ (moyen) |
| Risque | ⭐⭐⭐ (moyen - classification) |

**Score global: 3.8/5**

### Tâche #2: Fallback Tavily
| Critère | Score |
|---------|-------|
| Réduction tokens | ⭐⭐ (indirect) |
| Fiabilité outils | ⭐⭐⭐⭐ (fiabilité recherche) |
| Effort | ⭐⭐⭐⭐ (faible) |
| Risque | ⭐⭐⭐⭐ (faible) |

**Score global: 3.4/5**

### Tâche #8: Chrome / Tests Automatiques
| Critère | Score |
|---------|-------|
| Réduction tokens | ⭐⭐ (validation des autres) |
| Fiabilité outils | ⭐⭐⭐ (tests E2E) |
| Effort | ⭐⭐⭐ (à évaluer) |
| Risque | ⭐⭐⭐ (à évaluer) |

**Score global: 2.8/5**

### Tâche #5: MCP Response Caching
| Critère | Score |
|---------|-------|
| Réduction tokens | ⭐ (latence, pas tokens) |
| Fiabilité outils | ⭐⭐⭐ (performance) |
| Effort | ⭐⭐⭐ (moyen) |
| Risque | ⭐⭐⭐ (invalidation) |

**Score global: 2.2/5**

### Tâche #7: Évaluation Embedding
| Critère | Score |
|---------|-------|
| Réduction tokens | ⭐ (qualité mémoire) |
| Fiabilité outils | ⭐⭐ (précision) |
| Effort | ⭐⭐⭐⭐ (faible) |
| Risque | ⭐⭐⭐⭐ (faible) |

**Score global: 2.0/5**

### Tâche #6: Étude A0T Token
| Critère | Score |
|---------|-------|
| Réduction tokens | ⭐⭐⭐⭐ (gratuit?) |
| Fiabilité outils | ⭐ (non lié) |
| Effort | ⭐⭐ (recherche longue) |
| Risque | ⭐ (incertain) |

**Score global: 1.8/5**

---

## 🏆 Ordre de Priorité Proposé

| Rang | Tâche | Justification |
|------|-------|---------------|
| **1** | #3 Tool Description Augmenter | Impact DIRECT sur fiabilité (+25%), faible effort/risque |
| **2** | #4 Lazy MCP Tool Loading | Impact DIRECT sur tokens (-46.9%), à faire après #3 (meilleure classification) |
| **3** | #2 Fallback Tavily | Fiabilité recherche, quick win |
| **4** | #8 Chrome / Tests Auto | Validation des autres tâches via tests E2E |
| **5** | #5 MCP Response Caching | Performance, moins prioritaire |
| **6** | #7 Évaluation Embedding | Amélioration qualité, basse priorité |
| **7** | #6 A0T Token | Recherche incertaine, à garder en veille |

---

## 📝 Notes de John (PM)

- **Dépendance identifiée:** #3 devrait précéder #4 pour améliorer la classification d'intention
- **Quick wins:** #3 et #2 peuvent être faites rapidement
- **Risque mitigé:** #4 nécessite des tests (d'où #8 en position 4)

---

## ✅ Validation PO Requise

Cet ordre de priorité vous convient-il ?

