# 📊 PHASE ANALYSIS - Auto-Diagnostic des Erreurs Récurrentes

> **Dernière mise à jour:** 2026-03-04
> **Statut:** 🟡 EN COURS - À APPROFONDIR AVANT VALIDATION PO
> **Agent:** Agent Zero (agent0)

---

## ⚠️ NOTE IMPORTANTE

**Cette analyse est préliminaire et nécessite un approfondissement avant toute décision ou validation par le Product Owner.**

Les données présentées ci-dessous sont basées sur:
- Patterns d'erreurs types des agents LLM
- Connaissances générales des erreurs courantes
- Analyse sommaire de l'historique de conversation

**Actions requises pour compléter l'analyse:**
1. Collecter les logs d'erreurs réels sur les 30 derniers jours
2. Catégoriser les erreurs par fréquence et impact
3. Identifier les causes racines spécifiques à cet agent
4. Valider les hypothèses avec des métriques

---

## 1. Erreurs Identifiées (Préliminaire)

### 1.1 Types d'Erreurs Récurrentes

| ID | Catégorie | Fréquence Est. | Impact | Priorité |
|----|-----------|----------------|--------|----------|
| E001 | Format JSON invalide | Haute (30%+) | Bloquant | P0 |
| E002 | Boucles retry infinies | Moyenne (15%) | Critique | P1 |
| E003 | Timeouts non gérés | Moyenne (12%) | Élevé | P1 |
| E004 | Mauvais usage d'outils | Moyenne (10%) | Élevé | P2 |
| E005 | Hallucinations de données | Basse (8%) | Moyen | P2 |
| E006 | Chemins fichiers incorrects | Basse (5%) | Moyen | P3 |
| E007 | Exposition de secrets | Très basse (2%) | Critique | P1 |

### 1.2 Détail par Erreur

#### E001 - Format JSON Invalide

**Description:**
- Oubli de virgules entre les champs
- Guillemets mal échappés dans les strings multilignes
- Accolades/brackets non fermés
- Syntaxe invalide dans tool_args

**Symptômes observés:**
```json
// Exemple d'erreur typique
{
  "thoughts": ["..."],
  "tool_name": "response",
  "tool_args": {
    "text": "Un texte avec \"guillemets\" non échappés"  // ❌ Erreur
  }
}
```

**Données manquantes:**
- [ ] Fréquence exacte sur les 30 derniers jours
- [ ] Types d'erreurs JSON les plus courants
- [ ] Impact sur le flux de conversation

---

#### E002 - Boucles Retry Infinies

**Description:**
- Retry sans compteur maximum
- Absence de backoff exponentiel
- Conditions d'arrêt non définies

**Code problématique typique:**
```python
# ❌ Pattern à éviter
while True:
    result = try_something()
    if result.success:
        break
    # Pas de max_attempts!
```

**Données manquantes:**
- [ ] Nombre de boucles infinies détectées
- [ ] Temps moyen avant détection/arrêt
- [ ] Impact sur les ressources système

---

#### E003 - Timeouts Non Gérés

**Description:**
- Oubli d'utiliser `runtime: "output"` pour processus longs
- Absence de timeout dans les appels réseau
- Blocage sur des entrées utilisateur attendues

**Données manquantes:**
- [ ] Nombre de timeouts dans les logs
- [ ] Temps moyen des opérations qui timeout
- [ ] Contextes les plus fréquents de timeout

---

#### E004 - Mauvais Usage d'Outils

**Description:**
- Arguments incorrects ou manquants
- Outil non adapté à la tâche
- Confusion entre outils similaires

**Données manquantes:**
- [ ] Liste des erreurs d'arguments par outil
- [ ] Outils les plus sujets à erreur
- [ ] Taux d'erreur par type d'outil

---

#### E005 - Hallucinations

**Description:**
- Affirmations sans vérification
- Données inventées ou obsolètes
- Confiance excessive dans les outputs LLM

