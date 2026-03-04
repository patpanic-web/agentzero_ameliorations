# BACKLOG - Agent-Zero: Modular Optimizer

## 📋 Tâches Actives

---

### Tâche #1 : Stratégie Multi-Modèles et Délégation Optimisée

**UUID** : `MM-DELEG-001`
**Priorité** : Haute 🔴
**Status** : EN COURS - Implémentation en cours
**Date de création** : 2026-03-04

#### 📝 Description

Implémenter une architecture multi-modèles pour optimiser les coûts tout en maintenant la qualité, avec une délégation active vers les agents subordonnés pour les tâches d'exécution.

#### ✅ Vérification de Compatibilité Effectuée

- **Date** : 2026-03-04
- **Version Agent Zero** : v0.9.8.2
- **Status** : ✅ COMPATIBLE
- **Détails** : Voir `VERIFICATION_COMPATIBILITE.md`

#### 🎯 Objectifs

1. **Réduction des coûts** : 44-89% via routing intelligent
2. **Maintien de la qualité** : Claude/GPT pour raisonnement, DeepSeek/Gemini pour exécution
3. **Délégation active** : Agent 0 se concentre sur planification et supervision

#### 📦 Sous-tâches

##### 1. Configuration des Modèles Subordonnés
**Priorité** : Haute

Fichiers à créer :

```
/a0/usr/agents/developer/settings.json
/a0/usr/agents/hacker/settings.json
/a0/usr/agents/researcher/settings.json
```

Configuration recommandée :

**developer** : DeepSeek V3.2 (économique, bon pour code)
```json
{
  "chat_model_provider": "openrouter",
  "chat_model_name": "deepseek/deepseek-v3.2",
  "chat_model_ctx_length": 64000,
  "chat_model_vision": false
}
```

**hacker** : Gemini 2.0 Flash (rapide, économique)
```json
{
  "chat_model_provider": "google",
  "chat_model_name": "gemini-2.0-flash",
  "chat_model_ctx_length": 100000,
  "chat_model_vision": true
}
```

**researcher** : DeepSeek V3.2 (économique, bon pour recherche)
```json
{
  "chat_model_provider": "openrouter",
  "chat_model_name": "deepseek/deepseek-v3.2",
  "chat_model_ctx_length": 64000
}
```

##### 2. Délégation Forcée via Prompts
**Priorité** : Haute

Fichier à créer : `/a0/usr/agents/agent0/prompts/agent.system.main.role.md`

Contenu recommandé :

```markdown
## Delegation Policy (CRITICAL)

ALWAYS delegate to specialized subordinates when:
- Writing unit tests, boilerplate code, documentation
- Performing repetitive tasks or bulk operations
- Executing standard security scans or audits
- Conducting research or data gathering

PREFER subordinates for execution tasks.
Your role is PLANNING and SUPERVISION, not execution.
Keep yourself available for complex reasoning and user interaction.
```

##### 3. Tests et Validation
**Priorité** : Moyenne

- [ ] Tester le chargement des settings par profil
- [ ] Vérifier les logs de délégation
- [ ] Mesurer les coûts réels vs estimés
- [ ] Ajuster les prompts si nécessaire

##### 4. Documentation
**Priorité** : Basse

- [ ] Documenter la configuration finale
- [ ] Créer un guide de maintenance

#### ⚠️ Contraintes Techniques

1. **NE PAS modifier les fichiers core** (`/a0/agents/`, `/a0/prompts/`)
2. **Utiliser uniquement `/a0/usr/agents/`** pour les overrides
3. **Préserver la configuration existante** (GLM-5 + Llama-4-Scout)
4. **Ne pas recréer les agents**, seulement modifier leur comportement

#### 📊 Analyse Coûts/Bénéfices

| Configuration | Coût/1M tokens | Économie |
|---------------|----------------|----------|
| Actuelle (GLM-5 only) | $1.48 | - |
| Proposée (sans délégation) | $7.00 | ❌ +373% |
| Proposée (80% délégation) | $1.51 | ≈ équivalent |
| Proposée (90% délégation) | $0.83 | ✅ -44% |

#### 📁 Fichiers de Référence

- `ANALYSE_MULTI_MODEL_STRATEGY.md` - Analyse initiale
- `VERIFICATION_COMPATIBILITE.md` - Vérification technique

---

## 📚 Archives

*Aucune tâche archivée*

---

## 🚀 Opportunités / Backlog Futur

### Opportunité #1 : MCP data.gouv.fr - Données Publiques Françaises

**UUID** : `DATA-GOUV-001`
**Priorité** : Moyenne 🟡 (à explorer)
**Status** : IDENTIFIÉ - Veille technologique
**Date de création** : 2026-03-04

#### 📝 Description

L'État français a lancé un **MCP gratuit** donnant accès à toutes ses données publiques. Pépite pour l'investissement immobilier.

#### 🎯 Cas d'usage potentiels

