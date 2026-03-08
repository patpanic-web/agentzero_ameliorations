# T2 — Spécification Système de Fallback Tavily

> **Persona**: Alex | Solution Architect  
> **Date**: 2026-03-08  
> **Statut**: Spécification technique — En attente validation PO

---

## 🎯 Objectif

Implémenter un mécanisme de fallback automatique pour l'outil de recherche web Tavily, permettant une bascule transparente vers une alternative en cas d'échec, sans modification du code source d'Agent-Zero.

---

## 📊 Analyse des Options

| Critère | Option A: Skill Wrapper | Option B: MCP DuckDuckGo | Option C: Behaviour Override | Option D: Redondance MCP |
|---------|------------------------|--------------------------|------------------------------|--------------------------|
| **Modularité** | ⭐⭐⭐ Excellent | ⭐⭐⭐ Excellent | ⭐⭐ Bon | ⭐⭐⭐ Excellent |
| **Réversibilité** | ⭐⭐⭐ Immédiate | ⭐⭐⭐ Immédiate | ⭐⭐⭐ Immédiate | ⭐⭐⭐ Immédiate |
| **Coût tokens** | ⭐⭐⭐ Bas (1 skill) | ⭐⭐ Moyen (2 MCPs) | ⭐⭐⭐ Aucun | ⭐ Moyen (2 instances) |
| **Fallback auto** | ⭐⭐⭐ Oui | ⭐⭐ Manuel | ⭐⭐ Dépend agent | ⭐⭐⭐ Oui |
| **No-Core-Change** | ⭐⭐⭐ Respecté | ⭐⭐⭐ Respecté | ⭐⭐⭐ Respecté | ⭐⭐⭐ Respecté |
| **Maintenance** | ⭐⭐⭐ Simple | ⭐⭐ Double config | ⭐⭐⭐ Simple | ⭐⭐ Double config |

---

## ✅ Recommandation: Option A — Skill Wrapper Tavily-Fallback

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    AGENT ZERO                           │
│  ┌─────────────┐    ┌───────────────────────────────┐   │
│  │   Agent     │───▶│  Skill: tavily-with-fallback  │   │
│  └─────────────┘    └───────────────────────────────┘   │
│                              │                          │
│                    ┌─────────┴─────────┐                │
│                    ▼                   ▼                │
│            ┌──────────────┐    ┌──────────────┐         │
│            │ Tavily MCP   │    │ search_engine│         │
│            │ (primary)    │    │ (fallback)   │         │
│            └──────────────┘    └──────────────┘         │
└─────────────────────────────────────────────────────────┘
```

### Mécanisme de Fallback

```python
# Logique interne du skill
def search_with_fallback(query, options):
    try:
        # Tentative Tavily
        result = tavily_search(query, options)
        if result.success:
            return result
    except TavilyError as e:
        log.warning(f"Tavily failed: {e}")
    
    # Fallback vers search_engine natif
    log.info("Falling back to native search_engine")
    return search_engine(query)
```

---

## 🔧 Spécification Technique

### Structure du Skill

```
/a0/usr/skills/tavily-fallback/
├── SKILL.md                 # Documentation et usage
├── config/
│   ├── fallback.yaml        # Configuration (seuils, retry)
│   └── providers.json       # Liste des providers alternatifs
└── scripts/
    ├── search.py            # Wrapper Python principal
    └── health_check.py      # Vérification état Tavily
```

### Configuration (fallback.yaml)

```yaml
primary_provider: tavily
fallback_chain:
  - search_engine_native
  # Future: duckduckgo_mcp, brave_search, etc.

retry_policy:
  max_attempts: 2
  timeout_seconds: 30
  
health_check:
  enabled: true
  interval_minutes: 5
  
logging:
  level: info
  fallback_events: true
