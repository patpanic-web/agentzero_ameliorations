# 🔄 Sprint 1 — "La Fondation" — Implémentation
> Date : 2026-03-05
> Statut : ✅ TERMINÉ

## Objectif
Faire en sorte qu'Agent Zero délègue SYSTÉMATIQUEMENT aux subordinates plutôt que d'exécuter lui-même.

## Fichiers Créés

### A1 — Override solving.md
- **Fichier :** `/a0/usr/agents/agent0/prompts/agent.system.main.solving.md`
- **Override de :** `/a0/prompts/agent.system.main.solving.md`
- **Changements :**
  - Step 3 : "solve or delegate" → "delegate or solve"
  - "tools solve subtasks" → "delegate subtasks to specialized subordinates"
  - Ajout : "only solve directly when no suitable subordinate profile exists"
- **Lignes modifiées :** 3 sur 16
- **Rollback :** `rm /a0/usr/agents/agent0/prompts/agent.system.main.solving.md`

### A2 — Override call_sub.md
- **Fichier :** `/a0/usr/agents/agent0/prompts/agent.system.tool.call_sub.md`
- **Override de :** `/a0/prompts/agent.system.tool.call_sub.md`
- **Changements :**
  - "you can use subordinates" → "always delegate execution subtasks to subordinates"
  - "subordinates can be..." → "subordinates are specialized agents for execution tasks"
  - Ajout : "delegate when task matches subordinate specialty"
- **Lignes modifiées :** 3 sur 23
- **Rollback :** `rm /a0/usr/agents/agent0/prompts/agent.system.tool.call_sub.md`

## Vérification
- Persistance : ✅ Fichiers dans /a0/usr/ (volume Docker monté)
- No-Core-Change : ✅ Aucun fichier core modifié
- Chirurgical : ✅ 6 lignes modifiées sur 39 lignes totales
