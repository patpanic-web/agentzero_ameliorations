# 🔍 Analysis — A24 : Prénoms formels personas BMAD

> Date : 2026-03-06 | Analyst : Business Analyst BMAD | Statut : ✅ ANALYSE COMPLÈTE

---

## 📌 Contexte & Besoin

**Constat** : Gap d'implémentation identifié lors de la reprise de session 8.
- Le PO s'attendait à voir des prénoms comme "Mary" dans les conversations
- `BMAD_PERSONAS.md` définit uniquement des rôles avec emojis : `🔍 Business Analyst`
- "Mary" a été utilisé ad-hoc dans SYNTHESE_ANALYSE_COMPLETE et TACHE_CHROME_BROWSER mais jamais formalisé

---

## 🎯 Critères de Succès

- [ ] Chaque persona BMAD a un prénom formel dans `BMAD_PERSONAS.md`
- [ ] Le prénom apparaît dans les réponses (ex: `🔍 Mary | Business Analyst |`)
- [ ] Le template project-governance Level 2 est synchronisé
- [ ] Le PO voit les prénoms dans toutes les futures conversations

---

## 💡 Prénoms Proposés

| Persona | Emoji | Prénom suggéré | Phase |
|---------|-------|----------------|-------|
| Business Analyst | 🔍 | Mary | Analysis |
| Product Manager | 📋 | Sarah | Planning |
| Solution Architect | 🏗️ | Alex | Solutioning |
| Developer | 👨‍💻 | James | Implementation |
| QA Engineer | 🧪 | Quinn | Validation |
| Scrum Master | 🔄 | Sam | Facilitation |

---

## 🔧 Fichiers à Modifier

1. `/a0/usr/projects/agentzero_ameliorations/.a0proj/instructions/BMAD_PERSONAS.md`
2. `/a0/usr/skills/project-governance/templates/niv2/instructions/BMAD_PERSONAS.md`

**Effort estimé** : 15 minutes

---

## ❓ Questions pour le PO

1. Les prénoms suggérés (Mary, Sarah, Alex, James, Quinn, Sam) vous conviennent-ils ?
2. Prénoms français ou universels ?
3. Format : `🔍 Mary | Business Analyst |` ou `🔍 Business Analyst (Mary) |` ?
