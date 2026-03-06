# Session Analysis Report


**Generated:** 2026-03-06 02:23:09
**Scan window:** Last 7 days


## 📊 Summary Statistics


- **Files scanned:** 461
- **Total tool calls:** 127
- **Subordinate delegations:** 13
- **Response calls:** 22
- **Delegation rate:** 10.2%


## ⚠️ Error Patterns Found


### Retry Loop (39 occurrences)


**Example 1** (from `76.txt`):


```
  fw.msg_misformat.md: ~ tokens
bash: bc: command not found
  fw.msg_nudge.md: ~ tokens
bash: bc: command not found
  fw.msg_repeat.md: ~ tokens
```


**Example 2** (from `76.txt`):


```
  fw.msg_nudge.md: ~ tokens
bash: bc: command not found
  fw.msg_repeat.md: ~ tokens
bash: bc: command not found
  fw.msg_summary.md: ~ tokens
```


**Example 3** (from `14.txt`):


```
File: /a0/prompts/memory.memories_filter.msg.md
---
File: /a0/prompts/fw.msg_nudge.md
---
File: /a0/prompts/fw.code.max_time.md
```


**Example 4** (from `14.txt`):


```
File: /a0/prompts/fw.tool_not_found.md
---
File: /a0/prompts/fw.msg_repeat.md
---
File: /a0/prompts/agent.system.tool.input.md
```


**Example 5** (from `24.txt`):


```
Only in /a0/prompts/: fw.msg_from_subordinate.md
Only in /a0/prompts/: fw.msg_misformat.md
Only in /a0/prompts/: fw.msg_nudge.md
Only in /a0/prompts/: fw.msg_repeat.md
Only in /a0/prompts/: fw.msg_summary.md
```


### File Error (29 occurrences)


**Example 1** (from `10.txt`):


```

    if merged is None:
        raise FileNotFoundError(
            f"Agent '{name}' not found in default or custom directories"
        )
```


**Example 2** (from `23.txt`):


```
/a0/usr/skills/project-governance/templates/niv2/knowledge/bmad/solutioning/README.md
(venv) §§secret(VPS_HOSTINGER_USER)@db9996741d2c:/# (venv) §§secret(VPS_HOSTINGER_USER)@db9996741d2c:/# (venv) §§secret(VPS_HOSTINGER_USER)@db9996741d2c:/# -rwxr-xr-x 1 §§secret(VPS_HOSTINGER_USER) §§secret(VPS_HOSTINGER_USER) 1987 Mar  5 18:36 /a0/usr/skills/project-governance/scripts/init-governance.sh
(venv) §§secret(VPS_HOSTINGER_USER)@db9996741d2c:/# (venv) §§secret(VPS_HOSTINGER_USER)@db9996741d2c:/# (ven
```


**Example 3** (from `17.txt`):


```
(venv) §§secret(VPS_HOSTINGER_USER)@db9996741d2c:/# (venv) §§secret(VPS_HOSTINGER_USER)@db9996741d2c:/# (venv) §§secret(VPS_HOSTINGER_USER)@db9996741d2c:/# > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > bash: /a0/usr/skills/project-governance/scripts/init-governance.sh: No such file or directory
(venv) §§secret(VPS_HOSTINGER_USER)@db9996741d2c:/# (venv) §§secret(VPS_HOSTINGER_USER)@db9996741d2c:/# (venv) §§secret(VPS_HOSTINGER_USER)@db99
```


**Example 4** (from `17.txt`):


```
(venv) §§secret(VPS_HOSTINGER_USER)@db9996741d2c:/# (venv) §§secret(VPS_HOSTINGER_USER)@db9996741d2c:/# (venv) §§secret(VPS_HOSTINGER_USER)@db9996741d2c:/# > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > bash: /a0/usr/skills/project-governance/scripts/init-governance.sh: No such file or directory
(venv) §§secret(VPS_HOSTINGER_USER)@db9996741d2c:/# (venv) §§secret(VPS_HOSTINGER_USER)@db9996741d2c:/# (venv) §§secret(VPS_HOSTINGER_USER)@db99
```


**Example 5** (from `18.txt`):


```
(venv) §§secret(VPS_HOSTINGER_USER)@db9996741d2c:/# ls: cannot access '/a0/usr/skills/project-governance/scripts/': No such file or directory
(venv) §§secret(VPS_HOSTINGER_USER)@db9996741d2c:/# (venv) §§secret(VPS_HOSTINGER_USER)@db9996741d2c:/# (venv) §§secret(VPS_HOSTINGER_USER)@db9996741d2c:/# > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > bash: /a0/usr/skills/project-governance/scripts/init-governance.sh: No such file or directory
(v
```


### Tool Not Found (23 occurrences)


**Example 1** (from `76.txt`):


```
  fw.rename_chat.sys.md: ~ tokens
bash: bc: command not found
  fw.tool_not_found.md: ~ tokens
bash: bc: command not found
  fw.tool_result.md: ~ tokens
```


**Example 2** (from `14.txt`):


```
File: /a0/prompts/agent.system.behaviour_default.md
---
File: /a0/prompts/fw.tool_not_found.md
---
File: /a0/prompts/fw.msg_repeat.md
```


**Example 3** (from `24.txt`):


```
Only in /a0/prompts/: fw.rename_chat.msg.md
Only in /a0/prompts/: fw.rename_chat.sys.md
Only in /a0/prompts/: fw.tool_not_found.md
Only in /a0/prompts/: fw.tool_result.md
Only in /a0/prompts/: fw.topic_summary.msg.md
```


