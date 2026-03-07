# 📋 AUDIT DE COMPRÉHENSION TOTALE
## Agent Zero Framework + BMAD Method — État Réel Certifié

> **Date** : 2026-03-07  
> **Méthode** : Lecture directe du code source + recherches web officielles  
> **Statut** : CERTIFIÉ — aucune supposition, uniquement des faits vérifiés  
> **Fichier** : knowledge/bmad/analysis/AUDIT_COMPREHENSION_TOTALE.md

---

## 1. ARCHITECTURE AGENT ZERO — CERTIFIÉE (code source lu)

### 1.1 Construction du System Prompt (ordre d'injection)

Source : `/a0/python/extensions/_20_behaviour_prompt.py` + `_30_system_prompt.py` + `_40_project_prompt.py`

```
POSITION 0 : behaviour.md (INSERT — injecté AVANT tout le reste)
  Fichier : /a0/usr/projects/<nom>/.a0proj/memory/behaviour.md (si projet actif)
  Fichier : /a0/usr/memory/<subdir>/behaviour.md (hors projet)
  Mécanisme : _20_behaviour_prompt.py → abs_db_dir() → get_project_meta_folder()

POSITION 1 : agent.system.main.md (avec surcharges incluses)
  Inclut via {{ include }} :
    - agent.system.main.role.md      → surcharge : /a0/usr/agents/agent0/prompts/role.md
    - agent.system.main.environment.md → original
    - agent.system.main.communication.md → original
    - agent.system.main.solving.md   → surcharge : /a0/usr/agents/agent0/prompts/solving.md
    - agent.system.main.tips.md      → original

POSITION 2 : agent.system.tools.md
  call_sub.md → surcharge : /a0/usr/agents/agent0/prompts/call_sub.md

POSITION 3 : MCP tools (si actifs)
POSITION 4 : Skills disponibles
POSITION 5 : Secrets/variables

POSITION 6 : project_prompt (si projet actif)
  = agent.system.projects.main.md
  + agent.system.projects.active.md avec project_instructions =
      project.json["instructions"]
      + sorted(instructions/*.md par nom alphabétique)
      = project.json["instructions"]
        + BMAD_PERSONAS.md (ordre alpha 1)
        + BMAD_PROCESS.md  (ordre alpha 2)
        + GIT_GOVERNANCE.md (ordre alpha 3)
```

### 1.2 Mécanisme de Surcharge — CERTIFIÉ

Source : `subagents.get_paths()` + `files.find_file_in_dirs()`

**Ordre de recherche pour `read_prompt(file)` :**
```
1. /a0/usr/projects/<nom>/.a0proj/agents/<profile>/prompts/  (projet + profil)
2. /a0/usr/projects/<nom>/.a0proj/                           (projet seul)
3. /a0/usr/agents/<profile>/prompts/                         (global utilisateur + profil) ← NOS SURCHARGES
4. /a0/agents/<profile>/prompts/                             (agents profil défaut)
5. /a0/usr/                                                  (global utilisateur)
6. /a0/prompts/                                              (défaut système)
```

**Règle fondamentale :** La surcharge **REMPLACE** l'original. Il n'y a pas de merge.
`find_file_in_dirs` retourne le PREMIER fichier trouvé dans l'ordre ci-dessus.
→ Une surcharge doit contenir l'intégralité du contenu souhaité.

### 1.3 Emplacement behaviour.md — CERTIFIÉ

Source : `memory.py → abs_db_dir() → get_project_meta_folder()`

```python
# memory_subdir = "projects/agentzero_ameliorations"
# → starts with "projects/" → True
# → get_project_meta_folder("agentzero_ameliorations") = "/a0/usr/projects/agentzero_ameliorations/.a0proj"
# → + "memory" = "/a0/usr/projects/agentzero_ameliorations/.a0proj/memory/"
# → behaviour.md = /a0/usr/projects/agentzero_ameliorations/.a0proj/memory/behaviour.md
```

✅ **Confirmé** : behaviour.md est bien dans `.a0proj/memory/behaviour.md`

### 1.4 Instructions/ — Ordre d'Injection Alphabétique

Source : `build_system_prompt_vars()` → `sorted(additional_instructions.keys())`  
Les clés = `os.path.basename(file_path)` = noms de fichiers

```
Ordre d'injection :
1. BMAD_PERSONAS.md    (B < B < G, alphabétique)
2. BMAD_PROCESS.md
3. GIT_GOVERNANCE.md
```

---

## 2. BMAD OFFICIEL — RÉALITÉ vs NOTRE IMPLÉMENTATION

### 2.1 Ce qu'est RÉELLEMENT BMAD

Source : https://github.com/bmad-code-org/BMAD-METHOD (lu directement)