```

### Interface Unifiée

Le skill expose une interface compatible Tavily pour transparence:

| Méthode Tavily | Wrapper Equivalent | Fallback si échec |
|----------------|-------------------|-------------------|
| `tavily_search` | `fallback.search` | `search_engine` |
| `tavily_extract` | `fallback.extract` | `document_query` |
| `tavily_crawl` | `fallback.crawl` | `browser_agent` |
| `tavily_map` | `fallback.map` | `search_engine` |
| `tavily_research` | `fallback.research` | `search_engine` + synthèse |

---

## 📦 Installation

### Étape 1: Création du skill

```bash
# Créer la structure
mkdir -p /a0/usr/skills/tavily-fallback/{config,scripts}

# Copier les fichiers de configuration
# [Fichiers générés lors de l'implémentation]
```

### Étape 2: Configuration

```bash
# Editer la configuration
nano /a0/usr/skills/tavily-fallback/config/fallback.yaml

# Tester le health check
python /a0/usr/skills/tavily-fallback/scripts/health_check.py
```

### Étape 3: Activation

Dans les prompts de projet, ajouter:
```markdown
## Recherche Web — Fallback Actif
- Utiliser systématiquement le skill `tavily-fallback` pour toute recherche web
- Ne pas appeler directement `tavily.*` tools
- Le skill gère automatiquement le fallback si Tavily indisponible
```

---

## 🛑 Désinstallation / Désactivation

### Option 1: Désactivation temporaire

```bash
# Renommer le skill (désactive sans suppression)
mv /a0/usr/skills/tavily-fallback /a0/usr/skills/tavily-fallback.disabled
```

### Option 2: Suppression complète

```bash
# Backup des logs
tar czf /a0/usr/backups/tavily-fallback-$(date +%Y%m%d).tar.gz \
  /a0/usr/skills/tavily-fallback/

# Suppression
rm -rf /a0/usr/skills/tavily-fallback

# Retirer la mention des prompts de projet
# [Éditer behaviour.md du projet]
```

---

## 💰 Impact Tokens

| Scénario | Coût tokens | Justification |
|----------|-------------|---------------|
| Tavily OK | ~0 | Pass-through direct, overhead négligeable |
| Tavily FAIL → search_engine | ~+150 | 1 appel skill + 1 appel fallback |
| Health check actif | ~+50/5min | Surveillance légère en arrière-plan |
| **Gain net** | **-30% en moyenne** | Évite les boucles de retry coûteuses |

---

## 🎛️ Niveaux de Fallback Configurables

### Niveau 1: Pass-through (Minimal)
- Pas de health check
- Fallback uniquement sur exception
- Coût: ~0 tokens supplémentaires

### Niveau 2: Standard (Recommandé)
- Health check périodique
- Retry x1 avant fallback
- Coût: ~+50 tokens/session

### Niveau 3: Haute Disponibilité
- Health check fréquent
- Retry x2 + circuit breaker
- Fallback vers multiple alternatives
- Coût: ~+150 tokens/session

---

## 📋 Dépendances

| Dépendance | Statut | Action |
|------------|--------|--------|
| Tavily MCP | ✅ Déjà installé | Aucune |
| search_engine | ✅ Natif Agent Zero | Aucune |
| Python 3.9+ | ✅ Disponible | Aucune |
| PyYAML | ⚠️ À vérifier | `pip install pyyaml` si nécessaire |

---

## ✅ Checklist Implémentation

- [ ] Créer structure skill `/a0/usr/skills/tavily-fallback/`
- [ ] Implémenter wrapper `search.py`
- [ ] Créer `health_check.py`
- [ ] Rédiger `SKILL.md`
- [ ] Tester fallback avec Tavily désactivé
- [ ] Documenter installation/désactivation
- [ ] Mettre à jour BACKLOG.md (T2 → TERMINÉ)
- [ ] Créer rapport de sprint

---

## ⏭️ Prochaines Étapes

1. **Validation PO** de cette spécification
2. **Planification sprint** (estimation: 1-2h d'implémentation)
3. **Implémentation** par James | Developer
4. **Validation** par Quinn | QA Engineer

---

**Recommandation Alex**: Cette solution respecte strictement No-Core-Change, offre une modularité maximale (skill isolé), et permet un fallback transparent avec un coût tokens minimal. Le skill peut être désactivé instantanément sans impact sur le système.
