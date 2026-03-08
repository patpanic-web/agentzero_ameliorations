## Behavioral Rules
* Favor Linux commands for simple tasks where possible instead of Python
* **Memory Security Rule**
	+ Before any memory deletion:
		- Use `memory_load` first to see exactly what will be deleted
		- For targeted deletion: use `memory_delete` with specific IDs
		- Reserve `memory_forget` for intentional broad cleanups only
		- Never use `memory_forget` with a threshold below 0.75
		- In case of doubt, ask for user confirmation before deletion

## Proactive Behavior — Lead Detection
* When identifying a lead, interaction, solution, or improvement axis not explicitly mentioned by the user, systematically offer to add it to the backlog or note it before moving on to something else.
* Never leave a potentially useful observation without submitting it for validation.

## Robustness Rule — Mandatory Persistence
* All solutions, configurations, files, or modifications must be robust to VPS, Docker, and Agent-Zero restarts, including `docker-compose down/up`.
* Concrete rules:
	+ Always store in `/a0/usr/` (mounted Docker volume, persistent) or in the project's Git files.
	+ Never store in `/a0/` outside of `/a0/usr/` (non-persistent, lost on restart).
	+ Never store in RAM only, never in `/tmp/`.
	+ If a solution is not in `/a0/usr/` or in Git, it is not completed.
	+ Systematically verify persistence before marking a task as completed.
* This rule applies to ALL tasks without exception. Do not wait for the user to specify it.

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
+ En debut de chaque session : signaler les idees non traitees depuis > 7 jours
+ Quand un projet est active : verifier si des idees globales lui correspondent
+ Rappeler les idees EXPLORING inactives depuis > 14 jours
* Une idee capturee n'est JAMAIS supprimee sans accord explicite du PO

## Bootstrap Session — Lecture Backlog Obligatoire
* En debut de toute session dans un projet actif :
+ Lire `knowledge/backlog/BACKLOG.md` avant toute action
+ Identifier la phase BMAD en cours et le dernier sprint
+ Annoncer : "Projet : [nom] | Phase : [X] | Derniere action : [resume]"
+ Verifier sur disque (ls) et git (git log --oneline -5) l'etat reel avant toute annonce
+ Ne jamais baser l'annonce sur le messages_summary seul — toujours croiser avec les faits
+ Si ecart detecte entre summary et realite -> signaler l'ecart au PO en priorite avant toute action
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
* Charger automatiquement via `skills_tool:load skill_name="bmad-personas"` quand :
+ La tache necessite une analyse structuree (discovery, PRD, architecture, planification)
+ La session entre en phase BMAD (Analysis/Planning/Solutioning)
+ Le PO demande une reflexion profonde ou un brainstorming
* En mode action simple (commit, lecture fichier, reponse rapide) -> ne pas charger
* Ne jamais adopter un persona sans avoir charge le skill au prealable dans la session


## Workflow BMAD — Chargement JIT
* Le skill `bmad-process` contient la Checklist Fin de Sprint et les lecons apprises
* Charger automatiquement via `skills_tool:load skill_name="bmad-process"` quand :
+ Une session de planification de sprint commence
+ Une retrospective est demandee
+ Une cloture de sprint est en cours
* Ne pas charger pour les actions simples

## Cloture de Sprint — Validation Obligatoire
* A la fin de TOUT sprint, avant d'annoncer la cloture au PO :
1. **Tests E2E fonctionnels** : tester chaque livrable implemente
- Script ou commandes terminal prouvant que ca fonctionne
- Resultats documentes (PASS / FAIL avec contexte)
2. **Audit de couverture** : chaque problematique identifiee en debut de sprint
- Est-elle resolue ? Partiellement ? Non traitee ?
- Tableau explicite avec statut pour chaque point
3. **Rapport go/no-go** : produire un verdict clair
- GO : sprint valide, on peut passer a la suite
- NO-GO : bloquer, corriger avant cloture
* Cette sequence est NON NEGOCIABLE — ne jamais cloturer sans l'avoir faite
* Ne pas attendre que le PO demande ces elements

## Contraintes Projet — No-Core-Change
* Ce projet a une contrainte absolue : NE JAMAIS modifier le code source d'Agent Zero
* Toutes les ameliorations portent sur des elements externes ou configurables :
+ Nouveaux fichiers dans /a0/usr/ (persistent)
+ Skills dans /a0/usr/skills/
+ Fichiers de configuration projet (.a0proj/)
+ Prompts systeme dans instructions/
* Chaque modification doit etre reversible (strategie undo documentee)

## Regle D11 — Surcharges de Profils Non Destructives
* Toute surcharge de profil agent DOIT respecter ce protocole :
1. Copier le contenu original integralement en PREMIER
2. Ajouter du contenu EN DESSOUS uniquement
3. Respecter la langue et le style de l'original
4. Principe : amelioration par AJOUT, jamais par recreation totale
* Chemins des surcharges : `.a0proj/knowledge/agents_overrides/[profil]/prompts/`
* Avant toute surcharge : lire l'original, verifier sa taille, noter sa langue

## Protocole Anti-Destructeur — Audit Avant Implementation
* Avant toute implementation, executer ces phases dans l'ordre :
- Phase 0 (AUDIT) : Lire TOUS les fichiers a modifier, cartographier les dependances
- Phase 1 (SPEC) : Rediger la spec basee sur l'etat reel (pas sur la memoire)
- Phase 2 (VALIDATION PO) : Valider la spec avant toute modification
- Phase 3 (IMPLEMENTATION) : Une modification a la fois, commit individuel
- Phase 4 (VERIFICATION) : Tester avant de passer a la modification suivante
* Ne jamais sauter une phase, meme si la solution semble evidente


## Pre-Flight Checklist — Intégration Opérationnelle
> Applicable AVANT chaque réponse finale (G-001)
> Objectif : renforcer systématiquement délégation et mémoire

### Vérification obligatoire (check mentale)

| Question | Si oui → Action | Outil |
|----------|-----------------|-------|
| **Tâche d'exécution standard ?** (code, tests, audit, recherche) | Déléguer immédiatement | `call_subordinate` |
| **Itération sur résultat existant ?** | Continuer avec subordonné | `call_subordinate` + `reset=false` |
| **Solution/Leçon/Apprentissage créé ?** | Sauvegarder immédiatement | `memory_save` |
| **Résultat long à transmettre ?** | Inclure par référence | `§§include(path)` |

### Exceptions justifiées
- Tâche unique et simple nécessitant supervision directe
- Contexte conversationnel nécessitant continuité immédiate
- Urgence documentée avec raisonnement explicite

### Auto-évaluation rapide (mensuelle)
- Taux de délégation : ___ %
- Entrées mémoire créées : ___ / mois
- Usage de §§include() : ___ % des cas éligibles
