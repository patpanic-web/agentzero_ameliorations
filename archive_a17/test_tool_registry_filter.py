"""
Test script for ToolRegistry filter extension.
Verifies that the monkey-patching works and measures token savings.
"""

import sys
import os
sys.path.insert(0, '/a0/usr/extensions')

# Test if the extension loads without errors
try:
    print("=== Test 1: Importing extension ===")
    import tool_registry_filter
    print("✅ tool_registry_filter imported successfully")
    
    # Test ToolRegistry availability
    print("\n=== Test 2: ToolRegistry availability ===")
    try:
        from extensions.tool_registry import ToolRegistry
        print("✅ ToolRegistry is available")
        
        # Test if tools are indexed
        registry = ToolRegistry()
        tool_count = registry.get_tool_count()
        print(f"✅ ToolRegistry has {tool_count} tools indexed")
        
        # Test a search
        test_query = "web search"
        results = registry.search_tools(test_query, k=3)
        print(f"✅ Search for '{test_query}' returned {len(results)} results")
        for i, tool in enumerate(results):
            print(f"   {i+1}. {tool.get('name')} (score: {tool.get('similarity_score', 0):.3f})")
            
    except ImportError as e:
        print(f"⚠️ ToolRegistry not available: {e}")
    
    # Test MCPConfig patching
    print("\n=== Test 3: MCPConfig patching ===")
    try:
        from python.helpers.mcp_handler import MCPConfig
        
        # Check if patched
        config = MCPConfig.get_instance()
        print(f"✅ MCPConfig.get_instance() works")
        
        # Try to get tools prompt
        print("\n=== Test 4: Getting tools prompt ===")
        try:
            prompt = config.get_tools_prompt()
            if prompt:
                lines = prompt.count('\n')
                chars = len(prompt)
                print(f"✅ Got tools prompt: {lines} lines, {chars} characters")
                
                # Count tools in prompt
                tool_sections = prompt.count('### ')
                print(f"✅ Found approximately {tool_sections} tool sections in prompt")
                
                # Estimate tokens (rough: ~4 chars per token)
                estimated_tokens = chars // 4
                print(f"✅ Estimated tokens: {estimated_tokens} (approx 4 chars per token)")
                
                # Check if filtering likely applied
                if tool_sections < 20:  # If less than 20 tools, filtering likely applied
                    print(f"✅ Filtering appears to be working (only {tool_sections} tools)")
                else:
                    print(f"⚠️ Many tools ({tool_sections}) - filtering might not be applied")
                
                # Show first few lines
                first_lines = prompt.split('\n')[:10]
                print(f"\nFirst 10 lines of prompt:")
                for line in first_lines:
                    print(f"  {line}")
            else:
                print("⚠️ Empty tools prompt returned")
                
        except Exception as e:
            print(f"❌ Error getting tools prompt: {e}")
            
    except Exception as e:
        print(f"❌ MCPConfig test failed: {e}")
    
    print("\n=== Test 5: Query extraction ===")
    try:
        # Test query extraction
        query = tool_registry_filter.extract_user_query_from_context()
        print(f"✅ Query extraction: '{query}'")
    except Exception as e:
        print(f"⚠️ Query extraction failed: {e}")
    
    print("\n=== All tests completed ===")
    print("\nNext steps:")
    print("1. Restart Agent-Zero to activate the patch")
    print("2. Test with actual agent conversations")
    print("3. Monitor token usage in logs")
    
except Exception as e:
    print(f"❌ Test failed: {e}")
    import traceback
    traceback.print_exc()

