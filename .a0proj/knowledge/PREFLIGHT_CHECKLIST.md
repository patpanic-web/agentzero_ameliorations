# Pre-Flight Checklist — Agent Zero
> À consulter AVANT chaque réponse finale
> Objectif : renforcer délégation et mémoire

## ✅ Questions obligatoires (check mentale)

### 1. Délégation — "Cette tâche mérite-t-elle un subordonné ?"
- [ ] Création de code (tests, boilerplate, scripts répétitifs) → **DELEGATE → developer**
- [ ] Audit sécurité, pentest, scan → **DELEGATE → hacker**
- [ ] Recherche web massive, documentation → **DELEGATE → researcher**
- [ ] Analyse de fichiers complexes → **DELEGATE → profil adapté**
- [ ] Tâche unique, simple, nécessitant ma supervision → **OK pour execution directe**

### 2. Mémoire — "Ai-je quelque chose à mémoriser ici ?"
- [ ] Solution réutilisable découverte → **memory_save**
- [ ] Erreur évité / leçon apprise → **memory_save**
- [ ] Information contextuelle pour futures sessions → **memory_save**
- [ ] Rien de nouveau → **OK, continuer**

### 3. Optimisation — "Puis-je utiliser §§include() au lieu de réécrire ?"
- [ ] Résultat de subordonné long → **§§include(path)**
- [ ] Contenu de fichier déjà disponible → **§§include(path)**
- [ ] Court ou reformulation nécessaire → **Réécriture OK**

## 🚨 Règles d'or

| Situation | Action requise |
|-----------|----------------|
| Tâche d'exécution standard | call_subordinate + reset=true |
| Itération sur résultat | call_subordinate + reset=false |
| Apprentissage créé | memory_save immédiat |
| Résultat long à transmettre | §§include() obligatoire |

## 📊 Auto-évaluation rapide
- Délégation ce mois : ___ / 10
- Mémoire sauvegardée ce mois : ___ entrées
- §§include() utilisé : ___ fois

---
*Dernière mise à jour : 2026-03-08*
*Lié à : BACKLOG_GLOBAL.md G-001*
