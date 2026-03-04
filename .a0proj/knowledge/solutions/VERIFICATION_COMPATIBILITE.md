# Vérification de Compatibilité - Architecture Multi-Modèles

## ✅ Conclusion : Configuration 100% Compatible

L'architecture proposée est **entièrement compatible** avec Agent Zero v0.9.8+.

---

## 🔍 Analyse Technique Détaillée

### 1. Mécanisme de Surcharge des Settings

**Extension concernée** : `/a0/python/extensions/agent_init/_15_load_profile_settings.py`

```python
# L'extension recherche settings.json dans les répertoires de profils
config_files = subagents.get_paths(self.agent, "settings.json", ...)

# Si trouvé, elle crée une nouvelle config avec les overrides
new_config = initialize_agent(override_settings=settings_override)
```

**Ordre de priorité** (du plus haut au plus bas) :
1. `/a0/usr/projects/<project>/.a0proj/agents/<profile>/settings.json` (projet)
2. `/a0/usr/agents/<profile>/settings.json` (utilisateur) ← **Recommandé**
3. `/a0/agents/<profile>/settings.json` (défaut framework)

### 2. Granularité des Settings Supportés

**Tous ces paramètres sont surchargeables par profil** :

| Catégorie | Paramètres |
|-----------|-----------|
| **Chat Model** | `chat_model_provider`, `chat_model_name`, `chat_model_api_base`, `chat_model_kwargs`, `chat_model_ctx_length`, `chat_model_vision` |
| **Util Model** | `util_model_provider`, `util_model_name`, `util_model_api_base`, `util_model_kwargs`, `util_model_ctx_length` |
| **Browser Model** | `browser_model_provider`, `browser_model_name`, `browser_model_api_base`, `browser_model_vision` |
| **Embed Model** | `embed_model_provider`, `embed_model_name`, `embed_model_api_base` |
| **Rate Limits** | `*_rl_requests`, `*_rl_input`, `*_rl_output` |

### 3. État Actuel de la Configuration

**Fichier** : `/a0/usr/settings.json`

```
chat_model:  GLM-5 (OpenRouter) → $1.48/1M tokens mixte
util_model:  Llama-4-Scout → $0.15/1M tokens mixte
browser_model: DeepSeek V3.2 → DÉJÀ OPTIMISÉ! ✅
embed_model:  HuggingFace (local) → Gratuit ✅
```

**Répertoires agents** :
- `/a0/agents/` → Profils par défaut (agent0, developer, hacker, researcher)
- `/a0/usr/agents/` → **Vide** → Emplacement idéal pour les overrides utilisateur

### 4. Prompts Personnalisés par Profil

**Emplacement** : `/a0/usr/agents/<profile>/prompts/`

**Mécanisme** : Les prompts dans ce répertoire surchargent ceux de `/a0/prompts/` et `/a0/agents/<profile>/prompts/`.

**Fichiers modifiables** :
- `agent.system.main.role.md` → Rôle et comportement
- `agent.system.main.solving.md` → Méthodologie de résolution
- `agent.system.main.behaviour.md` → Règles comportementales

---

## 📐 Architecture Recommandée (Vérifiée Compatible)

### Structure des Fichiers à Créer

```
/a0/usr/agents/
├── developer/
│   ├── settings.json          ← Modèle économique (DeepSeek)
│   └── prompts/
│       └── (optionnel)        ← Prompts personnalisés
├── hacker/
│   ├── settings.json          ← Modèle économique (Gemini Flash)
│   └── prompts/
├── researcher/
│   ├── settings.json          ← Modèle économique (DeepSeek)
│   └── prompts/
└── agent0/
    └── prompts/
        └── agent.system.main.role.md  ← Prompts délégation forcée
```

### Exemple de settings.json pour Subordonné

**Fichier** : `/a0/usr/agents/developer/settings.json`

```json
{
  "chat_model_provider": "openrouter",
  "chat_model_name": "deepseek/deepseek-v3.2",
  "chat_model_ctx_length": 64000,
  "chat_model_vision": false
}
```

### Exemple de Prompt pour Délégation Forcée

**Fichier** : `/a0/usr/agents/agent0/prompts/agent.system.main.role.md`

```markdown
## Delegation Policy (CRITICAL)

ALWAYS delegate to specialized subordinates when:
- Writing unit tests, boilerplate code, documentation
- Performing repetitive tasks or bulk operations
- Executing standard security scans or audits
- Conducting research or data gathering

PREFER subordinates for execution tasks.
Your role is PLANNING and SUPERVISION, not execution.
```

---

## ⚠️ Points d'Attention Technique

### 1. Ne Pas Modifier les Fichiers Core

❌ **À éviter** :
- Modifier `/a0/agents/<profile>/agent.json` (metadata seulement)
- Modifier `/a0/prompts/*.md` (serait écrasé lors des updates)
- Modifier les fichiers Python du framework

✅ **Recommandé** :
- Créer `/a0/usr/agents/<profile>/settings.json`
- Créer `/a0/usr/agents/<profile>/prompts/*.md`

### 2. Compatibilité avec les Projects

Les settings peuvent aussi être définis au niveau projet :
`/a0/usr/projects/<project>/.a0proj/agents/<profile>/settings.json`

**Priorité** : Projet > Utilisateur > Défaut

### 3. Rate Limiting

Les subordonnés héritent des rate limits globaux sauf si override :
```json
{
  "chat_model_rl_requests": 0,
  "chat_model_rl_input": 0,
  "chat_model_rl_output": 0
}
```

---

## ✅ Checklist de Compatibilité

| Critère | Status | Notes |
|---------|--------|-------|
| Settings override par profil | ✅ | Extension `_15_load_profile_settings.py` |
| Prompts override par profil | ✅ | Système de merge automatique |
| Emplacement utilisateur (non-core) | ✅ | `/a0/usr/agents/` |
| Paramètres modèle surchargeables | ✅ | Tous les `*_model_*` |
| Compatibilité upgrades | ✅ | Fichiers séparés du core |
| Projects support | ✅ | Priorité projet > user > default |

---

## 🚀 Implémentation Recommandée

### Phase 1 : Configuration des Modèles
1. Créer `/a0/usr/agents/developer/settings.json`
2. Créer `/a0/usr/agents/hacker/settings.json`
3. Créer `/a0/usr/agents/researcher/settings.json`

### Phase 2 : Délégation Forcée
1. Créer `/a0/usr/agents/agent0/prompts/agent.system.main.role.md`
2. Tester le comportement de délégation

### Phase 3 : Validation
1. Vérifier les logs de chargement des settings
2. Mesurer les coûts réels
3. Ajuster les prompts si nécessaire

---

**Date de vérification** : 2026-03-04
**Agent Zero version** : v0.9.8.2
**Status** : ✅ COMPATIBLE - Prêt pour implémentation
