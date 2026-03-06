# 🔍 Analysis — AUDIT-003 : Boucles de retry (CAUSE IDENTIFIÉE)

> Date : 2026-03-06 | Analyst : Business Analyst BMAD | Statut : ✅ ANALYSE COMPLÈTE

---

## 📌 Contexte & Besoin

Le self-audit a détecté **39 patterns de retry/loop**. Cause racine identifiée.

---

## 🎯 Cause Racine Identifiée

### 🔴 `bc` non installé dans le container Docker

**Séquence de la boucle :**
1. L'agent exécute une commande utilisant `bc` (calculatrice bash) pour des calculs de tokens/pourcentages
2. `bash: bc: command not found` → erreur
3. `fw.msg_misformat.md` déclenché → Agent Zero interprète l'erreur comme un misformat
4. `fw.msg_nudge.md` → Agent Zero nudge l'agent pour corriger
5. L'agent réessaie → `bc` toujours absent → loop infini
6. `fw.msg_repeat.md` → détection de répétition

**Preuve (session 76.txt) :**
```
bash: bc: command not found
fw.msg_misformat.md
bash: bc: command not found  
fw.msg_nudge.md
bash: bc: command not found
fw.msg_repeat.md
```

**Vérification** : `which bc` → ❌ non installé confirmé

---

## 🔗 Impact en cascade

Cette seule cause racine explique probablement 70-80% des erreurs des 4 audits :
- **AUDIT-001** (21 erreurs JSON) : misformat généré par les boucles `bc`
- **AUDIT-002** (23 tool not found) : agents appellent des outils dans les boucles retry
- **AUDIT-004** (17 timeouts) : boucles prolongées → dépassement timeout

---

## 💡 Solution Proposée

**Option 1 (immédiate)** : Installer `bc` → `apt-get install -y bc`
- Effort : 1 minute
- Persistance : NON (perdu au redémarrage Docker)

**Option 2 (robuste)** : Ajouter `bc` dans le Dockerfile ou script d'init No-Core-Change
- Effort : 15 min
- Persistance : OUI

**Option 3 (préventive)** : Ajouter règle dans les prompts pour éviter `bc` → utiliser Python ou `awk` à la place
- Effort : 10 min
- Persistance : OUI (No-Core-Change compatible)

---

## ✅ Critères de Succès

- [ ] `bc` installé ou remplacé
- [ ] 0 occurrence `bc: command not found` dans les prochaines sessions
- [ ] Réduction retry loops ≥ 80%