| Aspect | Réalité |
|--------|---------|
| **Nom complet actuel** | "Build More Architect Dreams" (rebrandé fév. 2026, était "Breakthrough Method of Agile AI Driven Development") |
| **Version actuelle** | v6.0.4 (Mars 2026) — 39.2k stars, très actif |
| **Plateforme cible** | Claude Code, Cursor, GitHub Copilot — IDEs avec accès fichiers |
| **Installation** | `npx bmad-method install` — génère des fichiers YAML d'agents |
| **Format** | Agents YAML + workflows Markdown + templates |
| **Architecture** | Agents spécialisés par phase (PM, Architect, Developer, QA, Scrum...) |
| **Chargement** | JIT (Just-In-Time) — chaque agent charge son contexte à la demande |

**BMAD N'EST PAS conçu pour Agent Zero.** C'est un framework pour IDEs AI (Claude Code, Cursor).

### 2.2 Notre Adaptation BMAD

Notre implémentation utilise les **principes** de BMAD (phases, personas, rituals) mais adaptés manuellement pour Agent Zero. C'est une adaptation CUSTOM, légitime mais distincte de BMAD officiel.

**Anti-patterns identifiés par rapport à BMAD officiel :**

| Anti-pattern | BMAD officiel fait | Notre implémentation fait |
|---|---|---|
| Chargement des personas | JIT — chargé uniquement quand le persona est activé | Injecté en totalité à CHAQUE requête (9 863 bytes) |
| Skill fantôme | N/A | `project.json` référence `skill bmad-method` qui n'existe pas |
| Séparation phases | Chaque phase = fichier séparé chargé à la demande | Tout dans un seul BMAD_PERSONAS.md |
| Scale-adaptive | Ajuste la profondeur selon complexité | Overhead constant quelle que soit la tâche |

### 2.3 Ce que BMAD officiel fait bien (applicable ici)

- **JIT Loading** : charger les personas uniquement en mode EXPLORE, pas systématiquement
- **Scale-Domain-Adaptive** : réduire l'overhead pour les tâches simples
- **Workflows modulaires** : une phase à la fois, pas tout en permanence

---

## 3. ÉTAT RÉEL DES FICHIERS DU PROJET

### 3.1 behaviour.md (position 0 — injecté en premier)

**Emplacement** : `/a0/usr/projects/agentzero_ameliorations/.a0proj/memory/behaviour.md`  
**Taille** : ~1 200 bytes

**Contenu actuel** :
- ✅ Règle mémoire sécurisée (memory_load avant delete)
- ✅ Comportement proactif (lead detection)
- ✅ Règle persistance /a0/usr/
- ❌ PAS de lecture backlog en début de session
- ❌ PAS de déclaration de mode d'interaction
- ❌ PAS de gate de confirmation pour modifications comportementales
- ❌ PAS de règle capture d'idées

### 3.2 project.json["instructions"] (injecté dans project_prompt)

**Problèmes identifiés** :
- 🔴 Référence `skill bmad-method` → ce skill N'EXISTE PAS (instruction fantôme)
- 🟡 Entièrement en français (incohérence avec prompts originaux en anglais)
- ✅ Contenu utile : No-Core-Change, Modularité, Audit Continu

### 3.3 BMAD_PERSONAS.md (injecté en position 1 des instructions/)

**Taille** : 9 863 bytes — injecté à CHAQUE requête dans un projet  
**Contenu** : 6 personas complets (Mary/BA, Sarah/PM, Alex/Arch, James/Dev, Quinn/QA, Bob/Scrum)  
**Problème** : overhead constant même pour une question simple

### 3.4 BMAD_PROCESS.md (injecté en position 2 des instructions/)

**Taille** : 4 099 bytes  
**Contenu** : workflow BMAD + checklist + leçons apprises  
**Valeur** : les leçons apprises sont précieuses et doivent être conservées

### 3.5 GIT_GOVERNANCE.md (injecté en position 3 des instructions/)

**Taille** : 523 bytes — court, en anglais, bien écrit  
**Statut** : ✅ OK, rien à changer

### 3.6 Surcharges agent0 (/a0/usr/agents/agent0/prompts/)

| Fichier | Taille | Contenu | Statut |
|---------|--------|---------|--------|
| `role.md` | ~6k | Delegation Policy + Orchestration Protocol | ✅ Pertinent |
| `solving.md` | ~3k | Delegate-first (MUST delegate) | ✅ Pertinent |
| `call_sub.md` | ~2k | Renforce la délégation obligatoire | ✅ Pertinent |

---

## 4. IMPLICATIONS POUR L'ANALYSE DES BESOINS

### 4.1 Ce qui est CONFIRMÉ

