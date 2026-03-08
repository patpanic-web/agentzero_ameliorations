# SPECIFICATION IMPLEMENTATION — T2 Fallback Tavily

> **For**: James | Developer  
> **Date**: 2026-03-08  
> **Architecture**: Skill-Based, Stateless, Per-Request Fallback

---

## 🎯 OBJECTIF FINAL

Créer `/a0/usr/skills/tavily-fallback/` avec un wrapper qui :
1. **Essaye Tavily** pour chaque requête
2. **Fallback immédiat** sur `search_engine` si Tavily échoue
3. **Pas d'etat entre requêtes** — Tavily re-testé à chaque appel

---

## 📁 STRUCTURE À CRÉER

```
/a0/usr/skills/tavily-fallback/
├── SKILL.md                          # (TU) Usage + configuration
├── config/
│   └── fallback.yaml                 # (TU) Options: timeout, retry
└── scripts/
    └── fallback_search.py            # (TU) Wrapper principal
```

---

## 🔧 IMPLEMENTATION DÉTAILLÉE

### 1. config/fallback.yaml

```yaml
# Configuration du fallback Tavily
# Mode: always_try_primary = tavily teste a chaque requete

primary:
  provider: tavily
  timeout_seconds: 15
  max_retries: 0  # Pas de retry, fallback immediat

fallback:
  provider: search_engine
  timeout_seconds: 30

# Pas de circuit breaker — stateless par design
logging:
  level: info
  log_fallback_events: true
```

### 2. scripts/fallback_search.py

**Pattern à implémenter**:
```python
#!/usr/bin/env python3
"""
Fallback Search Wrapper — Stateless per-request fallback
Usage: python fallback_search.py "query string" [options]
"""
import sys
import json
import logging
from typing import Optional, Dict, Any

# Configuration
TAVILY_TIMEOUT = 15
FALLBACK_TIMEOUT = 30

def search_with_fallback(query: str) -> Dict[str, Any]:
    """
    Pattern CRITIQUE: stateless, pas de memoire entre appels
    """
    # ESSAI 1: Tavily (toujours essayer d'abord)
    try:
        result = call_tavily(query, timeout=TAVILY_TIMEOUT)
        if result and not result.get('error'):
            log.info(f"Tavily OK: {query[:50]}...")
            return format_result(result, source='tavily')
    except Exception as e:
        log.warning(f"Tavily failed: {e}")
    
    # FALLBACK: search_engine natif (immediate, pas de retry)
    log.info(f"Fallback to search_engine: {query[:50]}...")
    try:
        result = call_search_engine(query, timeout=FALLBACK_TIMEOUT)
        return format_result(result, source='search_engine', fallback=True)
    except Exception as e:
        log.error(f"Both failed: {e}")
        return {'error': str(e), 'query': query}

def call_tavily(query: str, timeout: int) -> Any:
    # Via subprocess ou MCP call
    pass

def call_search_engine(query: str, timeout: int) -> Any:
    # Via subprocess ou direct call
    pass
```

**POINT CLÉ**: Pas de variable globale, pas de compteur d'echecs. Chaque appel est indépendant.

### 3. SKILL.md

Sections obligatoires:
- Usage: comment appeler le skill
- Configuration: modifier fallback.yaml
- Désactivation: `mv skill.disabled`
- Troubleshooting: logs dans /a0/usr/skills/tavily-fallback/logs/

---

## ✅ TESTS E2E REQUIS

### Test 1: Tavily OK (baseline)
```bash
python scripts/fallback_search.py "test query"
# Attendu: resultat Tavily, pas de fallback loggue
```

### Test 2: Tavily FAIL → Fallback
```bash
# Simuler echec: modifier config timeout=0.001 ou deconnecter
python scripts/fallback_search.py "test query"  
# Attendu: resultat search_engine, log "Fallback to search_engine"
```

### Test 3: Recovery (requête suivante)
```bash
# Revenir config normale
python scripts/fallback_search.py "another query"
# Attendu: Tavily fonctionne de nouveau (pas de memoire d'echec)
```

---

## 🚫 ANTI-PATTERNS À ÉVITER

- ❌ Circuit breaker avec compteur d'echecs
- ❌ Timer de cooldown
- ❌ Variable globale "tavily_healthy = False"
- ❌ Health check periodique
- ❌ Retry multiple sur Tavily

✅ **Seul pattern acceptable**: Try Tavily → Fail → Immediate Fallback → Return

---

## 💾 PERSISTANCE

- Skill dans `/a0/usr/skills/` → persistant (monté Docker)
- Tests avec `docker-compose restart` pour valider

---

**James**: Implemente UNIQUEMENT ce qui est specifié ici. Validation PO deja faite sur le mecanisme per_request.
