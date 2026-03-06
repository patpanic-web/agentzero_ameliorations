#!/usr/bin/env python3
"""
MCP Monitor — Vérifie si le nombre d'outils MCP actifs justifie le lancement de A17.
Seuil de déclenchement A17 : > 15 outils MCP actifs.

Usage: python3 check_mcp_count.py
"""

import json
import sys

SETTINGS_PATH = '/a0/usr/settings.json'
A17_THRESHOLD = 15  # Seuil outils MCP pour déclencher A17

# Estimation tokens par outil MCP (description + schema + exemple)
TOKENS_PER_TOOL = 250

def count_tools_for_mcp(mcp_name: str) -> int:
    """Estimation du nombre d'outils par MCP connu."""
    known_tool_counts = {
        'tavily': 5,
        'playwright': 22,
        'system-diag': 27,
        'git': 12,
        'docker-mcp': 8,
    }
    return known_tool_counts.get(mcp_name, 10)  # 10 par défaut si inconnu

def main():
    with open(SETTINGS_PATH, 'r') as f:
        settings = json.load(f)

    mcp_raw = settings.get('mcp_servers', '{}')
    if isinstance(mcp_raw, str):
        mcp_data = json.loads(mcp_raw)
    else:
        mcp_data = mcp_raw

    servers = mcp_data.get('mcpServers', {})

    print('=' * 55)
    print('📊 MCP MONITOR — Audit des MCPs actifs')
    print('=' * 55)

    active_mcps = []
    total_tools = 0

    for name, config in servers.items():
        disabled = config.get('disabled', False)
        if not disabled:
            tool_count = count_tools_for_mcp(name)
            tokens = tool_count * TOKENS_PER_TOOL
            active_mcps.append((name, tool_count, tokens))
            total_tools += tool_count
            status = '✅'
        else:
            status = '❌ (disabled)'
        desc = config.get('description', '')
        print(f'  {status} {name:<15} {"→ " + desc if desc else ""}')

    total_tokens = total_tools * TOKENS_PER_TOOL

    print()
    print(f'  Outils actifs estimés : {total_tools}')
    print(f'  Tokens estimés        : ~{total_tokens:,}')
    print(f'  Seuil déclenchement A17 : > {A17_THRESHOLD} outils')
    print()

    if total_tools > A17_THRESHOLD:
        print(f'🔴 SEUIL ATTEINT ! A17 (ToolRegistry Filter) doit être lancé.')
        print(f'   {total_tools} outils > {A17_THRESHOLD} — Le filtrage sémantique est justifié.')
        sys.exit(1)  # Exit code 1 = action requise
    else:
        remaining = A17_THRESHOLD - total_tools
        print(f'✅ Seuil non atteint. A17 non nécessaire pour l\'instant.')
        print(f'   Marge : {remaining} outils avant déclenchement.')
        sys.exit(0)  # Exit code 0 = OK

if __name__ == '__main__':
    main()