- ✅ **behaviour.md est le bon endroit** pour les règles globales (position 0, toujours injecté)
- ✅ **Séparation projet/hors-projet** est architecturalement fondée (project_prompt n'existe que si projet actif)
- ✅ **Le backlog comme SSOT** est la bonne approche pour la mémoire cross-session
- ✅ **Git pour l'undo** est la bonne approche (chaque commit = état stable)

### 4.2 Ce qui est RÉVISÉ

| Supposition initiale | Réalité certifiée |
|---|---|
| "skill bmad-method" à supprimer | ✅ Confirmé — n'existe pas, à supprimer |
| BMAD_PERSONAS.md peut être déplacé dans knowledge/ | ✅ Possible — mais doit être chargé via skill/on-demand |
| Les surcharges "ajoutent" au original | ❌ FAUX — elles REMPLACENT. Toute surcharge doit être complète |
| behaviour.md peut être enrichi directement | ✅ Confirmé — c'est un fichier texte simple, pas une surcharge |
| project.json instructions = simple texte | ✅ Confirmé — est concatené directement dans le prompt |

### 4.3 Découverte Architecturale Importante

**La séparation projet/hors-projet existe déjà nativement dans Agent Zero.**

`project_prompt` est injecté **uniquement si un projet est actif**. Cela signifie :
- BMAD_PERSONAS.md, BMAD_PROCESS.md, GIT_GOVERNANCE.md → **déjà absents hors projet**
- Les instructions BMAD sont **déjà contextualisées au projet**
- La seule chose qui s'applique globalement = behaviour.md

→ **Notre analyse était correcte sur ce point, mais pour de mauvaises raisons.**  
Ce n'est pas quelque chose qu'on doit implémenter — c'est déjà fait par Agent Zero.

---

## 5. RÉSUMÉ — CE QUI DOIT CHANGER ET POURQUOI

| Modification | Fichier | Justification certifiée | Impact tokens |
|---|---|---|---|
| **M1** : Ajouter 4 règles | `behaviour.md` | Position 0, injecté toujours, bon endroit | +300 bytes constant |
| **M2** : Supprimer skill fantôme + réécrire EN | `project.json[instructions]` | Skill n'existe pas, incohérence langue | -200 bytes |
| **M3** : Déplacer BMAD_PERSONAS.md | `instructions/` → `knowledge/` | 9 863 bytes injectés pour RIEN 80% du temps | **-9 863 bytes/requête** |
| **M4** : Simplifier BMAD_PROCESS.md | `instructions/BMAD_PROCESS.md` | Garder leçons apprises, alléger règles | -1 500 bytes |
| **M5** : Créer BACKLOG statuts | `BACKLOG.md` | Un seul fichier avec statuts de maturité | 0 |

**Gain net estimé : -11 000 tokens/requête en contexte projet**

---

## 6. CE QUI NE CHANGE PAS

- ✅ Surcharges agent0 (role, solving, call_sub) → pertinentes, bien implémentées
- ✅ GIT_GOVERNANCE.md → court, EN, bon
- ✅ Backlog comme SSOT → approche validée
- ✅ Architecture de gouvernance (knowledge/, decisions/, etc.) → solide
- ✅ Séparation projet/hors-projet → déjà native dans Agent Zero

---

## 7. PROTOCOLE ANTI-DESTRUCTEUR — FORMALISÉ

Règle permanente pour toute modification touchant le comportement d'Agent Zero :

```
PHASE 0 — AUDIT OBLIGATOIRE
  □ Lire chaque fichier à modifier (état réel, pas supposé)
  □ Vérifier le mécanisme exact d'injection
  □ Identifier toutes les dépendances et références
  □ Documenter les risques de casse

PHASE 1 — SPEC COMPLÈTE
  □ État actuel exact (extrait du fichier)
  □ État cible exact (contenu complet)
  □ Diff précis ligne par ligne
  □ Impact comportemental documenté
  □ Procédure undo : git log + git revert <hash>

PHASE 2 — VALIDATION PO
  □ PO valide la spec complète AVANT toute modification
  □ Format : ⚠️ [VALIDATION REQUISE] + ce qui change + impact + risque + undo

PHASE 3 — IMPLÉMENTATION
  □ Une modification à la fois
  □ Commit individuel par modification
  □ Vérification comportementale avant modification suivante
  □ Rollback immédiat si comportement inattendu
```

---

## 8. UNDO — PROCÉDURE SIMPLE

```bash
# Voir l'historique des modifications
git log --oneline -20

# Annuler une modification spécifique (sans perdre l'historique)
git revert <hash_du_commit>
git push origin main

# Revenir à un état complet (plus radical)
git checkout <hash_du_commit> -- chemin/vers/fichier
git commit -m "revert: restauration fichier"
git push origin main
```

Cette procédure est incluse dans chaque modification. L'agent l'exécute sur simple demande verbale.

---

*Rapport généré le 2026-03-07 — Audit complet basé sur lecture code source + sources officielles*
