# 📋 Backlog - Agent-Zero: Modular Optimizer

> Dernière mise à jour: 2026-03-04

---

## 📊 Vue d'Ensemble

| Statut | Nombre |
|--------|--------|
| À FAIRE | 1 |
| EN COURS | 0 |
| TERMINÉ | 1 |
| BLOQUÉ | 0 |

---

## ✅ Tâches Terminées

### Tâche #1: Stratégie Multi-Modèles pour Subordonnés

| Champ | Valeur |
|-------|--------|
| **Priorité** | HAUTE |
| **Statut** | ✅ TERMINÉ |
| **Date début** | 2026-03-03 |
| **Date fin** | 2026-03-04 |
| **UUID** | généré automatiquement |

#### Description
Implémenter une stratégie multi-modèles pour les agents subordonnés afin d'optimiser les coûts et la qualité des réponses selon le type de tâche.

#### Solution Implémentée
- **Developer**: DeepSeek V3.2 (openrouter) - 64K ctx - Économique pour code
- **Hacker**: Gemini 3 Flash Preview (openrouter) - 1M ctx - Vision pour sécu
- **Researcher**: GPT-4o-mini (openrouter) - 128K ctx - Économique pour recherche

#### Fichiers Créés
- `/a0/usr/agents/developer/settings.json`
- `/a0/usr/agents/hacker/settings.json`
- `/a0/usr/agents/researcher/settings.json`
- `.a0proj/knowledge/main/SUBORDINATES_CONFIG.md`

#### Architecture
Utilise le mécanisme d'override natif d'Agent Zero via `_15_load_profile_settings.py`. Les configurations sont invisibles dans l'UI mais appliquées automatiquement lors de l'appel de subordonnés.

#### Procédure de Rollback
```bash
rm -rf /a0/usr/agents/developer
rm -rf /a0/usr/agents/hacker
rm -rf /a0/usr/agents/researcher
```

#### Décision Associée
- [ADR-003] Adoption de la stratégie multi-modèles avec délégation active

---

## 📋 Tâches À Faire

### Tâche #2: Fallback Tavily pour la Recherche Web

| Champ | Valeur |
|-------|--------|
| **Priorité** | MOYENNE |
| **Statut** | 📋 À FAIRE |
| **Date création** | 2026-03-04 |
| **UUID** | wK25JDI4 |

#### Description
Implémenter un mécanisme de fallback pour les recherches web via Tavily MCP, avec fallback vers d'autres sources si le service est indisponible.

#### Contexte
Le PO a mentionné cette tâche comme prioritaire après la finalisation de la Tâche #1.

#### Prérequis
- Tâche #1 TERMINÉE ✅

---

## 📝 Notes

- Ce backlog suit la méthodologie BMAD
- Chaque tâche est liée à une décision dans `decisions/DECISIONS.md`
- Les fichiers de solution sont dans `solutions/`
