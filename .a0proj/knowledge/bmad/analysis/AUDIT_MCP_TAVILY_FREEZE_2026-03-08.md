# 🔍 Audit MCP Tavily — Figeages et Solutions

**Date**: 2026-03-08  
**Statut**: Investigation complète, décision PO prise  
**Responsable**: Agent Zero  
**Prochaine action**: À déterminer par PO si récidive

---

## 🚨 Problème Signalé

**Symptôme**: Agent Zero fige lors de l'utilisation des MCP Tools, notamment Tavily.

**Fréquence**: Récurrent, nécessite redémarrage manuel.

---

## 🔬 Diagnostic Technique

### Configuration MCP Actuelle

```json
{
  "mcp_server_enabled": false,
  "mcp_client_init_timeout": 10,
  "mcp_client_tool_timeout": 120,
  "mcpServers": {
    "tavily": {
      "command": "npx -y tavily-mcp@latest",
      "env": { "TAVILY_API_KEY": "tvly-dev-..." }
    },
    "qnap": { "command": "/a0/usr/mcp/qnap/qmcp", ... },
    "docker-mcp": { "disabled": true }
  }
}
```

### Causes Identifiées

| Cause | Sévérité | Détail |
|-------|----------|--------|
| **Démarrage npx lent** | 🔴 Haute | Tavily MCP démarre via `npx` ( téléchargement à froid = 10-60s) |
| **Timeout MCP court** | 🔴 Haute | 120s parfois insuffisant avec démarrage npx |
| **Memory consolidation** | ⚠️ Moyenne | Timeout 60s, possible conflit avec MCP timeout |
| **MCP serveur désactivé** | 🟢 Info | `mcp_server_enabled: false` (expose outils A0, pas problème ici) |

### Tests Effectués

| Test | Résultat | Commentaire |
|------|----------|-------------|
| Tavily MCP manuel | 🔴 `unknown` / erreur JSON | Échec démarrage |
| QNAP MCP | 🟢 OK | Initialize réussi |
| Tavily API directe | 🟢 **1.04s** | Skill tavily-fallback validé |
| Memory consolidation | ⚠️ Timeout 60s | Code source confirmé |

---

## ✅ Solutions Validées

### Solution 1: Skill Tavily-Fallback (T2)

**Fichier**: `/a0/usr/skills/tavily-fallback/`  
**Statut**: ✅ Fonctionnel, testé 2026-03-08  
**Performance**: ~1s vs 10-60s MCP  
**Fallback**: DuckDuckGo si Tavily API échoue

**Désactivation Tavily MCP**:
```json
{
  "mcpServers": {
    "tavily": {
      "command": "npx -y tavily-mcp@latest",
      "disabled": true  ← AJOUTER
    }
  }
}
```

### Solution 2: API Tavily Directe (Python)

**Package**: `tavily-python`  
**Commande**: `pip install tavily-python`  
**Usage**: Client Python natif, pas de npx  
**Fonctionnalités**: `search()` nativement, autres via HTTP manuel

### Solution 3: Hybride MCP + API

**Concept**: Search rapide (API) + Extract/Crawl/Map/Research (MCP)  
**Bénéfice**: Performance + fonctionnalités avancées  
**Implémentation**: Renommer outils, router via skill  
**Complexité**: Moyenne (modification skill requise)

---

## 📊 Comparaison Solutions

| Critère | MCP Actuel | Skill T2 | API Directe | Hybride |
|---------|------------|----------|-------------|---------|
| Latence | 10-60s ❌ | ~1s ✅ | ~1s ✅ | Mixte |
| Fiabilité | 🔴 Fige | 🟢 Stable | 🟢 Stable | 🟢 Stable |
| Search | ✅ | ✅ | ✅ | ✅ Rapide |
| Extract | ✅ | ❌ | ⚠️ Manuel | ✅ |
| Crawl/Map/Research | ✅ | ❌ | ⚠️ Manuel | ✅ |
| Complexité | Basse | Basse | Moyenne | Moyenne |
| No-Core-Change | ✅ | ✅ | ✅ | ✅ |

---

## 🎯 Décision Product Owner (2026-03-08)

**Choix**: Maintenir configuration actuelle (Tavily MCP), ne pas migrer.

**Justification**:
- Préserver fonctionnalités avancées (extract, crawl, map, research)
- Éviter risque régression pendant investigation
- Skill tavily-fallback disponible comme filet

**Réversibilité**: Oui, désactivation MCP possible immédiatement.

---

## 📝 Actions Futures (Backlog)

| Action | Condition | Priorité | Estimation |
|--------|-----------|----------|------------|
| Activer skill tavily-fallback | Prochain figeage Tavily | 🔴 Haute | 5 min |
| Désactiver Tavily MCP | Si skill validé | 🟡 Moyenne | 2 min |
| Implémenter extract natif | Si besoin extraction fréquente | 🟢 Basse | 2h |
| Migrer hybride complet | Si besoin perf + features | 🟢 Basse | 4h |

---

## 🔧 Escape Hatch (Procédure d'Urgence)

**Si figeage MCP Tavily**:
```bash
# 1. Stop Agent Zero

# 2. Désactiver Tavily MCP
python3 << 'PYEOF'
import json
with open('/a0/usr/settings.json', 'r') as f:
    d = json.load(f)
mcp = json.loads(d['mcp_servers'])
mcp['mcpServers']['tavily']['disabled'] = True
d['mcp_servers'] = json.dumps(mcp, indent=2)
with open('/a0/usr/settings.json', 'w') as f:
    json.dump(d, f, indent=2)
print("Tavily MCP désactivé")
PYEOF

# 3. Redémarrer Agent Zero
# 4. Skill tavily-fallback actif automatiquement
```

---

## 📁 Références

- **Skill**: `/a0/usr/skills/tavily-fallback/SKILL.md`
- **Logs**: `/a0/usr/skills/tavily-fallback/logs/fallback_search.log`
- **Config**: `/a0/usr/settings.json`
- **Solution T2**: `.a0proj/knowledge/solutions/T2_TAVILY_FALLBACK_SPEC.md`

---

## 🏷️ Tags

`mcp`, `tavily`, `freeze`, `timeout`, `monitoring`, `skill`, `t2`, `deferred`

---

*Document créé par Agent Zero le 2026-03-08*  
*Prochaine révision: Sur décision PO ou récidive*
