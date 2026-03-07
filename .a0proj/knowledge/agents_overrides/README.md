# Agents Overrides

Ce dossier contient la copie versionnée des fichiers de surcharge d'agents.
Les fichiers opérationnels sont dans `/a0/usr/agents/{profil}/prompts/` (volume Docker persistant).

## Méthodologie
- Les surcharges incluent intégralement le contenu original shipped (`/a0/agents/{profil}/prompts/`)
- Seul du contenu additionnel est ajouté en fin de fichier (section `## Operational Context` ou `## Proactive reporting`)
- Langue : anglais uniquement, style minimaliste identique aux originaux
- Aucune modification du contenu original

## Profils
- `developer/` : Master Developer + Operational Context
- `researcher/` : Deep ReSearch + Operational Context
- `hacker/` : Cyber Security Expert (role + communication + environment)

## Déploiement
En cas de perte des fichiers dans `/a0/usr/agents/`, les restaurer depuis ce dossier :
```bash
cp .a0proj/knowledge/agents_overrides/developer/prompts/* /a0/usr/agents/developer/prompts/
cp .a0proj/knowledge/agents_overrides/researcher/prompts/* /a0/usr/agents/researcher/prompts/
cp .a0proj/knowledge/agents_overrides/hacker/prompts/* /a0/usr/agents/hacker/prompts/
```
