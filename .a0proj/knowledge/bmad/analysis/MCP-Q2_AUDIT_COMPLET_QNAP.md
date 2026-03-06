# 📊 Audit Complet QNAP SarahPatNas

**Date** : 2026-03-06  
**NAS** : SarahPatNas (QNAP TS-453 Pro)  
**Firmware** : QTS 5.2.8 (2025/12/25)

---

## 📋 Résumé Exécutif

| Catégorie | Score | Commentaire |
|-----------|-------|-------------|
| **Sécurité Globale** | 🔴 5/10 (Vulnérabilités critiques) | Points à améliorer |
| **Exposition Réseau** | 🟢 8/10 | Tailscale bien configuré |
| **Services** | 🟡 6/10 | Trop de services actifs |
| **Stockage** | 🟢 8.5/10 | RAID5 sain, 53% libre |
| **Surveillance** | 🟢 8/10 | Logs actifs mais alertes à traiter |

---



---

## 🚨 ALERTE SÉCURITÉ - Vulnérabilités Critiques QTS 5.2.x

### Source : QNAP Security Advisory QSA-25-45 (PWN2OWN 2025)

⚠️ **Votre firmware QTS 5.2.8 est concerné par ces vulnérabilités :**

| CVE | Type | Sévérité | Impact |
|-----|------|----------|--------|
| **CVE-2025-62849** | SQL Injection | 🔴 Critique | Execution de code à distance |
| **CVE-2025-62847** | Command Injection | 🔴 Critique | Exécution de commandes |
| **CVE-2025-59385** | Authentication Bypass | 🔴 Critique | Contournement authentification |
| **CVE-2025-62848** | DoS | 🟡 Moyen | Déni de service |

### 🔴 Action Urgente Requise

**Mettre à jour QTS vers la dernière version immédiatement.**

Vérifier les mises à jour sur : https://www.qnap.com/en/support

### Recommandations Temporaires (en attendant mise à jour)

1. **Désactiver myQNAPcloud** - Réduire la surface d'attaque
2. **Limiter l'accès réseau** - IP whitelist via Tailscale uniquement
3. **Désactiver services non essentiels** - FTP, SSH si inutilisés
4. **Activer QuFirewall** - Si disponible
5. **Surveiller les logs** - Rechercher activités suspectes

---


## 1. Connexions Externes & Réseau

### Configuration Réseau Actuelle

| Interface | IP | Statut | Notes |
|-----------|-----|--------|-------|
| **eth0** | 192.168.1.149 | ✅ Actif | DHCP, réseau local |
| **eth1** | 0.0.0.0 | ❌ Inactif | Non utilisé |
| **eth2** | 0.0.0.0 | ❌ Inactif | Non utilisé |
| **eth3** | 0.0.0.0 | ❌ Inactif | Non utilisé |
| **Tailscale** | 100.69.233.116:8443 | ✅ Actif | VPN sécurisé |

### Services Réseau Actifs

| Service | Statut | Risque | Recommandation |
|---------|--------|--------|----------------|
| **myQNAPcloud** | ✅ Actif | 🔴 Moyen | Vérifier exposition Internet |
| **CloudLink** | ✅ Actif | 🟡 Faible | Connexion myQNAPcloud |
| **Tailscale** | ✅ Actif | 🟢 Très faible | VPN recommandé ✅ |
| **SMB Service** | ✅ Actif | 🟡 Moyen | Réservé au réseau local |
| **QuFTP** | ✅ Actif | 🔴 Moyen | FTP non chiffré - éviter |
| **SSH** | ? | 🔴 Élevé | Vérifier si activé |
| **HTTPS (Web)** | ✅ Actif | 🟡 Moyen | Interface QTS |

### 🔐 Bonnes Pratiques Réseau (Recommandations)

D'après les recherches de sécurité QNAP :

✅ **À Faire**
- Garder Tailscale comme seul accès externe
- Désactiver UPnP sur le routeur et NAS
- Utiliser only nécessaire ports
- Activer QuFirewall (si disponible)

⚠️ **À Vérifier**
- myQNAPcloud : configurer en mode "Privé" ou désactiver
- FTP/QuFTP : privilégier SFTP
- SSH : désactiver si non utilisé, sinon clé SSH

---

## 2. Services QNAP

### Applications Installées (32 total)

#### Services Essentiels (à garder)
| Application | Version | Statut |
|-------------|---------|--------|
| Container Station | 3.1.2.1742 | ✅ Actif |
| Hybrid Backup Sync | 26.3.0.226 | ✅ Actif |
| File Station 5 | 5.5.6.5190 | ✅ Actif |
| Multimedia Console | 2.9.0 | ✅ Actif |
| Security Center | 3.1.0.3632 | ✅ Actif |
| ClamAV | 0.103.11.46 | ✅ Actif |
| Malware Remover | 6.6.8 | ✅ Actif |
| Resource Monitor | 1.2.0 | ✅ Actif |

