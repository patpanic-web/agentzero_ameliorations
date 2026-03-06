"""
ToolRegistry Prompt Override Extension

This extension filters MCP tools using semantic search before including them in system prompts.
It replaces the standard MCP tools prompt with a filtered version containing only relevant tools.
"""

import os
import json
from typing import Any, List, Dict
from python.helpers.extension import Extension
from python.helpers.mcp_handler import MCPConfig
from agent import Agent, LoopData
import logging

logger = logging.getLogger(__name__)


def get_tool_registry():
    """
    Import and return ToolRegistry instance.
    Uses lazy import to avoid dependency issues.
    """
    try:
        from extensions.tool_registry import ToolRegistry
        return ToolRegistry()
    except ImportError as e:
        logger.warning(f"Failed to import ToolRegistry: {e}")
        return None


def extract_user_query_from_context(context) -> str:
    """
    Extract user query from agent context for semantic filtering.
    This is a heuristic - we try to get the last user message.
    """
    try:
        # Try to get from conversation history
        if hasattr(context, 'conversation_history') and context.conversation_history:
            for message in reversed(context.conversation_history):
                if message.get('role') == 'user':
                    user_text = message.get('content', '')
                    # Clean up - take first 100 chars
                    return user_text[:200].strip()
        
        # Try to get from agent context
        if hasattr(context, 'last_user_message'):
            return context.last_user_message or ""
            
    except Exception as e:
        logger.debug(f"Failed to extract user query: {e}")
        
    return ""


def filter_mcp_tools_with_registry(tools_list: List[Dict], query: str) -> List[Dict]:
    """
    Filter MCP tools using ToolRegistry semantic search.
    Always includes essential tools and falls back to all tools if needed.
    """
    registry = get_tool_registry()
    if not registry:
        logger.warning("ToolRegistry not available, returning all tools")
        return tools_list
    
    # Load tools data if not already indexed
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
    
    try:
        # Get semantically relevant tools
        relevant_tools = registry.search_tools(query, k=8)  # Top 8 most relevant
        
        # Convert to list of tool dictionaries
        filtered_tools = []
        tool_names_found = set()
        
        for tool_data in relevant_tools:
            tool_name = tool_data.get('name', '')
            if tool_name:
                tool_names_found.add(tool_name)
                # Find the original tool from full list
                for original_tool in tools_list:
                    if original_tool.get('name') == tool_name:
                        filtered_tools.append(original_tool)
                        break
        
        # Always include essential tools
        essential_tool_names = ["response", "code_execution_tool", "call_subordinate", "memory_load", "memory_save"]
        for tool_name in essential_tool_names:
            if tool_name not in tool_names_found:
                # Find in original list
                for original_tool in tools_list:
                    if original_tool.get('name') == tool_name:
                        filtered_tools.append(original_tool)
                        tool_names_found.add(tool_name)
                        break
        
        # Ensure we have at least 5 tools
        if len(filtered_tools) < 5:
            # Add some more tools from original list
            for original_tool in tools_list:
                if original_tool.get('name') not in tool_names_found:
                    filtered_tools.append(original_tool)
                    tool_names_found.add(original_tool.get('name'))
                    if len(filtered_tools) >= 10:  # Reasonable max
                        break
        
        logger.info(f"Filtered {len(tools_list)} tools down to {len(filtered_tools)} based on query: '{query[:50]}...'")
        return filtered_tools
        
    except Exception as e:
        logger.error(f"ToolRegistry filtering failed: {e}")
        return tools_list


def generate_mcp_tools_prompt(tools_list: List[Dict]) -> str:
    """
    Generate MCP tools prompt from filtered tools list.
    Format matches the original but only includes filtered tools.
    """
    if not tools_list:
        return ""
    
    prompt_lines = ["## Remote (MCP Server) Agent Tools available:"]
    
    for tool in tools_list:
        name = tool.get('name', '')
        description = tool.get('description', '')
        
        if not name:
            continue
            
        prompt_lines.append(f"### {name}")
        if description:
            prompt_lines.append(f"{description}")
        
        # Add input schema if available
        input_schema = tool.get('input_schema', {})
        if input_schema:
            prompt_lines.append(f"\n#### Input schema for tool_args:")
            prompt_lines.append(f"{json.dumps(input_schema, indent=2)}")
        
        prompt_lines.append(f"\n#### Usage:")
        prompt_lines.append(f"{{\n    \"thoughts\": [\"...\"],\n    \"tool_name\": \"{name}\",\n    \"tool_args\": !follow schema above\n}}")
        prompt_lines.append("")
    
    return "\n\n".join(prompt_lines)


