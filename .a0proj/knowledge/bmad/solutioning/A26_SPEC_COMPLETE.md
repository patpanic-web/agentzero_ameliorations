# A26 — Spec Complète : Modularisation BMAD + Refonte Workflow

> **Statut** : Prête pour validation PO
> **Phase** : Solutioning
> **Date** : 2026-03-07

## Résumé des 7 Modifications

| # | Fichier | Action | Impact |
|---|---------|--------|--------|
| M1 | `memory/behaviour.md` | +4 blocs | Comportement global amélioré |
| M2 | `.a0proj/project.json` | Nettoyage instructions | Suppression skill fantôme |
| M3 | `instructions/BMAD_PERSONAS.md` | **Supprimer** | -9 863 bytes/req |
| M4 | `instructions/BMAD_PROCESS.md` | **Remplacer** par BMAD_CORE.md | -3 576 bytes/req |
| M5 | `/a0/usr/skills/bmad-personas/SKILL.md` | **Créer** | JIT personas |
| M6 | `/a0/usr/skills/bmad-process/SKILL.md` | **Créer** | JIT workflow |
| M7 | `/a0/usr/BACKLOG_GLOBAL.md` | **Créer** | Capture idées hors projet |

**Gain estimé : -13 439 bytes/req sur 80% des échanges**

## Procédure Undo Globale
```bash
cd /a0/usr/projects/agentzero_ameliorations
git log --oneline -10          # identifier les commits
git revert <hash>              # annuler un commit specifique
git push origin main
# Skills (hors repo) : rm -rf /a0/usr/skills/bmad-personas/ /a0/usr/skills/bmad-process/
# Backlog global     : rm /a0/usr/BACKLOG_GLOBAL.md
```

---

## M1 — behaviour.md : Ajout 4 Blocs

**Fichier** : `.a0proj/memory/behaviour.md`
**Action** : Ajouter a la fin
**Taille actuelle** : 1 466 bytes → cible ~3 200 bytes

### Contenu a ajouter

```markdown
## Capture d'Idees — Regle de Tracabilite
* Toute idee mentionnee (meme en passant) doit etre captee et tracee immediatement.
* Si une idee est mentionnee dans un projet actif :
  + Tracer dans le backlog du projet (statut IDEA)
* Si une idee est mentionnee hors projet :
  + Verifier si elle correspond a un projet existant
    -> Si oui : proposer de la tracer dans ce projet
  + Sinon : capturer dans /a0/usr/BACKLOG_GLOBAL.md (statut IDEA)
* Avant de capturer une nouvelle idee : verifier similarites avec l'existant
  + Si similaire -> proposer fusion ou enrichissement (ne pas dupliquer)
  + Tracer la fusion : "fusionne avec [ID]"
* Comportement proactif sur /a0/usr/BACKLOG_GLOBAL.md :
  + En debut de session : signaler les idees non traitees depuis > 7 jours
  + Quand un projet est active : verifier si des idees globales lui correspondent
  + Rappeler les idees EXPLORING inactives depuis > 14 jours
* Une idee capturee n'est JAMAIS supprimee sans accord explicite du PO

## Bootstrap Session — Lecture Backlog Obligatoire
* En debut de toute session dans un projet actif :
  + Lire `knowledge/backlog/BACKLOG.md` avant toute action
  + Identifier la phase BMAD en cours et le dernier sprint
  + Annoncer : "Projet : [nom] | Phase : [X] | Derniere action : [resume]"
* Ne jamais planifier un sprint sans avoir relu le backlog dans la meme session

## Gate de Confirmation — Actions Irreversibles
* Avant toute action potentiellement irreversible ou impactante, demander confirmation :
  + Modification de fichiers de configuration systeme
  + Suppression de fichiers ou donnees
  + Modification de comportement global (behaviour.md, instructions/)
  + Commit/push de changements structurels
* Format : "Je vais [action precise]. Confirmes-tu ?"
* Exception : les actions deja explicitement validees dans une spec approuvee par le PO

## Personas BMAD — Chargement Automatique JIT
* Les personas BMAD sont dans le skill `bmad-personas` — jamais injectes par defaut
* Charger automatiquement via skills_tool:load skill_name="bmad-personas" quand :
  + La tache necessite une analyse structuree (discovery, PRD, architecture, planification)
  + La session entre en phase BMAD (Analysis/Planning/Solutioning)
  + Le PO demande une reflexion profonde ou un brainstorming
* En mode action simple (commit, lecture fichier, reponse rapide) -> ne pas charger
* Ne jamais adopter un persona sans avoir charge le skill au prealable dans la session
```

