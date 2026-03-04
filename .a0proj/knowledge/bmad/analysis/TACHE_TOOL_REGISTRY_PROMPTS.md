# 📊 Analyse BMAD: Intégration ToolRegistry dans les prompts système

## Contexte
Intégrer le ToolRegistry dans le système de prompts d'Agent-Zero pour filtrer les outils MCP via recherche sémantique.

## 📋 Instructions originales
- Faire en sorte que lorsqu'une tâche est donnée à l'agent, le ToolRegistry filtre les outils MCP pertinents AVANT qu'ils ne soient inclus dans le prompt système.
- Contrainte ABSOLUE: No-Core-Change

## 🔍 Analyse du système actuel

### Architecture découverte
1. **Système de prompts:** `/a0/prompts/agent.system.mcp_tools.md` contient `{{tools}}`
2. **Génération du contenu:** `/a0/python/extensions/system_prompt/_10_system_prompt.py` - fonction `get_mcp_tools_prompt()`
3. **Handler MCP:** `/a0/python/helpers/mcp_handler.py` - méthode `get_tools_prompt()`
4. **ToolRegistry existant:** `/a0/usr/extensions/tool_registry.py` - utilise FAISS + embeddings

### Mécanisme de lecture des prompts
- La fonction `agent.read_prompt()` cherche les fichiers dans plusieurs répertoires
- Utilise `find_file_in_dirs()` qui recherche d'abord dans les répertoires backup
- Structure: recherche dans backup_dirs puis dans les répertoires par défaut

## 🎯 Options d'implémentation (non-intrusive)

### Option 1: Surcharge du template via /a0/usr/prompts/
**Avantages:**
- Simple, juste un fichier MD
- Compatible avec le système existant
- Aucun code Python à modifier

**Inconvénients:**
- Le template `agent.system.mcp_tools.md` ne contient que `{{tools}}`
- La logique de filtrage doit être dans le code qui génère `{{tools}}`
- Nécessite de surcharger la logique de génération, pas juste le template

### Option 2: Extension système qui override get_mcp_tools_prompt()
**Avantages:**
- Permet d'intercepter l'appel à `get_mcp_tools_prompt()`
- Peut filtrer les outils avec ToolRegistry avant de générer le prompt
- Plus propre, séparation des responsabilités

**Inconvénients:**
- Nécessite de comprendre le système d'extensions
- Plus complexe à implémenter

### Option 3: Surcharge de MCPConfig.get_tools_prompt()
**Avantages:**
- Intercepte directement la génération des outils
- Pas besoin de toucher au système de prompts

**Inconvénients:**
- Requiert monkey-patching ou substitution de classe

## 🤔 Décision préliminaire
**Option 2 recommandée:** Créer une extension dans `/a0/usr/extensions/` qui:
1. Se charge avant `_10_system_prompt.py`
2. Override `get_mcp_tools_prompt()`
3. Utilise ToolRegistry pour filtrer les outils par pertinence sémantique
4. Génère le prompt avec uniquement les outils filtrés

## 📝 Questions à valider
1. Comment l'extension accède-t-elle à la requête utilisateur pour le filtrage sémantique ?
2. Où stocker le ToolRegistry pour réutilisation ?
3. Comment mesurer la réduction de tokens ?

