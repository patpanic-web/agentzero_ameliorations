# ⚙️ Configuration des Subordonnés

> **Dernière mise à jour**: 2026-03-05 (Sprint 4 — Audit et validation modèles)
> **Validation**: Tous les modèles vérifiés actifs sur OpenRouter (mars 2026)

---

## 📊 Configuration Actuelle (Validée)

| Profil | Provider | Modèle | Contexte | Vision | Statut |
|--------|----------|--------|----------|--------|--------|
| **agent0** | openrouter | `anthropic/claude-sonnet-4.6` | 100K | ✅ | ✅ Actif |
| **developer** | openrouter | `deepseek/deepseek-v3.2` | 64K | ❌ | ✅ TOP 4 OpenRouter |
| **hacker** | openrouter | `google/gemini-3-flash-preview` | 1M | ✅ | ✅ TOP 3 OpenRouter |
| **researcher** | openrouter | `openai/gpt-4o-mini` | 128K | ❌ | ✅ Actif |

> 📌 **Règle PO** : Les modèles ne sont changés que sur décision explicite du PO.
> Agent0 est toujours configuré manuellement via l'interface utilisateur.

---

## 🎯 Justification des Choix

### Agent0 (Orchestration, Raisonnement, Interaction PO)
- **Claude Sonnet 4.6** : Meilleur raisonnement, orchestration multi-agents, vision
- **Contrôle** : Manuel via UI uniquement — ne pas modifier par code
- **Coût** : ~$3 input / $15 output par million de tokens

### Developer (Code, Tests, Débogage)
- **DeepSeek V3.2** : TOP 4 des modèles les plus utilisés sur OpenRouter (mars 2026)
- Tool-use intégré, raisonnement fort, excellent pour le code
- **Coût** : ~$0.55 input / $2.19 output par million de tokens
- **Alternative premium** : `anthropic/claude-sonnet-4.6` ($3/$15/1M)
- **Alternative économique** : `qwen/qwen3-coder` (forte montée en 2026)

### Hacker (Sécurité, Pentest, Audits)
- **Gemini 3 Flash Preview** : TOP 3 sur OpenRouter, 1M contexte, vision intégrée
- Multimodal : analyse de captures d'écran et diagrammes réseau
- **Coût** : ~$0.50 input / $3 output par million de tokens
- **Alternative** : `deepseek/deepseek-v3.2` (open source)

### Researcher (Recherche, Documentation, Rapports)
- **GPT-4o-mini** : Rapide, économique, bon pour synthèse et structuration
- **Coût** : ~$0.15 input / $0.60 output par million de tokens
- **Alternative qualité** : `deepseek/deepseek-v3.2`
- **Alternative économique** : `minimax/minimax-m2.5` (TOP 1 OpenRouter mars 2026)

---

## 🔄 Comment Modifier un Modèle

### Via Agent Zero (Recommandé)

Dites simplement au PO :
```
"Change developer vers [modèle OpenRouter]"
"Change hacker vers deepseek/deepseek-v3.2"
"Change researcher vers openai/gpt-4o"
```

### Via Fichier Manuel

1. Ouvrir le fichier correspondant :
   - `/a0/usr/agents/developer/settings.json`
   - `/a0/usr/agents/hacker/settings.json`
   - `/a0/usr/agents/researcher/settings.json`

2. Modifier les valeurs :
   ```json
   {
     "chat_model_provider": "openrouter",
     "chat_model_name": "nouveau-modele",
     "chat_model_ctx_length": 64000,
     "chat_model_vision": false
   }
   ```

3. Redémarrer le chat pour appliquer

### Rollback (retour config par défaut)

```bash
# Supprimer l'override d'un profil spécifique
rm -rf /a0/usr/agents/developer
rm -rf /a0/usr/agents/hacker
rm -rf /a0/usr/agents/researcher

# Ou supprimer TOUS les overrides
rm -rf /a0/usr/agents/*
```

Après suppression, le profil utilise les paramètres globaux de l'UI.

---

## 📂 Fichiers de Configuration

| Fichier | Description |
|---------|-------------|
| `/a0/usr/settings.json` | Config globale Agent0 (UI) |
| `/a0/usr/agents/developer/settings.json` | Override profil Developer |
| `/a0/usr/agents/hacker/settings.json` | Override profil Hacker |
| `/a0/usr/agents/researcher/settings.json` | Override profil Researcher |

---

## 🏗️ Architecture de Configuration

```
┌─────────────────────────────────────────────────────────────────┐
│  Configuration GLOBALE (UI Agent Zero)                          │
│  /a0/usr/settings.json                                          │
│  → Agent0 utilise ces paramètres                                 │
│  → Contrôle manuel PO uniquement                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ call_subordinate(profile='developer')
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Configuration par PROFIL (Override)                            │
│  /a0/usr/agents/{profile}/settings.json                          │
│  → S'applique SEULEMENT au subordonné                            │
│  → Prioritaire sur la config globale                             │
│  → Invisible dans l'UI (conception Agent Zero)                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 Modèles Alternatifs Notables (Mars 2026)

| Modèle | Contexte | Vision | Coût input/M | Note |
|--------|----------|--------|--------------|------|
| `minimax/minimax-m2.5` | - | - | - | TOP 1 OpenRouter |
| `moonshot/kimi-k2.5` | - | - | - | TOP 2 OpenRouter |
| `google/gemini-3-flash-preview` | 1M | ✅ | $0.50 | TOP 3 |
| `deepseek/deepseek-v3.2` | 64K | ❌ | $0.55 | TOP 4 |
| `qwen/qwen3-coder` | 262K | ❌ | $0.10 | Très fort en code |
| `openai/gpt-4o-mini` | 128K | ❌ | $0.15 | Économique |

---

## 📝 Historique des Modifications

| Date | Profil | Ancien Modèle | Nouveau Modèle | Raison |
|------|--------|---------------|----------------|--------|
| 2026-03-04 | developer | — | deepseek/deepseek-v3.2 | Configuration initiale |
| 2026-03-04 | hacker | — | google/gemini-3-flash-preview | Configuration initiale |
| 2026-03-04 | researcher | — | openai/gpt-4o-mini | Configuration initiale |
| 2026-03-05 | *tous* | — | — | Audit validation Sprint 4 ✅ |
