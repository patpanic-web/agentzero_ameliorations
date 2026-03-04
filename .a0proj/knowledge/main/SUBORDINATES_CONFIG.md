# ⚙️ Configuration des Subordonnés

> **Dernière mise à jour**: 2026-03-04

## 📊 État Actuel

| Profil | Provider | Modèle | Contexte | Vision | Coût/1M tokens |
|--------|----------|--------|----------|--------|----------------|
| **developer** | openrouter | `deepseek/deepseek-v3.2` | 64K | ❌ | ~$2.74 |
| **hacker** | openrouter | `google/gemini-3-flash-preview` | 1M | ✅ | ~$3.50 |
| **researcher** | openrouter | `openai/gpt-4o-mini` | 128K | ❌ | ~$0.75 |

## 🎯 Justification des Choix

### Developer (Code, Tests, Débogage)
- **DeepSeek V3.2**: Excellent pour le code, tool-use intégré, raisonnement fort
- **Coût**: $0.55 input / $2.19 output par million de tokens
- **Alternative premium**: `anthropic/claude-sonnet-4.5` ($3/$15/1M)

### Hacker (Sécurité, Pentest, Audits)
- **Gemini 3 Flash Preview**: Multimodal (vision), 1M contexte, excellent raisonnement
- **Vision**: Permet l'analyse de captures d'écran et diagrammes
- **Coût**: $0.50 input / $3 output par million de tokens

### Researcher (Recherche, Documentation, Rapports)
- **GPT-4o-mini**: Rapide, économique, bon pour synthèse
- **Coût**: $0.15 input / $0.60 output par million de tokens
- **Alternative qualité**: `deepseek/deepseek-v3.2`

---

## 🔄 Comment Modifier

### Via Agent Zero (Recommandé)

Dites simplement: **"Change [profil] vers [modèle]"**

Exemples:
```
"Change developer vers anthropic/claude-sonnet-4.5"
"Change hacker vers deepseek/deepseek-v3.2"
"Change researcher vers openai/gpt-4o"
```

### Via Fichier Manuel

1. Ouvrir le fichier correspondant:
   - `/a0/usr/agents/developer/settings.json`
   - `/a0/usr/agents/hacker/settings.json`
   - `/a0/usr/agents/researcher/settings.json`

2. Modifier les valeurs:
   ```json
   {
     "chat_model_provider": "openrouter",
     "chat_model_name": "nouveau-modele",
     "chat_model_ctx_length": 64000,
     "chat_model_vision": false
   }
   ```

3. Redémarrer le chat pour appliquer

---

## 📂 Fichiers de Configuration

| Fichier | Description |
|---------|-------------|
| `/a0/usr/agents/developer/settings.json` | Configuration du profil Developer |
| `/a0/usr/agents/hacker/settings.json` | Configuration du profil Hacker |
| `/a0/usr/agents/researcher/settings.json` | Configuration du profil Researcher |
| `/a0/usr/agents/agent0/prompts/agent.system.main.role.md` | Prompt de délégation Agent 0 |

---

## ⚠️ Procédure de Rollback

Pour revenir à la configuration par défaut (effacer l'override):

```bash
# Supprimer l'override d'un profil spécifique
rm -rf /a0/usr/agents/developer
rm -rf /a0/usr/agents/hacker
rm -rf /a0/usr/agents/researcher

# Ou supprimer tous les overrides
rm -rf /a0/usr/agents/*
```

Après suppression, le profil utilisera les paramètres globaux définis dans l'UI.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│  Configuration GLOBALE (UI Agent Zero)                          │
│  /a0/usr/settings.json                                          │
│  → Agent0 utilise ces paramètres                                 │
│  → Contrôle manuel via interface                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ call_subordinate(profile='developer')
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Configuration par PROFIL (Override)                            │
│  /a0/usr/agents/{profile}/settings.json                          │
│  → S'applique SEULEMENT à ce subordonné                          │
│  → Prioritaire sur la config globale                             │
│  → Invisible dans l'UI (conception Agent Zero)                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📝 Historique des Modifications

| Date | Profil | Ancien Modèle | Nouveau Modèle | Raison |
|------|--------|---------------|----------------|--------|
| 2026-03-04 | developer | - | deepseek/deepseek-v3.2 | Configuration initiale |
| 2026-03-04 | hacker | - | google/gemini-3-flash-preview | Configuration initiale |
| 2026-03-04 | researcher | - | openai/gpt-4o-mini | Configuration initiale |
