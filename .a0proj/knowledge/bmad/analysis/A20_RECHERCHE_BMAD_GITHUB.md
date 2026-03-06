# Rapport sur la méthode BMAD (Breakthrough Method of Agile AI Driven Development)

## 1. GitHub Officiel bmad-code/bmad-method
- **Repo**: [BMAD-METHOD GitHub Repository](https://github.com/bmad-code-org/BMAD-METHOD)
- **Dernière version**: V6 Stable Release - Fin de la phase bêta.
- **Structure**: Cette version met l'accent sur la modularité par phase, permettant une gestion améliorée des workflows.
- **Documentation Lue**: README, CHANGELOG, et structure des fichiers analysés.
- **Sous-agents et sous-skills**: Des agents spécialisés par phase existent, facilitant l'intégration et l'utilisation.
- **Comparaison avec les versions précédentes**: Des changements significatifs ont été apportés dans la v6, avec de meilleures pratiques et fonctionnalités.

## 2. Retours utilisateurs
- **Discussion sur Beads**: [Long term memory backend discussion](https://github.com/bmad-code-org/BMAD-METHOD/discussions/1148) décrit comment Beads pourrait servir de couche de mémoire à long terme, réduisant les erreurs répétées dans les décisions par sprint.
- **OpenCode Integration**: [Issue #285](https://github.com/bmad-code-org/BMAD-METHOD/issues/285) montre des préoccupations sur l'intégration d'OpenCode et des bugs identifiés lors de la mise à niveau.
- **Autres retours**: Les problèmes d'intégration mentionnent souvent des améliorations de la structure de dossiers et des agents, signalant une tendance vers une meilleure modularisation.

## 3. Questions clés
1. **Lazy loading**: Oui, la v6 supporte nativement un lazy loading par phase.
2. **Taille d'un skill**: Typiquement, un skill complet peut être plus volumineux que les phases individuelles, en raison de la surcharge de fonctionnalités intégrées.
3. **Modularisation**: Les utilisateurs avancés tendent à modulariser BMAD pour une meilleure gestion de leurs projets.
4. **Anti-patterns**: Des anti-patterns connus incluent une mauvaise gestion des chemins dans les mises à niveau.
5. **Mention d'Agent Zero**: Agent Zero est souvent cité pour son intégration avec BMAD et des discussions sur l'optimisation des performances.

## Conclusion
La modularisation de BMAD vaut la peine d’être explorée, étant donné ses avantages en termes de gestion des workflows et de réduction des erreurs. Cependant, les utilisateurs doivent être vigilants par rapport aux changements de structure et aux problèmes d'intégration. 