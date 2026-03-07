# A22 — Optimisation des LLM par Profil

> Date : 2026-03-07 | Statut : ✅ TERMINÉ | Sprint 13

---

## 🎯 Objectif

Optimiser le rapport performance/coût des LLM pour Agent Zero et ses subordonnés, avec interface simplifiée de contrôle pour le PO.

---

## 📊 Configuration Finale

### Agent Zero Principal (UI)

| Slot | Modèle | Coût/1M | Justification |
|------|--------|---------|---------------|
| **Chat** | `moonshot/kimi-k2.5` | $1.07 | IFEval 92.6%, Agentic 85%, économique |
| **Util** | `mistralai/mistral-small-3.2` | $0.18 | Suffisant pour vérif clés API |
| **Browser** | `moonshot/kimi-k2.5` | $1.07 | Multi-turn 88%, navigation browser-use |

**Gain** : -81% vs configuration précédente (Claude Sonnet 4.6)

### Subordonnés (Config fichiers)

| Profil | Modèle | Provider | Coût/1M | Justification |
|--------|--------|----------|---------|---------------|
| **developer** | `kimi-k2.5` | moonshot | $1.07 | HumanEval 99%, LiveCodeBench 85% |
| **hacker** | `tngtech/deepseek-r1t2-chimera` | openrouter | ~$1.15 | 94% compliance, raisonnement avancé |
| **researcher** | `kimi-k2.5` | moonshot | $1.07 | Contexte 262K, économique OSINT |

---

## 🔧 Interface Simplifiée PO

### Fichier de contrôle central

```
/a0/usr/LLM_PROFILES.yaml  ← PO modifie ici
```

**Exemple de modification** :
```yaml
profiles:
  developer:
    provider: "moonshot"
    name: "kimi-k2.5"  # ← Changer ici
```

### Synchronisation

Après modification du YAML :
```bash
python /a0/usr/sync_llm_profiles.py
```

Le script met à jour automatiquement les 3 fichiers `settings.json`.

---

## 📁 Fichiers Créés

| Fichier | Description |
|---------|-------------|
| `/a0/usr/LLM_PROFILES.yaml` | Configuration centrale PO |
| `/a0/usr/sync_llm_profiles.py` | Script de synchronisation |
| `/a0/usr/agents/developer/settings.json` | Config complète developer |
| `/a0/usr/agents/hacker/settings.json` | Config complète hacker (DeepSeek R1T2) |
| `/a0/usr/agents/researcher/settings.json` | Config complète researcher |

---

## 📝 Procédure de Modification

### Pour changer le LLM d'un subordonné :

1. **Éditer** `/a0/usr/LLM_PROFILES.yaml`
2. **Modifier** la section du profil concerné
3. **Exécuter** `python /a0/usr/sync_llm_profiles.py`
4. **Vérifier** dans l'interface que le changement est pris en compte

### Pour switch temporairement Agent0 vers un modèle premium :

1. **UI Agent Zero** → Settings
2. **Chat Model** → Sélectionner `anthropic/claude-opus-4.6`
3. **Usage** : Tâches BMAD critiques uniquement ($30/1M)
4. **Retour** : Revenir à `moonshot/kimi-k2.5` après usage

---

## 💰 Impact Économique

| Scénario | Coût estimé/1M | Gain |
|----------|----------------|------|
| Avant (tout Claude) | ~$12 | — |
| Après (optimisé) | ~$2.32 | **-81%** |

---

## 🎓 Sources

Basé sur `RAPPORT_PO_CHOIX_LLM_PAR_PROFIL.md` — analyse complète des benchmarks 2026.
