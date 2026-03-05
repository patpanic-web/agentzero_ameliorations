# Analyse d'Audit de Sécurité du Container

## Sujet Central
Évaluation de la posture de sécurité de l'environnement d'exécution Agent-Zero.

## Objectifs (Mary 📊)
- Identifier les services réseau à l'écoute sur localhost.
- Analyser la hiérarchie des utilisateurs et les capacités (SUDO).
- Détecter des configurations risquées ou des points de durcissement.

## Contraintes
- Strictement local.
- Pas de modification système intrusive.

## Plan Technique (John 📋)
1. Énumération réseau (ports/services).
2. Énumération système (users/privs).
3. Audit des fichiers sensibles.
4. Synthèse des findings.
