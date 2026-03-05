# 📊 BMAD Phase 1 - ANALYSE COMPLÈTE
# Configuration Agent Zero : Diagnostic et Axes d'Amélioration

> **Date :** 2026-03-05
> **Phase BMAD :** Analysis (Phase 1)
> **Analyste :** Mary (Business Analyst)
> **Version Agent Zero :** v0.9.8.2

---

## 🎯 Objectif de l'Analyse

Identifier et documenter TOUS les problèmes de configuration qui empêchent Agent Zero
de se comporter correctement, en se basant sur :
- 4 audits précédents (Git, Délégation, Complet, LLM)
- Vérification en temps réel de CHAQUE fichier et configuration
- Recherche de bonnes pratiques officielles et communautaires
- Analyse du code source des extensions critiques

---

## 📐 Architecture de Prompts Agent Zero (Vérifiée)

### Mécanisme d'Héritage (Confirmé par code source + docs officielles)

Ordre de résolution (le dernier trouvé gagne) :

```
1. /a0/prompts/                                    → Prompts par défaut (globaux)
2. /a0/agents/<profile>/prompts/                   → Overrides profil (shipped)
3. /a0/usr/agents/<profile>/prompts/               → Overrides utilisateur
4. /a0/usr/projects/<name>/.a0proj/agents/<profile>/prompts/ → Overrides projet
5. behaviour.md (memory dir)                       → Injecté en TÊTE du prompt
```

**Source :** `subagents.py:get_paths()` + `files.py:read_prompt_file()` + docs officielles.

### Compilation du System Prompt (Confirmé par code source)

```
behaviour.md (insertion en position 0)
+ agent.system.main.md
  ├── agent.system.main.role.md
  ├── agent.system.main.environment.md
  ├── agent.system.main.communication.md
  ├── agent.system.main.solving.md
  └── agent.system.main.tips.md
+ agent.system.tools.md (TOUS les outils)
+ agent.system.tools_vision.md (si vision=true)
+ MCP tools (TOUS les MCP tools)
+ Skills (loaded skills)
+ Secrets
+ Project prompt
```

---

## 🔴 PROBLÈMES CRITIQUES

### P1 - Conflit de Signaux dans la Délégation

| Aspect | Détail |
|--------|--------|
| **Sévérité** | 🔴 CRITIQUE |
| **Impact** | Agent0 résout au lieu de déléguer |
| **Fichiers** | `solving.md` + `call_sub.md` vs `role.md` override |
| **Vérifié** | ✅ Code source lu et confirmé |

**Diagnostic détaillé :**

Il y a un CONFLIT DIRECT entre deux prompts actifs :

**`agent.system.main.solving.md` (NON overridé) dit :**
```
3 solve or delegate            ← SOLVE en PREMIER
tools solve subtasks
you can use subordinates       ← CAN = optionnel
```

**`agent.system.main.role.md` (overridé dans usr/agents/agent0/) dit :**
```
Delegation Policy (CRITICAL)
ALWAYS delegate to specialized subordinates when...
PREFER subordinates for execution tasks
Your role is PLANNING and SUPERVISION
```

**Résultat :** L'agent reçoit DEUX signaux contradictoires :
- Le rôle dit "TOUJOURS déléguer"
- Le processus de résolution dit "résoudre OU déléguer" avec "solve" en premier

Le processus pas-à-pas (solving.md) a un poids comportemental plus fort car il dicte
la SÉQUENCE D'ACTIONS, tandis que le rôle est une directive générale.

**Correctif proposé :** Créer un override de `agent.system.main.solving.md` dans
`/a0/usr/agents/agent0/prompts/` qui inverse l'ordre et renforce le langage.

---

### P2 - Langage Permissif dans call_subordinate

| Aspect | Détail |
|--------|--------|
| **Sévérité** | 🔴 CRITIQUE |
| **Impact** | Délégation perçue comme optionnelle |
| **Fichier** | `agent.system.tool.call_sub.md` |
| **Vérifié** | ✅ Contenu exact lu |

**Extrait actuel :**
```
you can use subordinates for subtasks    ← CAN = facultatif
subordinates can be scientist coder...   ← Pas de mapping clair
```

**Correctif proposé :** Override avec langage impératif et mapping tâche→profil explicite.

---

### P3 - Asymétrie Massive des Profils d'Agents

| Profil | Lignes Role | Lignes Comm | Total | Qualité |
|--------|-------------|-------------|-------|----------|
| developer | ~80 | ~100 | ~180 | ✅ Excellente |
| researcher | ~80 | ~100 | ~180 | ✅ Excellente |
| hacker | 8 | 0 | 8 | 🔴 Critique |
| agent0 | 13+21 (override) | 0 | 34 | 🟡 Insuffisant |

