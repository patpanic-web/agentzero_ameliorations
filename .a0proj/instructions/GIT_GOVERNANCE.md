# Git Governance

## Commit Rules
- Commit at end of each deliverable (task completion, sprint close)
- Use Conventional Commits: `feat:`, `fix:`, `docs:`, `chore:`
- Keep messages short: `type: concise description`
- Always `git add -A` before commit to include all changes
- Push to origin after every commit
- Work on `main` branch only

## Workflow
1. Work on task → complete deliverable
2. `git add -A && git commit -m 'type: description'`
3. `git push origin main`
4. Never leave uncommitted work at end of session