**Example 4** (from `27.txt`):


```
    *        fw.rename_chat.msg.md  
    *        fw.rename_chat.sys.md  
    *        fw.tool_not_found.md  
    *        fw.tool_result.md  
    *        fw.topic_summary.msg.md  
```


**Example 5** (from `27.txt`):


```
    *        fw.rename_chat.msg.md  
    *        fw.rename_chat.sys.md  
    *        fw.tool_not_found.md  
    *        fw.tool_result.md  
    *        fw.topic_summary.msg.md  
```


### Json Error (21 occurrences)


**Example 1** (from `76.txt`):


```
  fw.msg_from_subordinate.md: ~ tokens
bash: bc: command not found
  fw.msg_misformat.md: ~ tokens
bash: bc: command not found
  fw.msg_nudge.md: ~ tokens
```


**Example 2** (from `14.txt`):


```
File: /a0/prompts/agent.system.projects.inactive.md
---
File: /a0/prompts/fw.msg_misformat.md
---
File: /a0/prompts/fw.topic_summary.sys.md
```


**Example 3** (from `24.txt`):


```
Only in /a0/prompts/: fw.msg_critical_error.md
Only in /a0/prompts/: fw.msg_from_subordinate.md
Only in /a0/prompts/: fw.msg_misformat.md
Only in /a0/prompts/: fw.msg_nudge.md
Only in /a0/prompts/: fw.msg_repeat.md
```


**Example 4** (from `27.txt`):


```
    *        fw.msg_critical_error.md  
    *        fw.msg_from_subordinate.md  
    *        fw.msg_misformat.md  
    *        fw.msg_nudge.md  
    *        fw.msg_repeat.md  
```


**Example 5** (from `27.txt`):


```
    *        fw.msg_critical_error.md  
    *        fw.msg_from_subordinate.md  
    *        fw.msg_misformat.md  
    *        fw.msg_nudge.md  
    *        fw.msg_repeat.md  
```


### Code Error (18 occurrences)


**Example 1** (from `12.txt`):


```
We suggest implementing some combination of pagination, range selection, filtering, and/or truncation with sensible default parameter values for any tool responses that could use up lots of context. For Claude Code, we restrict tool responses to 25,000 tokens by default. We expect the effective context length of agents to grow over time, but the need for context-efficient tools to remain.

If you choose to truncate responses, be sure to steer agents with helpful instructions. You can directly en
```


**Example 2** (from `12.txt`):


```
```
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[1], line 141
    129 full_html = f'''<!DOCTYPE html>
```


**Example 3** (from `27.txt`):


```
  pdf.add_font('DejaVu', '', '/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed.ttf', uni=True)
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
Cell In[1], line 93
     90 pdf = PDF()
```


**Example 4** (from `35.txt`):


```
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[1], line 2
      1 # Continue PDF with Scenario C section
```


**Example 5** (from `35.txt`):


```
      5 pdf.body_text("Le scénario C reste la stratégie optimale avec 0€ de fiscalité totale, mais la mécanique diffère du fait du régime de communauté légale.")

NameError: name 'pdf' is not defined
(venv) root@5f82584bc268:/a0/usr/workdir#
```


### Timeout (17 occurrences)


**Example 1** (from `76.txt`):


```
  fw.msg_summary.md: ~ tokens
bash: bc: command not found
  fw.msg_timeout.md: ~ tokens
bash: bc: command not found
  fw.msg_truncated.md: ~ tokens
```


**Example 2** (from `14.txt`):


```
File: /a0/prompts/memory.memories_query.msg.md
---
File: /a0/prompts/fw.msg_timeout.md
---
File: /a0/prompts/agent.extras.agent_info.md
```


**Example 3** (from `24.txt`):


```
Only in /a0/prompts/: fw.msg_repeat.md
Only in /a0/prompts/: fw.msg_summary.md
Only in /a0/prompts/: fw.msg_timeout.md
Only in /a0/prompts/: fw.msg_truncated.md
Only in /a0/prompts/: fw.notify_user.notification_sent.md
```


**Example 4** (from `27.txt`):


```
    *        fw.msg_repeat.md  
    *        fw.msg_summary.md  
    *        fw.msg_timeout.md  
    *        fw.msg_truncated.md  
    *        fw.notify_user.notification_sent.md  
```


**Example 5** (from `27.txt`):


```
    *        fw.msg_repeat.md  
    *        fw.msg_summary.md  
    *        fw.msg_timeout.md  
    *        fw.msg_truncated.md  
    *        fw.notify_user.notification_sent.md  
```


## 📈 Delegation Analysis


- **Delegation rate:** 10.2% of tool calls are to subordinates
- **Response rate:** 17.3% of tool calls are responses


**Interpretation:**

- Delegation rate appears balanced


## 💡 Improvement Proposals


### AUDIT-001: Improve JSON response validation


Found 21 JSON formatting errors. Consider adding pre-flight JSON validation before sending responses.


### AUDIT-002: Tool registry awareness enhancement


Found 23 unknown tool errors. Agents should have better awareness of available tools.


### AUDIT-003: Reduce message repetition loops


Found 39 retry/loop patterns. Implement smarter retry logic with exponential backoff.


### AUDIT-004: Optimize timeout handling


Found 17 timeout errors. Adjust timeout values or implement async timeouts.
