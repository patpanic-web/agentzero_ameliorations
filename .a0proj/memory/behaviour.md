## Pre-Flight Checklist — Mandatory Before Response
> Execute before every final response

### D1. Delegation Check
- Task eligible for subordinate? → MUST delegate
- Standard execution (code, tests, audit, research) → call_subordinate
- Iterating on subordinate result → call_subordinate reset=false
- Simple task requiring direct supervision → execute directly

### D2. Memory Check  
- Reusable solution discovered? → MUST memory_save
- Lesson learned / error avoided? → MUST memory_save
- Context for future sessions? → MUST memory_save
- Nothing new → proceed

### D3. Include Optimization
- Long subordinate result? → §§include(path)
- File content already available? → §§include(path)
- Rewrite necessary → proceed

## Task Creation — Anti-Duplication Protocol
> Before creating ANY scheduled/planned/adhoc task

1. List existing: scheduler:list_tasks with relevant filters
2. Check similarity: name, objective, frequency >70% = DUPLICATE
3. If duplicate: propose merge, do NOT create, document decision
4. If unique: create with dedicated_context=true, log ID

### Weekly Maintenance
Every Monday, list all scheduled tasks and verify:
- Undetected redundancies
- Obsolete tasks to delete
- Schedule overlaps
