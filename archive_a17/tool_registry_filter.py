"""
ToolRegistry Filter - Monkey patches MCPConfig.get_tools_prompt() to filter tools using semantic search.
This reduces token usage by including only relevant tools in system prompts.
"""

import os
import json
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

# Try to import ToolRegistry
try:
    from extensions.tool_registry import ToolRegistry, get_tool_registry
    TOOL_REGISTRY_AVAILABLE = True
except ImportError:
    logger.warning("ToolRegistry not available, using all tools")
    TOOL_REGISTRY_AVAILABLE = False


def extract_user_query_from_context() -> str:
    """
    Extract user query from the current context for semantic filtering.
    This is a heuristic approach.
    """
    try:
        # Try to get from agent context
        from agent import AgentContext
        context = AgentContext.get_current()
        if context:
            # Get last user message from conversation history
            history = getattr(context, 'conversation_history', [])
            if history:
                for msg in reversed(history):
                    if isinstance(msg, dict) and msg.get('role') == 'user':
                        content = msg.get('content', '')
                        if isinstance(content, str):
                            # Extract first meaningful part
                            return content[:200].strip()
                        elif isinstance(content, list):
                            # Handle multimodal content
                            text_parts = [item.get('text', '') for item in content if isinstance(item, dict) and 'text' in item]
                            return ' '.join(text_parts)[:200].strip()
            
            # Try to get from active agent
            active_agent = getattr(context, 'active_agent', None)
            if active_agent:
                last_input = getattr(active_agent, 'last_user_input', '')
                if last_input:
                    return str(last_input)[:200].strip()
    except Exception as e:
        logger.debug(f"Failed to extract user query: {e}")
    
    return ""  # Empty query means use all tools


def filter_tools_with_registry(tools_list: List[Dict[str, Any]], query: str) -> List[Dict[str, Any]]:
    """
    Filter tools using ToolRegistry semantic search.
    Always includes essential tools.
    """
    if not TOOL_REGISTRY_AVAILABLE:
        logger.warning("ToolRegistry not available, returning all tools")
        return tools_list
    
    try:
        registry = get_tool_registry()
        
        # Load tools if not indexed
        tools_path = "/a0/usr/projects/agentzero_ameliorations/.a0proj/knowledge/tools_registry.json"
        if registry.get_tool_count() == 0 and os.path.exists(tools_path):
            try:
                with open(tools_path, 'r') as f:
                    tools_data = json.load(f)
                registry.index_tools(tools_data)
                logger.info(f"Indexed {len(tools_data)} tools for filtering")
            except Exception as e:
                logger.error(f"Failed to index tools: {e}")
                return tools_list
        
        # If no query or registry empty, return all tools
        if not query.strip() or registry.get_tool_count() == 0:
            return tools_list
        
        # Get semantically relevant tools
        relevant_tools = registry.search_tools(query, k=8)  # Top 8 most relevant
        
        # Convert to filtered list
        filtered_tools = []
        found_tool_names = set()
        
        # Add relevant tools
        for tool_data in relevant_tools:
            tool_name = tool_data.get('name', '')
            if tool_name:
                found_tool_names.add(tool_name)
                # Find original tool
                for original_tool in tools_list:
                    if original_tool.get('name') == tool_name:
                        filtered_tools.append(original_tool)
                        break
        
        # Always include essential tools
        essential_tool_names = [
            "response",
            "code_execution_tool", 
            "call_subordinate",
            "memory_load",
            "memory_save",
            "memory_delete",
            "memory_forget",
            "skills_tool",
            "search_engine",
            "document_query",
            "notify_user",
            "wait",
            "input",
            "behaviour_adjustment"
        ]
        
        for tool_name in essential_tool_names:
            if tool_name not in found_tool_names:
                for original_tool in tools_list:
                    if original_tool.get('name') == tool_name:
                        filtered_tools.append(original_tool)
                        found_tool_names.add(tool_name)
                        break
        
        # Ensure minimum number of tools
        if len(filtered_tools) < 5:
            # Add more tools from original list
            for original_tool in tools_list:
                if original_tool.get('name') not in found_tool_names:
                    filtered_tools.append(original_tool)
                    found_tool_names.add(original_tool.get('name'))
                    if len(filtered_tools) >= 12:  # Reasonable max
                        break
        
        logger.info(f"Filtered {len(tools_list)} tools down to {len(filtered_tools)} based on query: '{query[:50]}...'")
        return filtered_tools
        
    except Exception as e:
        logger.error(f"ToolRegistry filtering failed: {e}")
        return tools_list


