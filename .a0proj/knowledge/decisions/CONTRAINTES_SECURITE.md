# 🔒 Contraintes de Sécurité et Persistance
> Décidé par le PO le 2026-03-05 — APPLICABLE À TOUS LES SPRINTS
> Vérifié techniquement le 2026-03-05

---

## 🔴 Règles ABSOLUES

### 1. No-Core-Change
- AUCUNE modification du code source d'Agent Zero
- Uniquement : configurations, prompts overrides, modules externes

### 2. Protection de l'Infrastructure
- NE PAS toucher à la configuration VPS (réseau, SSH, firewall, services système)
- NE PAS toucher à la configuration Docker (docker-compose, Dockerfile, volumes)
- NE PAS toucher aux fichiers core d'Agent Zero (/a0/python/, /a0/prompts/)
- Accès root disponible → responsabilité maximale

### 3. Persistance des Modifications
Toute modification DOIT survivre à :
- ✅ Redémarrage du VPS
- ✅ `docker compose down` puis `docker compose up`
- ✅ Redémarrage d'Agent Zero

---

## ✅ Vérification Persistance (2026-03-05)

### Montages Docker vérifiés
```
/dev/sda1 → /a0/usr     (ext4, rw)  ← PERSISTANT ✅
/dev/sda1 → /a0/.env    (ext4, rw)  ← PERSISTANT ✅
```

### Conséquences
| Chemin | Monté ? | Persiste docker down/up ? | Modifiable ? |
|--------|---------|--------------------------|-------------|
| `/a0/usr/` | ✅ Volume hôte | ✅ OUI | ✅ Zone de travail |
| `/a0/usr/prompts/` | ✅ (sous /a0/usr/) | ✅ OUI | ✅ Overrides prompts |
| `/a0/usr/agents/` | ✅ (sous /a0/usr/) | ✅ OUI | ✅ Profils agents |
| `/a0/usr/settings.json` | ✅ (sous /a0/usr/) | ✅ OUI | ✅ Settings globaux |
| `/a0/usr/projects/` | ✅ (sous /a0/usr/) | ✅ OUI | ✅ Données projets |
| `/a0/.env` | ✅ Volume hôte | ✅ OUI | ⚠️ Avec précaution |
| `/a0/prompts/` | ❌ Image container | ❌ NON (perdu) | ❌ INTERDIT |
| `/a0/python/` | ❌ Image container | ❌ NON (perdu) | ❌ INTERDIT |

### Conclusion Technique
> **Toutes nos modifications dans `/a0/usr/` sont automatiquement persistantes.**
> C'est exactement la zone prévue par Agent Zero pour les customisations.
> Les fichiers core dans `/a0/prompts/` et `/a0/python/` sont dans l'image Docker
> et ne DOIVENT PAS être modifiés (ils seraient perdus ET c'est du core).

---

## 📂 Zones Autorisées (VÉRIFIÉ)

| Zone | Chemin | Persiste | Usage |
|------|--------|----------|-------|
| Prompt overrides global | `/a0/usr/prompts/` | ✅ | Override des prompts core pour TOUS les agents |
| Agent profiles | `/a0/usr/agents/{profil}/prompts/` | ✅ | Override prompts par profil |
| Agent settings | `/a0/usr/agents/{profil}/settings.json` | ✅ | Config LLM et params par profil |
| Settings global | `/a0/usr/settings.json` | ✅ | Config globale (MCP, etc.) |
| Projets | `/a0/usr/projects/` | ✅ | Données et config projets |

## ⛔ Zones INTERDITES

| Zone | Chemin | Raison |
|------|--------|--------|
| Code Python A0 | `/a0/python/` | Core + non persistant |
| Prompts originaux | `/a0/prompts/` | Core + non persistant |
| Docker config | Hors container | Infrastructure |
| Config VPS | `/etc/`, services | Infrastructure |
| Variables env | `/a0/.env` | Seulement si absolument nécessaire, avec backup |

---

## 🔄 Procédure de Rollback Universelle

Pour TOUT fichier override dans `/a0/usr/` :
1. **Supprimer le fichier override** → Agent Zero revient au comportement core
2. **Redémarrer Agent Zero** (si nécessaire pour prise en compte)
3. Aucune autre action requise

Exemple :
```bash
# Rollback d'un prompt override
rm /a0/usr/agents/agent0/prompts/agent.system.main.solving.md
# → Agent Zero utilisera /a0/prompts/agent.system.main.solving.md (core)
```

---

## 🔧 Règle de Modification des Fichiers (Ajouté 2026-03-05)

### Principe : Chirurgie, pas Reconstruction
- Les fichiers override NE SONT PAS créés de zéro
- On PART du fichier original et on y apporte UNIQUEMENT les modifications nécessaires
- Les directives de base DOIVENT être préservées — on les AMÉLIORE, on ne les remplace pas
- Chaque modification doit être minimale et ciblée
- L'essence et la logique d'origine du fichier sont conservées

### Processus
1. Lire le fichier original intégralement
2. Identifier les lignes/sections problématiques spécifiques
3. Modifier UNIQUEMENT ces parties
4. Vérifier que le reste est intact
5. Documenter les changements effectués (diff)