**Données manquantes:**
- [ ] Cas d'hallucination documentés
- [ ] Impact sur la qualité des réponses
- [ ] Contextes à risque d'hallucination

---

#### E006 - Chemins Fichiers Incorrects

**Description:**
- Chemins relatifs mal résolus
- Écrasement de fichiers existants
- Permissions insuffisantes

**Données manquantes:**
- [ ] Types d'erreurs fichiers
- [ ] Chemins les plus problématiques

---

#### E007 - Exposition de Secrets

**Description:**
- Affichage de credentials dans les outputs
- Logs contenant des secrets
- Fichiers de configuration exposés

**Données manquantes:**
- [ ] Audit de sécurité à réaliser
- [ ] Patterns de fuite potentiels

---

## 2. Root Cause Analysis (À Compléter)

```
┌─────────────────────────────────────────────────────────────┐
│                    ARBRE DES CAUSES                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Erreur JSON (E001)                                         │
│  ├── Cause racine 1: ? (à identifier)                       │
│  ├── Cause racine 2: ? (à identifier)                       │
│  └── Cause racine 3: ? (à identifier)                       │
│                                                             │
│  Boucle infinie (E002)                                      │
│  ├── Cause racine 1: ? (à identifier)                       │
│  └── Cause racine 2: ? (à identifier)                       │
│                                                             │
│  Timeout (E003)                                             │
│  └── Cause racine: ? (à identifier)                         │
│                                                             │
│  [À compléter après analyse approfondie]                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Métriques à Collecter

| Métrique | Source | Status |
|----------|--------|--------|
| Nombre total d'erreurs JSON | Logs API | ⬜ À collecter |
| Fréquence retry loops | Logs execution | ⬜ À collecter |
| Temps moyen avant timeout | Métriques système | ⬜ À collecter |
| Taux d'erreur par outil | Analytics | ⬜ À collecter |
| Cas d'hallucination | Feedback utilisateur | ⬜ À collecter |

---

## 4. Hypothèses à Valider

| ID | Hypothèse | Status | Preuve |
|----|-----------|--------|--------|
| H1 | Les erreurs JSON représentent >30% des échecs | ⬜ À valider | - |
| H2 | Une validation pré-envoi réduit les erreurs de 50%+ | ⬜ À valider | - |
| H3 | Le skill BMAD réduit les solutions précipitées | ⬜ À valider | - |
| H4 | L'inclusion vs réécriture économise >20% tokens | ⬜ À valider | - |

---

## 5. Prochaines Étapes (Analysis)

### 5.1 Collecte de Données

- [ ] **Extraire les logs des 30 derniers jours**
  - Chemin: `/a0/logs/` ou `/a0/usr/chats/`
  - Format: Analyser les fichiers .txt de conversation

- [ ] **Analyser les erreurs JSON spécifiques**
  - Parser les tool_calls échoués
  - Catégoriser par type d'erreur de syntaxe

- [ ] **Identifier les patterns de retry**
  - Chercher les boucles `while True` dans le code
  - Analyser les séquences de tentatives

### 5.2 Questions pour le PO

1. **Y a-t-il des logs d'erreurs centralisés ?**
2. **Quels sont les échecs les plus fréquemment rencontrés ?**
3. **Quelles métriques de performance sont actuellement suivies ?**
4. **Y a-t-il des retours utilisateurs sur les comportements problématiques ?**

### 5.3 Validation du Scope

- [ ] Confirmer les catégories d'erreurs prioritaires
- [ ] Définir les seuils de fréquence/impact acceptables
- [ ] Valider l'approche de collecte de données

---

## 6. Livrable de Fin de Phase

**Avant de passer à la phase PLANNING, il faut:**

✅ Données quantitatives sur les erreurs réelles
✅ Root causes identifiées et documentées
✅ Hypothèses validées ou infirmées
✅ Questions PO répondues
✅ Scope validé par le PO

**⚠️ VALIDATION REQUISE du Product Owner avant passage à PLANNING**

---

*Document généré par Agent Zero - Phase ANALYSIS en cours*
