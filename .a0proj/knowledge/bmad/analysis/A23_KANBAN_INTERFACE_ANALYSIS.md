# 🔍 Analysis — A23 : Interface Kanban PO ↔ Agent Zero

> Date : 2026-03-06 | Analyst : Business Analyst BMAD | Statut : 🔄 EN COURS

---

## 📌 Contexte & Besoin

**Constat** : L'interface actuelle PO ↔ Agent Zero est un chat textuel. Pour un flux de travail agile, le PO doit exprimer ses intentions en langage naturel, puis vérifier manuellement le backlog markdown.

**Besoin exprimé** : Un Kanban board visuel synchronisé avec BACKLOG.md, où le PO interagit avec Agent Zero comme avec une équipe agile (colonnes To Do / In Progress / Done).

---

## 🎯 Critères de Succès

- [ ] Visualisation en temps réel du BACKLOG.md sous forme de Kanban
- [ ] Actions PO depuis le board (déplacer carte = changer statut)
- [ ] Synchronisation bidirectionnelle Kanban ↔ BACKLOG.md
- [ ] Compatible No-Core-Change (pas de modif core A0)
- [ ] Accessible depuis l'interface existante ou via URL dédiée

---

## ❓ Questions de Découverte

1. **Outil existant ou custom ?** : Faut-il intégrer un outil existant (GitHub Projects, Trello, Notion, Linear) ou développer une interface custom ?
2. **Niveau d'intégration** : Lecture seule (Kanban affiche backlog) ou bidirectionnel (Kanban modifie backlog) ?
3. **Déclencheur Agent** : Les actions Kanban doivent-elles déclencher Agent Zero directement ou seulement modifier le backlog ?
4. **Authentification** : Accès restreint PO uniquement ou toute l'équipe ?
5. **Périmètre** : Un Kanban par projet ou global tous projets ?
6. **Effort acceptable** : L'effort (probablement 10-20h) est-il justifié par le gain d'expérience PO ?
7. **Contrainte déploiement** : Sur le VPS existant ? Sur port dédié ?

---

## 🔗 Dépendances

- BACKLOG.md (format actuel en tableau markdown)
- Infrastructure VPS (ports disponibles)
- Potentiellement : API Agent Zero pour déclencher des actions

---

## ⚠️ Risques Identifiés

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| Désynchronisation Kanban/BACKLOG | Haut | Haut | BACKLOG.md reste SSOT, Kanban est vue |
| Effort sous-estimé | Haut | Moyen | Commencer par un MVP lecture seule |
| Outil tiers = dépendance externe | Moyen | Moyen | Préférer solution hébergée localement |

---

## 💡 Pistes Préliminaires

- **Option A** : GitHub Projects synchronisé avec BACKLOG.md (via GitHub Actions)
- **Option B** : Interface web légère (Flask/FastAPI) parsant BACKLOG.md → Kanban
- **Option C** : Plugin/widget dans l'interface Agent Zero existante

---

## 📋 Livrables Attendus

- Comparatif des 3 options avec effort/complexité
- Décision PO sur l'approche
- PoC si validation