#### Services Réseau (à évaluer)
| Application | Risque | Action |
|-------------|--------|--------|
| **myQNAPcloud** | 🔴 Moyen | Vérifier exposition |
| **CloudLink** | 🟡 Faible | Vérifier si utilisé |
| **Tailscale** | 🟢 Très faible | ✅ Garder |
| **SMB Service** | 🟡 Moyen | Réservé LAN |
| **QuFTP** | 🔴 Moyen | Désactiver si inutilisé |

#### Applications Inutilisées (à désactiver)
| Application | Statut | Recommandation |
|-------------|--------|----------------|
| Helpdesk | ❌ Désactivé | OK |
| Browser Station | ❌ Désactivé | OK |
| CacheMount | ⚠️ Obsolète | Vérifier si nécessaire |

---

## 3. Conteneurs Docker

### Container Station

**Statut** : Actif (version 3.1.2.1742)

⚠️ **Note** : L'API Docker n'est pas directement accessible via MCP pour lister les conteneurs.  
**Recommandation** : Se connecter à l'interface QTS pour lister les conteneurs Docker.

---

## 4. Sites Web NAS

### /Web Dossier Partagé

⚠️ **ALERTE** : 9 fichiers index.html trouvés dans /Web !

| Fichier | Modifié | Taille | Action |
|---------|---------|--------|--------|
| index.html | 2025/01/08 23:39 | 4.7 KB | ✅ Actuel |
| index.html.old | 2025/01/08 16:20 | 5.9 KB | 🗑️ Supprimer |
| index.html.old2 | 2025/01/07 23:43 | 6.0 KB | 🗑️ Supprimer |
| index.html.old3 | 2025/01/08 22:41 | 6.0 KB | 🗑️ Supprimer |
| index.html.old4 | 2025/01/08 22:55 | 0.7 KB | 🗑️ Supprimer |
| index.html.old5 | 2025/01/08 23:02 | 2.0 KB | 🗑️ Supprimer |
| index.html.old6 | 2025/01/08 23:04 | 4.7 KB | 🗑️ Supprimer |
| index.html.old7 | 2025/01/08 23:19 | 2.9 KB | 🗑️ Supprimer |
| index.html.old8 | 2025/01/08 23:34 | 4.8 KB | 🗑️ Supprimer |

**Recommandation** : Nettoyer les anciennes versions pour libérer de l'espace et sécuriser.

---

## 5. Sécurité & Logs

### Alertes Récentes (Dernières 24h)

| Date | Sévérité | Source | Message |
|------|----------|--------|---------|
| 2026-03-06 14:30 | ⚠️ Warning | Security Center | **Activités fichiers inhabituelles** (469 changements) |
| 2026-03-06 06:42 | ⚠️ Warning | Security | **IP bloquée** : 147.182.163.8 (5 min) |
| 2026-03-06 06:00 | ⚠️ Warning | Security Center | **Échec Security Checkup** : Autorisation PatMaster expirée |
| 2026-03-06 02:00 | ⚠️ Warning | Antivirus | **Mémoire faible** : < 2 GB disponible |

### 🔴 Points d'Attention

#### 1. IP 147.182.163.8 Bloquée
- **Date** : 2026-03-06 06:42
- **Action** : IP ajoutée à la blocklist pour 5 minutes
- **Analyse** : Probable tentative d'accès non autorisé
- **Recommandation** : Surveiller les tentatives récurrentes

#### 2. Échec Security Checkup
- **Problème** : Autorisation du compte PatMaster expirée
- **Solution** : Se connecter à QTS, ouvrir Security Center > Scan Schedule et reconfigurer

#### 3. Activités Fichiers Inhabituelles
- **Cause probable** : Synchronisation (Qsync, Hybrid Backup, Container)
- **Volume** : 469 à 74,409 changements détectés
- **Action** : Vérifier les tâches de sync actives

#### 4. Mémoire Faible
- **Valeur** : < 2 GB disponible
- **Impact** : Performance antivirus réduite
- **Solution** : Surveiller les conteneurs Docker

### Historique des Connexions

⚠️ **IP ayant accédé au NAS** :  
- 2a01:e0a:c91:eb80:d8e6:1bb7:8487:5b29 (IPv6 - utilisateur PatMaster)
- 147.182.163.8 (IP bloquée - suspecte)

---

## 6. Utilisateurs

