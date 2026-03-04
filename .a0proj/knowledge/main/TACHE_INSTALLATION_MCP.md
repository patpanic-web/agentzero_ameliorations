# 🎯 Tâche: Installation des MCP pour Agent Zero

## 📅 Date: 2026-03-04
## 📋 Source: Projet automatisation_torrent (restauration)

---

## 🎯 Objectif
Installer et configurer les MCP identifiés pour améliorer la sécurité et les capacités d'Agent Zero, en particulier pour les opérations Git et Docker.

---

## 📦 MCP à Installer

### 1. mcp-server-git (Priorité HAUTE)
**Pourquoi:** Éviter les erreurs de manipulation Git destructrices
**Source:** https://github.com/modelcontextprotocol/servers/tree/main/src/git

```bash
pip install mcp-server-git
# ou via uvx (pas besoin d'installation préalable)
uvx mcp-server-git --help
```

### 2. docker-mcp (Priorité HAUTE)
**Pourquoi:** Gestion sécurisée des containers Docker
**Source:** https://github.com/QuantGeekDev/docker-mcp

```bash
pip install docker-mcp
# ou via uvx
uvx docker-mcp --help
```

### 3. system-diag-mcp (Priorité MOYENNE)
**Pourquoi:** Diagnostic système avant opérations lourdes
**Source:** https://github.com/cdmx1/system-diag-mcp

```bash
pip install system-diag-mcp
```

---

## ⚙️ Configuration Agent Zero (IMPORTANT!)

### ⚠️ NE PAS utiliser claude_desktop_config.json
**Ce fichier est pour Claude Desktop, PAS pour Agent Zero!**

### ✅ Méthode Correcte pour Agent Zero

#### Option 1: Via l'Interface UI (Recommandé)
1. Ouvrir Agent Zero Web UI
2. Aller dans **Settings** → **MCP/A2A**
3. Cliquer sur **External MCP Servers**
4. Cliquer **Open** pour éditer la configuration
5. Ajouter la configuration ci-dessous
6. Cliquer **Apply now**

#### Option 2: Édition directe de usr/settings.json
Le fichier de configuration est:
```
/a0/usr/settings.json
```

Clé à modifier: `"mcp_servers"`

---

## 📝 Configuration à Ajouter

```json
{
  "mcpServers": {
    "git": {
      "command": "uvx",
      "args": ["mcp-server-git", "--repository", "/a0/usr/projects"]
    },
    "docker-mcp": {
      "command": "uvx",
      "args": ["docker-mcp"]
    },
    "system-diag": {
      "command": "python",
      "args": ["-m", "system_diag_mcp"]
    }
  }
}
```

### Format dans settings.json
Dans `settings.json`, la valeur est stockée comme une **string JSON échappée**:

```json
{
  "mcp_servers": "{\"mcpServers\": {\"git\": {\"command\": \"uvx\", \"args\": [\"mcp-server-git\"]}, \"docker-mcp\": {\"command\": \"uvx\", \"args\": [\"docker-mcp\"]}, \"system-diag\": {\"command\": \"python\", \"args\": [\"-m\", \"system_diag_mcp\"]}}}"
}
```

> 💡 **L'UI gère automatiquement l'échappement!** Utiliser l'UI pour éviter les erreurs.

---

## ✅ Checklist d'Installation

### Phase 1: Installation des packages
```bash
# Vérifier environnement Python
which python && python --version

# Installer les MCP
pip install mcp-server-git docker-mcp system-diag-mcp

# Vérifier installation
pip list | grep -E "mcp|docker"
```

### Phase 2: Configuration via UI
1. Ouvrir Agent Zero Web UI
2. Settings → MCP/A2A → External MCP Servers → Open
3. Ajouter la configuration JSON
4. Apply now

### Phase 3: Vérification
1. Vérifier le statut des serveurs (indicateur vert = connecté)
2. Vérifier que les outils apparaissent dans la liste
3. Les outils seront nommés: `git.status`, `docker_mcp.list_containers`, etc.

### Phase 4: Tests
```bash
# Tester mcp-server-git
uvx mcp-server-git --help

# Tester docker-mcp  
uvx docker-mcp --help

# Vérifier Docker
docker ps
```

---

## 📊 Outils Fournis par les MCP

### mcp-server-git → Préfixe: `git.`
| Outil | Description |
|-------|-------------|
| `git.git_status` | État du repository |
| `git.git_log` | Historique commits |
| `git.git_diff` | Différences |
| `git.git_commit` | Créer commit (validé) |
| `git.git_branch` | Gestion branches |
| `git.git_rebase` | Rebase (protégé) |

### docker-mcp → Préfixe: `docker_mcp.`
| Outil | Description |
|-------|-------------|
| `docker_mcp.list_containers` | Lister containers |
| `docker_mcp.get_container_logs` | Logs container |
| `docker_mcp.deploy_compose_stack` | Déployer compose |
| `docker_mcp.get_container_stats` | Stats ressources |

### system-diag → Préfixe: `system_diag.`
| Outil | Description |
|-------|-------------|
| `system_diag.check_disk_usage` | Usage disque |
| `system_diag.check_memory` | RAM/Swap |
| `system_diag.check_cpu_usage` | Usage CPU |

---

## 🔒 Règles de Sécurité

### Pour l'Installation
1. **Backup settings.json** avant modification:
```bash
cp /a0/usr/settings.json /a0/usr/settings.json.bak
```

2. **Tester un MCP à la fois** - ne pas tous les activer d'un coup

### Règle No-Core-Change
Ce projet respecte la règle absolue:
- ✅ Configuration externe via settings.json
- ✅ MCP externes via uvx/npx
- ❌ **JAMAIS** modifier le code source d'Agent Zero

---

## 🚀 Commandes Rapides

```bash
# Installation complète
pip install mcp-server-git docker-mcp system-diag-mcp && echo "✅ MCP installés"

# Vérification
pip show mcp-server-git docker-mcp system-diag-mcp
```

---

## 📚 Références

- **Doc Agent Zero MCP:** `/a0/docs/guides/mcp-setup.md`
- **Doc avancée:** `/a0/docs/developer/mcp-configuration.md`
- **Settings file:** `/a0/usr/settings.json`

---

## 📝 Notes Importantes

- Ces MCP ont été identifiés suite à un incident sur le projet `automatisation_pour_telecharger_des_films_torrent`
- L'agent avait fait un rebase Git mal géré qui a bloqué le projet
- Ces outils permettront d'éviter ce type d'erreur à l'avenir
- **Toujours utiliser l'UI pour la configuration** pour éviter les erreurs d'échappement JSON

---

*Document préparé par Agent Zero principal*
*Correction: Configuration spécifique à Agent Zero (pas Claude Desktop)*