| Domaine | Données disponibles |
|---------|-------------------|
| **Cadastre** | Parcelles, propriétés, zones constructibles |
| **Immobilier** | Valeurs foncières, transactions, DPE |
| **Démographie** | Population, migrations, tendances |
| **Entreprises** | API Sirene, dirigeants, santé financière |
| **Accidentologie** | Zones à risque, sécurité routière |

#### 💡 Projet futur envisagé

**Agent-Zero pour l'investissement immobilier** :
- Analyse de marché automatisée
- Screening de biens/terrains
- Évaluation des risques (inondation, accidentologie...)
- Étude démographique et économique
- Recherche de données entreprises locales

#### ⚙️ Installation

- Compatible Claude / ChatGPT
- Installation en quelques secondes
- **Gratuit**

#### 📌 Actions futures

- [ ] Identifier le nom exact du MCP sur GitHub/registry
- [ ] Tester l'intégration avec Agent-Zero
- [ ] Évaluer la qualité des données
- [ ] Créer un skill dédié à l'analyse immobilière

#### 📎 Référence

- Memory ID : `9azGHOqq5Q`
- Source : Actualité tech mars 2026


---

### Tâche #2 : Auto-Diagnostic des Erreurs Récurrentes

**UUID** : `AUTO-DIAG-001`
**Priorité** : Haute 🔴
**Status** : 🟡 ANALYSIS EN COURS - À approfondir avant validation PO
**Date de création** : 2026-03-04

#### 📝 Description

Analyse systématique des erreurs récurrentes commises par l'agent pour identifier les patterns problématiques et proposer des solutions d'amélioration modulaires (skills, mémoires, protocoles).

#### 🎯 Objectifs

1. **Identifier** les erreurs récurrentes et leurs fréquences
2. **Analyser** les causes racines de chaque type d'erreur
3. **Proposer** des solutions "no-core-change" (skills, mémoires)
4. **Mesurer** l'impact des corrections

#### 📦 Phases BMAD

##### Phase 1: ANALYSIS (En cours) 🟡
**Statut:** Données préliminaires collectées, nécessite approfondissement

**Fichiers:**
- `.a0proj/knowledge/bmad/analysis/AUTO_DIAGNOSTIC_ERREURS.md`
- `.a0proj/knowledge/bmad/analysis/COLLECTE_DONNEES.md`

**Actions à compléter:**
- [ ] Collecter les logs d'erreurs réels sur 30 jours
- [ ] Catégoriser les erreurs par fréquence et impact
- [ ] Identifier les causes racines spécifiques
- [ ] Valider les hypothèses avec des métriques
- [ ] Répondre aux questions pour le PO

**Questions pour le PO:**
1. Y a-t-il des logs d'erreurs centralisés ?
2. Quels sont les échecs les plus fréquemment rencontrés ?
3. Quelles métriques de performance sont actuellement suivies ?
4. Y a-t-il des retours utilisateurs sur les comportements problématiques ?

##### Phase 2: PLANNING (À valider) ⬜
**Dépendance:** Validation du PO sur l'analyse

##### Phase 3: SOLUTIONING (À planifier) ⬜
**Dépendance:** Planning validé

##### Phase 4: IMPLEMENTATION (À planifier) ⬜
**Dépendance:** Solution validée

#### 📊 Erreurs Identifiées (Préliminaire)

| ID | Catégorie | Fréquence Est. | Impact | Priorité |
|----|-----------|----------------|--------|----------|
| E001 | Format JSON invalide | Haute (30%+) | Bloquant | P0 |
| E002 | Boucles retry infinies | Moyenne (15%) | Critique | P1 |
| E003 | Timeouts non gérés | Moyenne (12%) | Élevé | P1 |
| E004 | Mauvais usage d'outils | Moyenne (10%) | Élevé | P2 |
| E005 | Hallucinations de données | Basse (8%) | Moyen | P2 |
| E006 | Chemins fichiers incorrects | Basse (5%) | Moyen | P3 |
| E007 | Exposition de secrets | Très basse (2%) | Critique | P1 |

#### 🎯 Solutions Proposées (À valider)

| Solution | Type | Phase |
|----------|------|-------|
| `json_guard` skill | Skill externe | Sprint 1 |
| `retry_linter` skill | Skill externe | Sprint 1 |
| `bmad_protocol` skill | Skill externe | Sprint 2 |
| `timeout_helper` skill | Skill externe | Sprint 2 |
| Mémoires critiques | Mémoire système | Sprint 1 |

#### ⚠️ Blocages Actuels

- **Données manquantes:** Pas de logs d'erreurs centralisés
- **Validation requise:** Approfondissement nécessaire avant décision PO
- **Métriques indisponibles:** Aucune mesure quantitative actuelle

#### 📁 Fichiers de Référence

- `AUTO_DIAGNOSTIC_ERREURS.md` - Document d'analyse principal
- `COLLECTE_DONNEES.md` - Checklist de collecte de données

---
