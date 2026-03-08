# 🔍 Audit MCP-QNAP — Corrélation avec crashes OpenRouter

**Date**: 2026-03-08
**Statut**: Investigation complète
**Responsable**: Agent Zero
**Classification**: P1 — Instabilité potentielle

---

## 🚨 Problème Signalé

**Symptôme**: L'utilisateur suspecte que le MCP QNAP cause des crashes/freeze d'Agent Zero.
**Erreur observée**: `OpenRouterException - {"error":{"message":"No cookie auth credentials found","code":401}}`

---

## 🔬 Diagnostic Technique

### 1. Analyse de l'erreur OpenRouter

**Conclusion**: L'erreur "No cookie auth credentials found" est un **incident de service côté OpenRouter**, indépendant du MCP QNAP.

**Preuves**:
- Multiple rapports sur Reddit r/openrouter (post récent ~48h)
- Issues GitHub: continuedev/continue#10153, opencode#12436, dyad-sh/dyad#1686
- Erreur se produit avec différents clients (Continue, Opencode, Dyad, Agent0)
- Statut HTTP 401 indique problème d'authentification côté serveur OpenRouter

**Impact**: Incident temporaire OpenRouter, pas une régression A0.

### 2. Analyse MCP QNAP

**Configuration actuelle**:
```json
{
  "mcp_client_init_timeout": 10,
  "mcp_client_tool_timeout": 120,
  "mcpServers": {
    "qnap": {
      "command": "/a0/usr/mcp/qnap/qmcp",
      "args": ["--confighome", "/a0/usr/mcp/qnap"]
    }
  }
}
```

**Tests effectués**:

| Test | Résultat | Temps | Commentaire |
|------|----------|-------|-------------|
| Initialize MCP | 🟢 OK | ~1-2s | Logs qmcpagent.log confirment |
| Appel outil manuel | 🔴 Timeout | >15s | `timeout 15` échoué |
| Démarrage MCP | 🟢 OK | 1-2s | Via logs |

**Problèmes identifiés**:

| Problème | Sévérité | Impact |
|----------|----------|--------|
| Latence appels outils | 🔴 Haute | >15s pour certains appels |
| Timeout config court | ⚠️ Moyenne | 10s init peut être insuffisant avec réseau lent |
| mcp_server_enabled=false | ℹ️ Info | MCP chargé malgré flag désactivé? |

### 3. Analyse de corrélation

**Hypothèse**: Si MCP QNAP freeze (>15s) pendant un appel d'outil:
1. Bloque le thread d'exécution A0
2. Timeout en chaîne ou état inconsistant
3. Contexte LLM corrompu ou retry agressif
4. Erreurs indirectes (comme OpenRouter) apparaissent

**Preuve partielle**: Les logs montrent des restarts fréquents du MCP QNAP (plusieurs fois par heure), indiquant des problèmes de stabilité.

---

## ✅ Solutions Identifiées

### Solution 1: Désactiver temporairement MCP QNAP (T0)

**Action**: Ajouter `"disabled": true` au MCP QNAP
**Quand**: Si freeze/crash récurrent lié à QNAP confirmé
**Réversibilité**: Immédiate

```bash
python3 << 'PYEOF'
import json
with open('/a0/usr/settings.json', 'r') as f:
    d = json.load(f)
mcp = json.loads(d['mcp_servers'])
mcp['mcpServers']['qnap']['disabled'] = True
d['mcp_servers'] = json.dumps(mcp, indent=2)
with open('/a0/usr/settings.json', 'w') as f:
    json.dump(d, f, indent=2)
print("MCP QNAP désactivé")
PYEOF
```

### Solution 2: Augmenter les timeouts MCP (T1)

**Action**: Passer `mcp_client_init_timeout` à 30s et `mcp_client_tool_timeout` à 180s
**Bénéfice**: Réduire les faux timeouts réseau
**Risque**: Freeze plus longs si vrai problème

### Solution 3: Investigation réseau approfondie (T2)

**Actions**:
1. Tester connectivité Tailscale NAS (ping, curl)
2. Analyser latence des appels API QNAP
3. Vérifier certificats client (expiration, validité)
4. Comparer perfs avec/without Tailscale

**Complexité**: 2-4h

### Solution 4: Wrapper MCP avec timeout/circuit-breaker (T3)

**Concept**: Wrapper Python qui encapsule MCP QNAP avec:
- Timeout strict par appel
- Circuit-breaker après N échecs
- Fallback message explicite

**Complexité**: 4h
**No-Core-Change**: ✅

---

## 📊 Comparaison Solutions

| Solution | Rapidité | Efficacité | Réversibilité | Coût | Priorité |
|----------|----------|------------|---------------|------|----------|
| Désactiver QNAP | ⚡ Immédiate | 🔴 Élevée | ⚡ Immédiate | 0 | P1 |
| Augmenter timeouts | ⚡ Immédiate | ⚠️ Moyenne | ⚡ Immédiate | 0 | P2 |
| Investigation réseau | 🕐 2-4h | 🟢 Haute | N/A | Moyen | P3 |
| Wrapper circuit-breaker | 🕐 4h | 🟢 Haute | ✅ Facile | Élevé | P4 |

---

## 🎯 Recommandation PO

**Proposition**: 
1. **Court terme** (immédiat): Surveiller si l'erreur OpenRouter persiste — si oui, confirmer incident service
2. **Moyen terme** (si freeze QNAP confirmé): Désactiver MCP QNAP temporairement
3. **Long terme** (si besoin QNAP): Implémenter Solution 4 (wrapper circuit-breaker)

**Facteurs de décision**:
- Fréquence des erreurs OpenRouter (incident temporaire vs permanent)
- Confirmation de freeze spécifiquement lors des appels QNAP
- Nécessité business d'accès NAS via A0

---

## 📝 Actions Backlog

| ID | Action | Condition | Priorité | Statut |
|----|--------|-----------|----------|--------|
| MCP-QNAP-CRASH-1 | Désactiver MCP QNAP | Si freeze confirmé lié QNAP | P1 | 📋 À faire |
| MCP-QNAP-CRASH-2 | Augmenter timeouts MCP | Si tests montrent besoin | P2 | 📋 À faire |
| MCP-QNAP-CRASH-3 | Investigation réseau complète | Si besoin persistant QNAP | P3 | 📋 À faire |
| MCP-QNAP-CRASH-4 | Implémenter wrapper circuit-breaker | Si P3 confirme instabilité | P4 | 📋 À faire |

---

## 📁 Références

- **Audit Tavily**: `AUDIT_MCP_TAVILY_FREEZE_2026-03-08.md` (pattern similaire)
- **Config A0**: `/a0/usr/settings.json`
- **Logs QNAP**: `/a0/usr/mcp/qnap/qmcpagent.log`
- **Reddit OpenRouter**: r/openrouter/comments/1oqiaol/
- **Issue Continue**: github.com/continuedev/continue/issues/10153

---

## 🏷️ Tags

`mcp`, `qnap`, `openrouter`, `crash`, `timeout`, `investigation`, `network`, `tailscale`

---

*Document créé par Agent Zero le 2026-03-08*
*Mise à jour: Sur décision PO ou nouvelle occurrence*
