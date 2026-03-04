# 🏗️ Solution: Intégration ToolRegistry dans les prompts système

## 📋 Problème
Actuellement, tous les outils MCP sont inclus dans le prompt système, ce qui:
- Consomme beaucoup de tokens (~613 tokens baseline)
- Rend le prompt moins focalisé
- Peut ralentir le traitement par le LLM

## 🎯 Solution proposée
Créer une extension qui:
1. Intercepte la génération du prompt des outils MCP
2. Utilise ToolRegistry pour filtrer les outils par pertinence sémantique
3. Génère un prompt optimisé avec uniquement les outils pertinents

## 🔧 Architecture technique

### Extension: `tool_registry_prompt_override.py`
```python
# /a0/usr/extensions/tool_registry_prompt_override.py

from typing import Any
from python.helpers.extension import Extension
from python.helpers.mcp_handler import MCPConfig
from agent import Agent, LoopData
from extensions.tool_registry import ToolRegistry

class ToolRegistryPromptOverride(Extension):
    """
    Extension qui filtre les outils MCP par pertinence sémantique
    avant leur inclusion dans le prompt système.
    """
    
    async def execute(self, system_prompt: list[str] = [], loop_data: LoopData = LoopData(), **kwargs: Any):
        """
        Override de la génération du prompt MCP.
        Remplacer le contenu de `agent.system.mcp_tools.md` par une version filtrée.
        """
        # Récupérer l'agent courant
        agent = self.agent
        
        # Récupérer la requête utilisateur depuis le contexte
        user_query = self._extract_user_query(loop_data)
        
        # Récupérer tous les outils MCP
        mcp_config = MCPConfig.get_instance()
        if not mcp_config.servers:
            return  # Pas d'outils MCP à filtrer
        
        # Générer le prompt filtré
        filtered_prompt = self._generate_filtered_prompt(agent, user_query, mcp_config)
        
        # Remplacer le prompt original dans la liste
        for i, prompt in enumerate(system_prompt):
            if "## Remote (MCP Server) Agent Tools" in prompt:
                system_prompt[i] = filtered_prompt
                break
        
    def _extract_user_query(self, loop_data: LoopData) -> str:
        """
        Extrait la requête utilisateur du contexte.
        """
        # À implémenter: extraire le dernier message utilisateur
        # ou utiliser une heuristique pour déterminer le contexte
        return loop_data.last_user_message or ""
        
    def _generate_filtered_prompt(self, agent, user_query: str, mcp_config) -> str:
        """
        Génère le prompt filtré avec ToolRegistry.
        """
        try:
            # Initialiser ToolRegistry
            registry = ToolRegistry()
            
            # Charger les outils depuis le fichier de registry
            import json
            tools_path = "/a0/usr/projects/agentzero_ameliorations/.a0proj/knowledge/tools_registry.json"
            with open(tools_path, 'r') as f:
                tools_data = json.load(f)
            
            # Indexer les outils si nécessaire
            if registry.get_tool_count() == 0:
                registry.index_tools(tools_data)
            
            # Filtrer les outils par pertinence
            relevant_tools = registry.search_tools(user_query, k=8)  # Top 8 outils
            
            # Toujours inclure certains outils essentiels
            essential_tools = ["response", "code_execution_tool", "call_subordinate"]
            for tool_name in essential_tools:
                tool = registry.get_tool_by_name(tool_name)
                if tool and tool not in relevant_tools:
                    relevant_tools.append(tool)
            
            # Générer le prompt formaté
            prompt_lines = ["## Remote (MCP Server) Agent Tools available:"]
            
            for tool in relevant_tools:
                name = tool.get('name', '')
                description = tool.get('description', '')
                
                # Format similaire au prompt original
                prompt_lines.append(f"### {name}")
                prompt_lines.append(f"{description}")
                
                # Ajouter le schéma d'entrée si disponible
                input_schema = tool.get('input_schema', {})
                if input_schema:
                    prompt_lines.append(f"\n#### Input schema for tool_args:")
                    prompt_lines.append(f"{input_schema}")
                
                prompt_lines.append(f"\n#### Usage:")
                prompt_lines.append(f"{{\n    \"thoughts\": [\"...\"],\n    \"tool_name\": \"{name}\",\n    \"tool_args\": !follow schema above\n}}")
                prompt_lines.append("")
            
            return "\n\n".join(prompt_lines)
            
        except Exception as e:
            # Fallback: retourner le prompt original
            print(f"ToolRegistry filtering failed: {e}")
            return agent.read_prompt("agent.system.mcp_tools.md")
```

### Configuration: `extension_settings.json`
```json
{
  "extensions": {
    "tool_registry_prompt_override": {
      "enabled": true,
      "order": 5,  // S'exécuter avant system_prompt (ordre 10)
      "max_tools": 8,
      "essential_tools": ["response", "code_execution_tool", "call_subordinate"],
      "min_tools_for_fallback": 3
    }
  }
}
```

## 🎯 Avantages

### Réduction de tokens
- **Baseline:** ~613 tokens (tous les outils)
- **Avec filtrage:** ~50-100 tokens (top 8 outils + essentiels)
- **Économie:** ~85% de tokens

### Améliorations
1. **Meilleure pertinence:** Seuls les outils pertinents sont présentés
2. **Performance LLM:** Moins de tokens = traitement plus rapide
3. **Précision:** Le LLM se focalise sur les outils utiles
4. **Expérience développeur:** Meilleure découverte d'outils

## ⚙️ Installation

1. **Créer l'extension:**
```bash
cp /a0/usr/extensions/tool_registry.py /a0/usr/extensions/tool_registry_prompt_override.py
```

2. **Configurer l'ordre d'exécution:**
```bash
# Modifier /a0/usr/settings.json pour inclure l'extension
```

3. **Tester:**
```bash
# Vérifier que l'extension se charge
# Tester avec différentes requêtes
# Mesurer la réduction de tokens
```

## 🔄 Réversibilité

### Désactivation simple
```json
{
  "extensions": {
    "tool_registry_prompt_override": {
      "enabled": false
    }
  }
}
```

### Fallback automatique
- Si ToolRegistry échoue, retour au prompt original
- Si < 3 outils trouvés, inclure plus d'outils
- Journalisation des erreurs pour debugging

## 📊 Métriques de validation

### Tests à effectuer
1. **Token count:** Comparer avant/après avec même requête
2. **Tool relevance:** Vérifier que les outils filtrés sont pertinents
3. **Performance:** Mesurer le temps d'exécution
4. **Fallback:** Tester avec ToolRegistry désactivé

### Critères de succès
- [ ] Réduction tokens > 50%
- [ ] Outils pertinents retournés
- [ ] Aucun outil essentiel manquant
- [ ] Fallback fonctionnel

## 🔍 Questions ouvertes

1. **Comment accéder à la requête utilisateur ?**
   - Solution: Extraire depuis `loop_data` ou contexte
   - Alternative: Utiliser le dernier message utilisateur

2. **Comment garantir l'ordre d'exécution ?**
   - Solution: Configurer `order` dans settings.json
   - Tester avec différentes valeurs

3. **Comment tester efficacement ?**
   - Solution: Script de test avec différentes requêtes
   - Comparaison side-by-side