**Impact vérifié dans cette session :**
- Le developer subordinate a produit un audit INCOMPLET (fichiers déclarés "non trouvés" alors qu'ils existent)
- Le researcher subordinate a produit un rapport SUPERFICIEL
- Cela confirme que même avec de bons prompts (developer a 180 lignes), le MODÈLE
  assigné (DeepSeek V3.2) peut ne pas être à la hauteur pour certaines tâches

**Correctif proposé :** 
- Enrichir le profil hacker (méthodologie, outils, processus)
- Enrichir le profil agent0 (orchestration, critères de délégation, mapping)
- Évaluer l'adéquation modèle↔profil

---

## 🟡 PROBLÈMES IMPORTANTS

### P4 - Configuration Git MCP Incorrecte

| Aspect | Détail |
|--------|--------|
| **Sévérité** | 🟡 Important |
| **Impact** | Git MCP pointe vers un AUTRE projet |
| **Fichier** | `usr/settings.json` → `mcp_servers` |

**Valeur actuelle :**
```
"--repository", "/a0/usr/projects/automatisation_pour_telecharger_des_films_torrent"
```

**Devrait être :** Le repository du projet actif ou une configuration dynamique.

---

### P5 - Aucun Override de Communication pour Agent0

| Aspect | Détail |
|--------|--------|
| **Sévérité** | 🟡 Important |
| **Impact** | Agent0 utilise la communication par défaut (minimaliste) |
| **Contexte** | Developer et Researcher ont des prompts de communication dédiés (~100 lignes chacun) |

Developer a un processus d'interview structuré, des règles de thinking détaillées,
un format de réponse précis. Agent0 n'a rien de tout ça pour son rôle d'orchestrateur.

---

### P6 - Modèle LLM Preview pour Hacker

| Aspect | Détail |
|--------|--------|
| **Sévérité** | 🟡 Important |
| **Impact** | Stabilité non garantie |
| **Modèle** | `google/gemini-3-flash-preview` |

Un modèle "preview" ne devrait pas être utilisé en production pour des tâches
de sécurité qui nécessitent fiabilité et précision.

---

### P7 - Token Inflation par Chargement Exhaustif des Outils

| Aspect | Détail |
|--------|--------|
| **Sévérité** | 🟡 Important |
| **Impact** | Chaque agent reçoit TOUS les outils + TOUS les MCP tools |
| **Source** | `_10_system_prompt.py` : `get_tools_prompt()` + `get_mcp_tools_prompt()` |

Confirmé par code source : aucun filtrage par profil. Chaque subordinate reçoit
le même bloc d'outils que l'agent principal, gonflant le contexte inutilement.

**Note :** C'est by design selon la doc officielle. La doc recommande d'utiliser
les Skills pour les expertises contextuelles plutôt que les outils.

---

### P8 - Docker MCP Désactivé

| Aspect | Détail |
|--------|--------|
| **Sévérité** | 🟢 Mineur |
| **Impact** | Fonctionnalité Docker non disponible |
| **Config** | `"disabled": true` dans mcp_servers |

---

## 📊 Assignation LLM Actuelle (Complète)

| Rôle | Modèle | Provider | Ctx | Vision | Usage |
|------|--------|----------|-----|--------|-------|
| **Agent0** (chat) | Claude Opus 4.6 | OpenRouter | 100K | ✅ | Orchestration |
| **Utility** | Llama 4 Scout | OpenRouter | 100K | ❌ | Résumés, mémoire, keywords |
| **Browser** | DeepSeek V3.2 | OpenRouter | - | ✅ | Navigation web |
| **Embedding** | all-MiniLM-L6-v2 | HuggingFace | - | - | Vecteurs mémoire |
| **Developer** (sub) | DeepSeek V3.2 | OpenRouter | 64K | ❌ | Code, debug |
| **Hacker** (sub) | Gemini 3 Flash Preview | OpenRouter | 1M | ✅ | Sécurité |
| **Researcher** (sub) | GPT-4o-mini | OpenRouter | 128K | ❌ | Recherche |

### Observations sur l'adéquation Modèle↔Tâche

1. **Developer + DeepSeek V3.2 (64K ctx):** Le prompt developer fait ~180 lignes.
   Avec 64K de contexte, ça reste gérable mais le modèle peut manquer de rigueur
   pour des audits complexes (confirmé par cette session).

2. **Researcher + GPT-4o-mini:** Résultats superficiels dans cette session.
   Le modèle est économique mais peut manquer de profondeur.

3. **Hacker + Gemini Preview:** Modèle instable + prompt quasi-inexistant = risque.

4. **Agent0 + Claude Opus:** Excellent choix pour l'orchestration mais coûteux.
   L'optimisation des autres niveaux compense ce coût.

---

## 🎯 AXES D'AMÉLIORATION IDENTIFIÉS

### Résumé Priorisé

| # | Axe | Sévérité | Effort | Impact | Mécanisme |
|---|-----|----------|--------|--------|------------|
| A1 | Override solving.md pour Agent0 | 🔴 | 15 min | MAJEUR | usr/agents/agent0/prompts/ |
| A2 | Override call_sub.md pour Agent0 | 🔴 | 15 min | MAJEUR | usr/agents/agent0/prompts/ |
| A3 | Enrichir profil Hacker | 🔴 | 1h | HAUT | agents/hacker/prompts/ (usr) |
| A4 | Enrichir rôle orchestrateur Agent0 | 🟡 | 30 min | HAUT | usr/agents/agent0/prompts/ |
| A5 | Évaluer modèles subordinates | 🟡 | 1h | MOYEN | usr/agents/*/settings.json |
| A6 | Corriger Git MCP path | 🟡 | 5 min | MOYEN | usr/settings.json |
| A7 | Documenter & nettoyer backlog | 🟢 | 30 min | MOYEN | knowledge/backlog/ |
| A8 | Évaluer Docker MCP | 🟢 | 15 min | FAIBLE | usr/settings.json |

### Détail des Correctifs

#### A1 - Override solving.md (🔴 Quick Win #1)
Créer `/a0/usr/agents/agent0/prompts/agent.system.main.solving.md` avec :
- "DELEGATE FIRST, solve only if no subordinate matches"
- MUST language au lieu de CAN
- Checklist de délégation obligatoire avant résolution
- Mapping explicite tâche → profil

#### A2 - Override call_sub.md (🔴 Quick Win #2)
Créer `/a0/usr/agents/agent0/prompts/agent.system.tool.call_sub.md` avec :
- Langage impératif (MUST delegate)
- Critères clairs de quand utiliser quel profil
- Exemples concrets de délégation réussie

#### A3 - Enrichir profil Hacker (🔴 Effort moyen)
Créer `/a0/usr/agents/hacker/prompts/agent.system.main.role.md` avec :
- Méthodologies (OWASP, PTES, NIST)
- Liste d'outils Kali
- Processus structuré de tests
- Types de tests définis

#### A4 - Renforcer Agent0 orchestrateur (🟡 Important)
Améliorer `/a0/usr/agents/agent0/prompts/agent.system.main.role.md` avec :
- Processus d'orchestration détaillé
- Critères de qualité pour évaluer les résultats des subordinates
- Instructions de re-délégation si qualité insuffisante

#### A5 - Réévaluer modèles subordinates (🟡 Analyse)
Tester et potentiellement ajuster :
- Developer: DeepSeek V3.2 suffisant pour code, mais pour des audits?
- Researcher: GPT-4o-mini suffisant pour recherche basique, mais pour analyse approfondie?
- Hacker: Remplacer le modèle preview par un modèle stable

---

## ✅ Ce qui Fonctionne Bien

| Élément | Statut |
|---------|--------|
| Mécanisme d'override de prompts | ✅ Fonctionnel et vérifié |
| Settings.json par profil | ✅ Fonctionnel (Tâche #1) |
| Profils Developer et Researcher | ✅ Bien définis (prompts riches) |
| Claude Opus pour orchestration | ✅ Excellent choix |
| MCP Tavily, Playwright, System Diag | ✅ Fonctionnels |
| Behaviour system | ✅ Fonctionnel |

---

## 📎 Fichiers Clés Référencés

| Fichier | Rôle | État |
|---------|------|------|
| `/a0/prompts/agent.system.main.solving.md` | Process de résolution | ⚠️ Non overridé |
| `/a0/prompts/agent.system.tool.call_sub.md` | Outil délégation | ⚠️ Non overridé |
| `/a0/usr/agents/agent0/prompts/agent.system.main.role.md` | Rôle Agent0 | ✅ Override existe |
| `/a0/agents/hacker/prompts/agent.system.main.role.md` | Rôle Hacker | ⚠️ 8 lignes |
| `/a0/agents/developer/prompts/agent.system.main.role.md` | Rôle Developer | ✅ 180 lignes |
| `/a0/agents/researcher/prompts/agent.system.main.role.md` | Rôle Researcher | ✅ 180 lignes |
| `/a0/usr/settings.json` | Config globale | ⚠️ Git MCP incorrect |
| `/a0/usr/agents/*/settings.json` | Config modèles subs | ✅ Fonctionnel |

---

## 🔍 Méthodologie d'Analyse

- ✅ Lecture directe de TOUS les fichiers de prompts pertinents
- ✅ Analyse du code source Python des extensions critiques
- ✅ Vérification de la documentation officielle Agent Zero
- ✅ Recherche GitHub Issues (#674 confirmée)
- ✅ Cross-référence avec les 4 audits précédents
- ✅ Test empirique de la qualité des subordinates (cette session)