def patch_mcp_tools_prompt():
    """
    Monkey patch MCPConfig.get_tools_prompt() to filter tools.
    This replaces the original method with our filtered version.
    """
    try:
        from python.helpers.mcp_handler import MCPConfig
        
        # Save original method
        original_get_tools_prompt = MCPConfig.get_tools_prompt
        
        # Define new method
        def patched_get_tools_prompt(self):
            """
            Get filtered MCP tools prompt.
            """
            # Call original to get all tools
            original_prompt = original_get_tools_prompt(self)
            
            # If prompt is empty or ToolRegistry not available, return original
            if not original_prompt or not TOOL_REGISTRY_AVAILABLE:
                return original_prompt
            
            # Extract user query for semantic filtering
            user_query = extract_user_query_from_context()
            
            # Parse tools from original prompt (simplified parsing)
            # In reality, we would need to parse the tools from the prompt
            # For now, we'll work with the assumption that ToolRegistry has indexed tools
            
            # Since we can't easily parse tools from prompt text,
            # we'll use ToolRegistry's indexed tools
            try:
                registry = get_tool_registry()
                tools_path = "/a0/usr/projects/agentzero_ameliorations/.a0proj/knowledge/tools_registry.json"
                
                if registry.get_tool_count() == 0 and os.path.exists(tools_path):
                    with open(tools_path, 'r') as f:
                        tools_data = json.load(f)
                    registry.index_tools(tools_data)
                
                # Get filtered tools
                relevant_tools = registry.search_tools(user_query, k=8)
                
                # If we found relevant tools, reconstruct prompt
                if relevant_tools:
                    # Essential tools to always include
                    essential_tool_names = [
                        "response", "code_execution_tool", "call_subordinate",
                        "memory_load", "memory_save", "skills_tool", "search_engine"
                    ]
                    
                    # Build new prompt
                    prompt_lines = ["## Remote (MCP Server) Agent Tools available:"]
                    
                    # Add essential tools first
                    for tool_name in essential_tool_names:
                        tool = registry.get_tool_by_name(tool_name)
                        if tool:
                            prompt_lines.append(f"### {tool_name}")
                            prompt_lines.append(tool.get('description', ''))
                            input_schema = tool.get('input_schema', {})
                            if input_schema:
                                prompt_lines.append(f"\n#### Input schema for tool_args:")
                                prompt_lines.append(json.dumps(input_schema, indent=2))
                            prompt_lines.append(f"\n#### Usage:")
                            prompt_lines.append(f"{{\n    \"thoughts\": [\"...\"],\n    \"tool_name\": \"{tool_name}\",\n    \"tool_args\": !follow schema above\n}}")
                            prompt_lines.append("")
                    
                    # Add relevant tools (excluding essentials already added)
                    for tool_data in relevant_tools:
                        tool_name = tool_data.get('name', '')
                        if tool_name not in essential_tool_names:
                            prompt_lines.append(f"### {tool_name}")
                            prompt_lines.append(tool_data.get('description', ''))
                            input_schema = tool_data.get('input_schema', {})
                            if input_schema:
                                prompt_lines.append(f"\n#### Input schema for tool_args:")
                                prompt_lines.append(json.dumps(input_schema, indent=2))
                            prompt_lines.append(f"\n#### Usage:")
                            prompt_lines.append(f"{{\n    \"thoughts\": [\"...\"],\n    \"tool_name\": \"{tool_name}\",\n    \"tool_args\": !follow schema above\n}}")
                            prompt_lines.append("")
                    
                    filtered_prompt = "\n\n".join(prompt_lines)
                    
                    # Calculate token savings
                    original_lines = original_prompt.count('\n')
                    filtered_lines = filtered_prompt.count('\n')
                    reduction_pct = int((1 - filtered_lines / max(original_lines, 1)) * 100)
                    
                    logger.info(f"Tool filtering applied: {len(relevant_tools)} relevant tools, {reduction_pct}% line reduction")
                    return filtered_prompt
                
            except Exception as e:
                logger.error(f"Tool filtering error: {e}")
                
            # Fallback to original prompt
            return original_prompt
        
        # Apply the patch
        MCPConfig.get_tools_prompt = patched_get_tools_prompt
        logger.info("Successfully patched MCPConfig.get_tools_prompt() with ToolRegistry filtering")
        
    except Exception as e:
        logger.error(f"Failed to patch MCPConfig.get_tools_prompt(): {e}")


# Auto-patch when module is imported
patch_mcp_tools_prompt()