class ToolRegistryPromptOverride(Extension):
    """
    Extension that filters MCP tools using semantic search before including in system prompt.
    """
    
    async def execute(self, system_prompt: list[str] = [], loop_data: LoopData = LoopData(), **kwargs: Any):
        """
        Override MCP tools prompt generation with filtered version.
        """
        try:
            # Get the original MCP tools
            mcp_config = MCPConfig.get_instance()
            if not mcp_config.servers:
                return  # No MCP tools to filter
            
            # Extract user query for semantic filtering
            user_query = extract_user_query_from_context(self.agent.context)
            
            # Get all available MCP tools
            # We need to access the tools list - this might require patching
            # For now, we'll generate our own filtered version
            
            # Since we can't easily get the tools list from MCPConfig,
            # we'll load from our registry file
            tools_path = "/a0/usr/projects/agentzero_ameliorations/.a0proj/knowledge/tools_registry.json"
            if not os.path.exists(tools_path):
                logger.warning(f"Tools registry not found at {tools_path}")
                return
            
            with open(tools_path, 'r') as f:
                all_tools = json.load(f)
            
            # Filter tools based on user query
            filtered_tools = filter_mcp_tools_with_registry(all_tools, user_query)
            
            # Generate filtered prompt
            filtered_prompt = generate_mcp_tools_prompt(filtered_tools)
            
            if not filtered_prompt:
                return
            
            # Find and replace the MCP tools section in system_prompt
            for i, prompt in enumerate(system_prompt):
                if "## Remote (MCP Server) Agent Tools available:" in prompt:
                    system_prompt[i] = filtered_prompt
                    logger.info(f"Replaced MCP tools prompt with filtered version ({len(filtered_tools)} tools)")
                    break
            else:
                # MCP tools section not found, add it
                system_prompt.append(filtered_prompt)
                logger.info(f"Added filtered MCP tools prompt ({len(filtered_tools)} tools)")
                
        except Exception as e:
            logger.error(f"ToolRegistryPromptOverride failed: {e}")
            # Silently fail - don't break the system


# Alternative approach: Monkey-patch MCPConfig.get_tools_prompt
# This is more direct but riskier

def create_filtered_mcp_prompt() -> str:
    """
    Create a filtered MCP tools prompt.
    Can be used to replace the original get_tools_prompt method.
    """
    try:
        # Load tools
        tools_path = "/a0/usr/projects/agentzero_ameliorations/.a0proj/knowledge/tools_registry.json"
        if not os.path.exists(tools_path):
            return ""
        
        with open(tools_path, 'r') as f:
            all_tools = json.load(f)
        
        # For now, use first 10 tools as placeholder
        # In real implementation, extract user query from context
        filtered_tools = all_tools[:10]
        
        return generate_mcp_tools_prompt(filtered_tools)
        
    except Exception as e:
        logger.error(f"Failed to create filtered MCP prompt: {e}")
        return ""


# Monkey-patching approach (commented out for safety)
# def patch_mcp_tools_generation():
#     """
#     Monkey-patch MCPConfig.get_tools_prompt to return filtered tools.
#     Use with caution.
#     """
#     original_get_tools_prompt = MCPConfig.get_tools_prompt
#     
#     def patched_get_tools_prompt(self):
#         # Get original tools
#         original_prompt = original_get_tools_prompt()
#         
#         # If we can't filter, return original
#         if not hasattr(self, 'context') or not self.context:
#             return original_prompt
#         
#         # Extract user query
#         user_query = extract_user_query_from_context(self.context)
#         
#         # Generate filtered prompt
#         filtered_prompt = create_filtered_mcp_prompt()
#         
#         return filtered_prompt if filtered_prompt else original_prompt
#     
#     MCPConfig.get_tools_prompt = patched_get_tools_prompt
#     logger.info("Patched MCPConfig.get_tools_prompt with filtering")

