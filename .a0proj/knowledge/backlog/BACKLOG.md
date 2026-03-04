# 📋 Backlog - Agent-Zero: Modular Optimizer

> Dernière mise à jour: 2026-03-04

---

## 📊 Vue d'Ensemble

| Statut | Nombre |
|--------|--------|
| À FAIRE | 5 |
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

### Tâche #3: Tool Description Augmenter

| Champ | Valeur |
|-------|--------|
| **Priorité** | HAUTE |
| **Statut** | 📋 À FAIRE |
| **Date création** | 2026-03-04 |
| **UUID** | tool-aug-001 |
| **Source** | Recherche web + Audit local |

#### Description
Enrichir les descriptions des outils MCP pour améliorer la précision de sélection d'outil par l'agent.

#### Justification
- **Source**: arXiv 2025 - "MCP Tool Descriptions Are Smelly"
- **Gain**: +25% précision sur sélection d'outil
- **Risque**: Faible

#### Implémentation
- Modifier le prompt `agent.system.tools.md`
- Ajouter: Purpose, Guidelines, Limitations, Examples pour chaque outil

#### Faisabilité
| Critère | Évaluation |
|---------|------------|
| Core modifié | ❌ Aucun (extension prompt) |
| Réversibilité | ✅ Totale |
| Complexité | Faible |

#### Décision Associée
- [ADR-004] Analyse des Optimisations MCP

---

### Tâche #4: Lazy MCP Tool Loading

| Champ | Valeur |
|-------|--------|
| **Priorité** | HAUTE (avec tests) |
| **Statut** | 📋 À FAIRE |
| **Date création** | 2026-03-04 |
| **UUID** | lazy-mcp-001 |
| **Source** | Recherche web + Audit local |

#### Description
Implémenter un chargement paresseux des outils MCP pour réduire la consommation de tokens.

#### Justification
- **Source**: GitHub Anthropic #11364, LinkedIn A/B tests
- **Gain**: -46.9% tokens (validé)
- **Risque**: **MOYEN** - Goose (Block) a supprimé leur implémentation après échec

#### Audit Local
- Fichier: `/a0/python/extensions/system_prompt/_10_system_prompt.py`
- Ligne 55: `get_tools_prompt()` charge TOUS les outils

#### Implémentation
- Classification d'intention pour filtrer les outils pertinents
- Extension modifiable sans core change

#### Tests Requis
1. Benchmark tokens avant/après
2. Validation que la classification d'intention fonctionne
3. Tests de non-régression sur sélection d'outil

#### Procédure de Rollback
Désactiver l'extension par paramètre.

#### Décision Associée
- [ADR-004] Analyse des Optimisations MCP

---

### Tâche #5: MCP Response Caching

| Champ | Valeur |
|-------|--------|
| **Priorité** | MOYENNE |
| **Statut** | 📋 À FAIRE (en attente) |
| **Date création** | 2026-03-04 |
| **UUID** | mcp-cache-001 |
| **Source** | Recherche web |

#### Description
Implémenter un cache pour les réponses MCP répétitives.

#### Justification
- **Source**: Fast.io, Tim Kellogg ("MCP Resources are for Caching")
- **Gain**: -80% latence sur appels répétitifs
- **Risque**: Moyen (complexité invalidation)

#### Statut
En attente de stabilisation du pattern dans l'écosystème.

#### Décision Associée
- [ADR-004] Analyse des Optimisations MCP

---

## 📝 Notes

- Ce backlog suit la méthodologie BMAD
- Chaque tâche est liée à une décision dans `decisions/DECISIONS.md`
- Les fichiers de solution sont dans `solutions/`

---

### Tâche #6: Étude A0T Token pour Inférences Gratuites

| Champ | Valeur |
|-------|--------|
| **Priorité** | MOYENNE |
| **Statut** | 📋 À FAIRE |
| **Date création** | 2026-03-04 |
| **UUID** | a0t-token-001 |
| **Source** | Idée PO |

#### Description
Étudier la viabilité d'utiliser "Agentic AI Crypto - A0T Token" dans Agent Zero pour obtenir des inférences gratuites en cas de blocage du token A0T.