### Undo M1
```bash
git revert <hash_commit_M1> && git push origin main
```

---

## M2 — project.json : Nettoyage Instructions

**Fichier** : `.a0proj/project.json`
**Action** : Remplacer le champ `instructions`

### Instructions cibles (contenu exact)
```
En tant qu'expert en optimisation de systemes agentiques, suis ces directives :

Approche No-Core-Change : Interdiction formelle de modifier le code source d'Agent-Zero.
Toutes les ameliorations portent sur des elements externes ou configurables.

Modularite & Reversibilite : Solutions a la carte. Chaque outil/skill
activable/desactivable sans compromettre l'integrite du systeme.

Optimisation Ressources : Minimiser les appels API redondants. Evaluer le cout tokens
de chaque ajout. Si un skill n'apporte pas de gain mesurable, l'ecarter.

BMAD : En mode analyse/planification complexe, charger automatiquement le skill
bmad-personas pour adopter le persona approprie a la phase en cours.

Journal : Pour chaque modification, documenter installation et desactivation.
```

### Undo M2
```bash
git revert <hash_commit_M2> && git push origin main
```

---

## M3 — Supprimer BMAD_PERSONAS.md

**Fichier** : `.a0proj/instructions/BMAD_PERSONAS.md`
**Action** : rm (contenu migre dans skill M5)
**Gain** : -9 863 bytes/requete

### Undo M3
```bash
git revert <hash_commit_M3> && git push origin main
```

---

## M4 — Remplacer BMAD_PROCESS.md par BMAD_CORE.md

**Action** : Supprimer BMAD_PROCESS.md, creer BMAD_CORE.md
**Taille actuelle** : 4 099 bytes → cible 523 bytes

### Contenu exact BMAD_CORE.md
```markdown
# BMAD — Configuration Projet

## Phases
Analysis -> Planning -> Solutioning -> Implementation

## Personas (chargement JIT)
Pour activer un persona : skills_tool:load skill_name="bmad-personas"
Pour le workflow complet : skills_tool:load skill_name="bmad-process"
Ne pas charger pour les actions simples (commit, lecture, reponse rapide).

## Backlog = SSOT
Fichier : knowledge/backlog/BACKLOG.md — relire avant toute planification.

## Gouvernance Git
Voir GIT_GOVERNANCE.md
```

### Undo M4
```bash
git revert <hash_commit_M4> && git push origin main
```

---

## M5 — Skill bmad-personas

**Chemin** : `/a0/usr/skills/bmad-personas/SKILL.md`
**Action** : Creer nouveau skill 8 personas
Contenu : voir fichier cree separement (annexe M5)

### Undo M5
```bash
rm -rf /a0/usr/skills/bmad-personas/
```

---

## M6 — Skill bmad-process

**Chemin** : `/a0/usr/skills/bmad-process/SKILL.md`
**Action** : Creer nouveau skill workflow + lecons apprises
Contenu : voir fichier cree separement (annexe M6)

### Undo M6
```bash
rm -rf /a0/usr/skills/bmad-process/
```

---

## M7 — BACKLOG_GLOBAL.md

**Chemin** : `/a0/usr/BACKLOG_GLOBAL.md`
**Action** : Creer fichier structure
Contenu : voir fichier cree separement (annexe M7)

### Undo M7
```bash
rm /a0/usr/BACKLOG_GLOBAL.md
```

---

## Ordre d'Implementation

```
Etape 1 : M7 — BACKLOG_GLOBAL (aucun risque)
Etape 2 : M5 — skill bmad-personas (aucun risque)
Etape 3 : M6 — skill bmad-process (aucun risque)
Etape 4 : M4 — BMAD_CORE.md + suppr BMAD_PROCESS.md (faible risque)
Etape 5 : M3 — suppr BMAD_PERSONAS.md (M5 doit exister)
Etape 6 : M2 — nettoyer project.json (faible risque)
Etape 7 : M1 — enrichir behaviour.md (impact global, en dernier)
```
Chaque etape = 1 commit individuel. Verification avant etape suivante.

## Criteres de Succes

- [ ] Message simple en session projet : personas non charges
- [ ] Tache analytique : personas charges automatiquement
- [ ] Idee hors projet -> tracee dans BACKLOG_GLOBAL.md
- [ ] Debut session projet -> backlog annonce
- [ ] git log montre 7 commits propres
- [ ] ls /a0/usr/skills/ montre bmad-personas et bmad-process
- [ ] ls .a0proj/instructions/ ne montre plus BMAD_PERSONAS.md ni BMAD_PROCESS.md
