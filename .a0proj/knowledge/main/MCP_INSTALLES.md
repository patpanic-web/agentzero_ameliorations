# 📦 MCP Installés pour Agent Zero

## 📅 Date d'installation: 2026-03-04

---

## ✅ MCP Configurés (5 total)

| MCP | Statut | Commande | Description |
|-----|--------|----------|-------------|
| tavily | ✅ Actif | `npx -y tavily-mcp@latest` | Recherche web agentique |
| playwright | ✅ Actif | `npx -y @playwright/mcp@latest` | Automatisation navigateur |
| **git** | ✅ Configuré | `uvx mcp-server-git --repository ...` | Opérations Git sécurisées |
| **docker-mcp** | ✅ Configuré | `uvx docker-mcp` | Gestion containers Docker |
| **system-diag** | ✅ Configuré | `/opt/venv-a0/bin/system-diag-mcp` | Diagnostic système Ubuntu |

---

## 🔧 Corrections Appliquées

### Erreur 1: git MCP - "not a valid Git repository"
**Problème:** Le chemin `/a0/usr/projects` n'est pas un repo Git.
**Solution:** Pointé vers le repo valide `/a0/usr/projects/automatisation_pour_telecharger_des_films_torrent`

### Erreur 2: system-diag MCP - "Command not found"
**Problème:** `system-diag-mcp` installé dans `/opt/venv` mais Agent Zero utilise `/opt/venv-a0`.
**Solution:**
1. Installé le package dans venv-a0: `/opt/venv-a0/bin/pip install system-diag-mcp`
2. Utilisé le chemin absolu: `/opt/venv-a0/bin/system-diag-mcp`

---

## ⚙️ Configuration Finale (settings.json)

```json
{
  "mcpServers": {
    "tavily": {
      "command": "npx",
      "args": ["-y", "tavily-mcp@latest"],
      "env": { ... },
      "description": "Tavily Web Search MCP"
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"],
      "description": "Playwright MCP"
    },
    "git": {
      "command": "uvx",
      "args": ["mcp-server-git", "--repository", "/a0/usr/projects/automatisation_pour_telecharger_des_films_torrent"],
      "description": "Git operations MCP"
    },
    "docker-mcp": {
      "command": "uvx",
      "args": ["docker-mcp"],
      "description": "Docker MCP"
    },
    "system-diag": {
      "command": "/opt/venv-a0/bin/system-diag-mcp",
      "args": [],
      "description": "System Diagnostics MCP"
    }
  }
}
```

---

## 🔄 Activation

**Redémarrer Agent Zero** pour appliquer les corrections.

---

## 📝 Notes Techniques

- **venv Agent Zero:** `/opt/venv-a0` (Python 3.12)
- **venv système:** `/opt/venv` (Python 3.13)
- **Backup:** `/a0/usr/settings.json.bak`
- **Règle respectée:** No-Core-Change (configuration externe uniquement)

---

*Document mis à jour automatiquement par Agent Zero*
