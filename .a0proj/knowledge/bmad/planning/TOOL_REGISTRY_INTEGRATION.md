# 📋 Phase Planning: Intégration ToolRegistry dans les prompts

## 🎯 Objectif
Filtrer les outils MCP via recherche sémantique AVANT inclusion dans les prompts système.

## 🏗️ Architecture choisie
**Option 2:** Extension système qui override get_mcp_tools_prompt()

### Structure proposée:
```
/a0/usr/extensions/
├── tool_registry.py (existant)
└── tool_registry_prompt_override.py (nouveau)
```

### Fonctionnement:
1. Créer une extension qui se charge dans le système de prompts
2. Intercepter l'appel à get_mcp_tools_prompt()
3. Utiliser ToolRegistry pour filtrer les outils basé sur la requête utilisateur
4. Générer le prompt avec uniquement les outils filtrés

## 🔧 Dépendances
- ToolRegistry existant (FAISS + SentenceTransformer)
- Accès à la requête utilisateur pour le filtrage sémantique
- Compatibilité avec le système d'extensions d'Agent-Zero

## 📝 Étapes d'implémentation

### Étape 1: Comprendre le système d'extensions
- Analyser comment les extensions sont chargées
- Vérifier l'ordre de chargement (system_prompt extension)
- Comprendre comment accéder à la requête utilisateur

### Étape 2: Créer l'extension d'override
- Créer `/a0/usr/extensions/tool_registry_prompt_override.py`
- Implémenter une classe Extension qui override get_mcp_tools_prompt()
- Intégrer ToolRegistry pour le filtrage
- Gérer le fallback si ToolRegistry non disponible

### Étape 3: Configurer l'extension
- S'assurer qu'elle se charge AVANT _10_system_prompt.py
- Configurer les dépendances et initialisation
- Tester avec différents agents (agent0, developer, etc.)

### Étape 4: Tests et validation
- Mesurer la réduction de tokens
- Vérifier la pertinence des outils filtrés
- Tester avec différentes requêtes
- Vérifier qu'aucun outil essentiel n'est exclu

### Étape 5: Documentation
- Documenter comment activer/désactiver
- Documenter la configuration
- Créer des exemples d'utilisation

## ⚠️ Risques et atténuations

### Risque 1: Outils essentiels exclus
- Solution: Inclure toujours certains outils critiques (response, code_execution_tool, etc.)
- Fallback: Si recherche retourne < 3 outils, inclure plus d'outils

### Risque 2: Performance impact
- Solution: Cache des embeddings pour la session
- Solution: Limiter le nombre de recherches

### Risque 3: Compatibilité avec autres extensions
- Solution: Tester avec extensions existantes
- Solution: Logs détaillés pour debugging

## 📊 Métriques de succès

### Critères fonctionnels
- [ ] Les outils MCP sont filtrés par pertinence
- [ ] La réduction de tokens est mesurable (> 50%)
- [ ] Tous les agents fonctionnent normalement
- [ ] Aucune modification du code core

### Critères de performance
- [ ] Pas de délai perceptible lors du filtrage
- [ ] ToolRegistry réutilisé entre sessions
- [ ] Cache efficace pour requêtes similaires

### Critères de qualité
- [ ] Documentation complète
- [ ] Tests automatisés
- [ ] Configuration facile
- [ ] Réversible facilement

