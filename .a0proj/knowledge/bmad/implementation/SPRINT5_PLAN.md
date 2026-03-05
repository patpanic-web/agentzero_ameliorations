# 📋 Sprint 5 — Plan

## Thème : "La Performance"

## Objectif principal
Valider et activer le ToolRegistry Filter en production → réduction ~48% tokens/message

## Tâches

| ID | Titre | Effort | Priorité |
|----|-------|--------|----------|
| **A17** | Validation ToolRegistry Filter en production | ⏱️ 2h | 🔴 P1 CRITIQUE |
| **A6** | Corriger Git MCP default path | ⏱️ 5 min | 🟡 Quick win |
| **A9** | Remplir git_url dans project.json | ⏱️ 2 min | 🟡 Quick win |

## Définition de Done — A17
- [ ] Extension chargée et active au démarrage
- [ ] Logs de filtrage visibles ("Filtered X tools down to Y")
- [ ] Mesure tokens avant/après documentée
- [ ] Aucune régression fonctionnelle constatée
- [ ] Résultats documentés dans knowledge/

## Impact attendu
- Avant : ~27 400 tokens/message
- Après : ~14 650 tokens/message (-48%)
- Économie : ~12 750 tokens/message