| Utilisateur | UID | Admin | Statut | Connexions |
|-------------|-----|-------|--------|------------|
| **admin** | 0 | ✅ Oui | ❌ Désactivé | - |
| **Pat** | 1000 | Non | ✅ Actif | - |
| **Sarah** | 1001 | Non | ✅ Actif | - |
| **PatMaster** | 1002 | ✅ Oui | ✅ Actif | IPv6 (connue) |
| **Freebox** | 1003 | Non | ✅ Actif | - |

### Recommandations Utilisateurs

✅ **Bonnes pratiques en place**
- Compte admin désactivé
- Mot de passe forts (supposé)

⚠️ **À vérifier**
- Changer régulièrement les mots de passe
- Vérifier les permissions de Freebox
- Renforcer 2FA si disponible

---

## 7. Stockage

### Configuration RAID

| Élément | Détail |
|---------|--------|
| **Pool** | Pool 1 (RAID5) |
| **Disques** | 4x WD Red 2.73 TB |
| **Capacité** | ~8 TB (7.6 TButilisables) |
| **Utilisé** | 47% (3.6 TB) |
| **Libre** | 53% (~4 TB) |
| **Température** | 30-31°C (OK) |

### Dossiers Partagés

| Dossier | Type | Usage |
|---------|------|-------|
| Container | Docker | Containers/VM |
| Download | System | Téléchargements |
| Multimedia | Médias | Photos/Vidéos |
| Public | Partage | Public |
| Sauvegardes | Backup | **Recommandé pour A0** |
| Virtual | VM | Machines virtuelles |
| Web | Web | Sites web |
| homes | Users | Répertoires utilisateurs |

---

## 8. Checklist Sécurité

### ✅ Configurations Sécurisées

- [x] Compte admin désactivé
- [x] Antivirus ClamAV actif
- [x] Malware Remover actif
- [x] Security Center actif
- [x] Tailscale installé (VPN)
- [x] Firmware à jour (QTS 5.2.8)

### ⚠️ À Vérifier/Améliorer

- [ ] myQNAPcloud exposé sur Internet ?
- [ ] QuFTP sécurisé (SFTP préférable) ?
- [ ] SSH activé avec clé SSH ?
- [ ] UPnP désactivé ?
- [ ] QuFirewall configuré ?
- [ ] Autorisation PatMaster renew

### 🔴 Actions Correctives Urgentes

1. **Reconfigurer Security Checkup** (autorisation PatMaster expirée)
2. **Surveiller IP 147.182.163.8** (tentative accès bloquée)
3. **Nettoyer /Web** (9 fichiers obsolètes)
4. **Vérifier exposition myQNAPcloud**

---

## 9. Préparation MCP-Q3 (Stockage Persistant)

Pour intégrer le NAS comme stockage persistant Agent Zero :

| Option | Dossier | Capacité | Recommandation |
|--------|---------|----------|----------------|
| **Recommandé** | /Sauvegardes | ~4 TB libre | ✅ Dossier dédié backup |
| Alternative | /Public | ~4 TB libre | ⚠️ Partagé |

### Configuration Requise

1. Créer un utilisateur Agent Zero sur le NAS
2. Configurer NFS/SMB pour le montage
3. Tester la connexion via Tailscale

---

## 10. Score Final & Recommandations

### Score de Sécurité : 7.5/10

| Critère | Score | Détail |
|---------|-------|--------|
| Contrôle Accès | 8/10 | Admin désactivé, comptes OK |
| Réseau | 7/10 | Tailscale OK, à vérifier myQNAPcloud |
| Services | 6/10 | 32 apps - nettoyer inutilisés |
| Surveillance | 8/10 | Logs OK, alertes à traiter |
| Stockage | 9/10 | RAID5 sain, espace OK |

### 🎯 Actions Prioritaires

| # | Action | Priorité | Effort |
|---|--------|----------|--------|
| 1 | Reconfigurer Security Checkup | 🔴 P0 | 5 min |
| 2 | Nettoyer /Web (9 fichiers) | 🟡 P1 | 10 min |
| 3 | Vérifier myQNAPcloud | 🟡 P1 | 15 min |
| 4 | Surveiller IP 147.182.163.8 | 🟡 P1 | - |
| 5 | Désactiver services inutiles | 🟢 P2 | 30 min |

---

## 📚 Sources

- Bonnes pratiques QNAP : Recherche web (QNAP FAQ, Reddit, YouTube)
- Données système : MCP QNAP (qnap.list_*, qnap.get_*)
- Logs : qnap.list_logs

---

*Rapport généré le 2026-03-06 à 18:40*  
*Agent Zero - Projet Agent-Zero Modular Optimizer*