#### Contexte
Le PO possède déjà des wallets crypto et envisage une conversion de certaines cryptos en A0T.

#### Questions à Résoudre
1. Sur quels réseaux l'A0T Token est-il disponible ?
2. Quelles cryptos peuvent être swapées vers A0T ?
3. Comment intégrer A0T dans Agent Zero ?
4. Quel est le mécanisme de "blocage" et comment obtient-on des inférences gratuites ?

#### Livrables Attendus
- [ ] Analyse technique de l'A0T Token
- [ ] Liste des réseaux supportés
- [ ] Matrice de compatibilité des cryptos à swaper
- [ ] Guide d'intégration Agent Zero
- [ ] Analyse coût/bénéfice

#### Prérequis
- Recherche documentaire sur Agentic AI Crypto
- Analyse des wallets existants du PO


---

### Tâche #7: Évaluation du Modèle d'Embedding

| Champ | Valeur |
|-------|--------|
| **Priorité** | BASSE |
| **Statut** | 📋 À FAIRE |
| **Date création** | 2026-03-04 |
| **UUID** | embedding-001 |
| **Source** | Discussion PO |

#### Description
Évaluer la pertinence de challenger le modèle d'embedding actuel `sentence-transformers/all-MiniLM-L6-v2`.

#### Contexte
Le modèle actuel est compact (80MB) mais de qualité moyenne. Il existe des alternatives plus performantes.

#### Modèles à Comparer
| Modèle | Taille | Qualité | Commentaire |
|--------|--------|---------|-------------|
| all-MiniLM-L6-v2 | 80MB | Moyenne | Actuel, rapide |
| all-mpnet-base-v2 | 420MB | Haute | +10% précision |
| bge-small-en-v1.5 | 130MB | Haute | Bon compromis |
| multilingual-e5-small | 470MB | Haute | Multilingue |

#### Critères d'Évaluation
- Qualité des embeddings (benchmark MTEB)
- Vitesse d'inférence
- Impact sur la Tool Memory
- Compatibilité avec Agent-Zero

#### Livrables Attendus
- [ ] Benchmark des modèles
- [ ] Recommandation argumentée
- [ ] Guide de migration si applicable


---

### Tâche #8: Résolution Problème Chrome / Tests Automatiques Navigateur

| Champ | Valeur |
|-------|--------|
| **Priorité** | À DÉFINIR (en attente clarification) |
| **Statut** | 📋 À FAIRE |
| **Date création** | 2026-03-04 |
| **UUID** | chrome-browser-001 |
| **Source** | Demande PO |

#### Description
Investiguer et résoudre le problème d'installation de Chrome pour les tests automatiques. Le PO souhaite évaluer l'utilité d'un navigateur Chrome fonctionnel pour les phases de test automatiques.

#### Contexte
- Chrome standard ne peut pas être installé sur Kali (non supporté)
- Playwright MCP apporte déjà Chromium (`chromium-1208`)
- Un test réussi existe (`screenshots/playwright_test_success.png`)

#### Questions à Résoudre
1. Le PO a-t-il besoin de Chrome spécifiquement ou de tests navigateur ?
2. Playwright Chromium répond-il au besoin ?
3. Quels types de tests automatiques sont envisagés ?
4. Quelle est la valeur ajoutée d'avoir Chrome vs Chromium ?

#### Alternatives Identifiées
| Option | Avantages | Inconvénients |
|--------|-----------|---------------|
| **Playwright Chromium** | Déjà installé, fonctionne | Pas d'extensions Chrome |
| **Chrome Docker externe** | Chrome officiel | Complexité, tokens |
| **Chrome Headless Shell** | Léger | Configuration requise |

#### Prérequis
- [ ] Clarification du besoin avec le PO
- [ ] Définition du type de tests envisagés

#### Livrables Attendus
- [ ] Analyse comparative Chrome vs Chromium pour les tests
- [ ] Recommandation argumentée
- [ ] Si applicable: solution d'installation

#### Note
Cette tâche nécessite une phase Analysis BMAD complète avant toute implémentation.

