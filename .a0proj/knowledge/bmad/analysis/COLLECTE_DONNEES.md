# 📋 Collecte de Données - Erreurs Récurrentes

> **Statut:** ⬜ À collecter
> **Date début:** 2026-03-04
> **Responsable:** Agent Zero

---

## 1. Données à Collecter

### 1.1 Logs d'Erreurs JSON

| Date | Fichier Source | Type Erreur | Fréquence | Notes |
|------|----------------|-------------|-----------|-------|
| - | - | - | - | - |

**Méthode de collecte:**
```bash
# Rechercher les erreurs JSON dans les logs
grep -r "error\|invalid\|parse" /a0/usr/chats/ --include="*.txt" | head -100
```

### 1.2 Patterns de Retry

| Date | Contexte | Boucle détectée | Temps perdu | Notes |
|------|----------|-----------------|-------------|-------|
| - | - | - | - | - |

**Méthode de collecte:**
```bash
# Rechercher les patterns de retry
grep -r "retry\|tentative\|while True" /a0/usr/chats/ --include="*.txt" | head -100
```

### 1.3 Timeouts

| Date | Opération | Durée | Contexte | Notes |
|------|-----------|-------|----------|-------|
| - | - | - | - | - |

### 1.4 Erreurs d'Outils

| Outil | Erreur | Fréquence | Cause probable | Notes |
|-------|--------|-----------|----------------|-------|
| - | - | - | - | - |

### 1.5 Hallucinations

| Date | Contexte | Type hallucination | Impact | Notes |
|------|----------|-------------------|--------|-------|
| - | - | - | - | - |

---

## 2. Questions pour le PO

### Prioritaires
1. **Y a-t-il des logs d'erreurs centralisés ?**
   - Réponse: ⬜ À compléter
   
2. **Quels sont les échecs les plus fréquemment rencontrés ?**
   - Réponse: ⬜ À compléter
   
3. **Quelles métriques de performance sont actuellement suivies ?**
   - Réponse: ⬜ À compléter
   
4. **Y a-t-il des retours utilisateurs sur les comportements problématiques ?**
   - Réponse: ⬜ À compléter

---

## 3. Checklist Avancement

- [ ] Collecter 30 jours de logs
- [ ] Analyser les erreurs JSON
- [ ] Identifier les patterns retry
- [ ] Documenter les timeouts
- [ ] Catégoriser les erreurs d'outils
- [ ] Noter les hallucinations
- [ ] Compléter les root causes
- [ ] Valider les hypothèses

---

## 4. Prochaine Action

**Commande à exécuter pour démarrer la collecte:**

```bash
# Analyser les conversations des 7 derniers jours
find /a0/usr/chats -name "*.txt" -type f -mtime -7 -exec grep -l "error\|erreur\|failed\|invalid" {} \;
```

---

*Document de travail - Phase ANALYSIS*
