#!/usr/bin/env python3
"""
Test script for ToolRegistry module.

Tests semantic search functionality and demonstrates token savings.
"""

import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tool_registry import ToolRegistry


def test_tool_registry():
    """Run comprehensive tests for ToolRegistry."""
    print("=== ToolRegistry Test Suite ===\n")
    
    # Load tools data
    tools_path = "/a0/usr/projects/agentzero_ameliorations/.a0proj/knowledge/tools_registry.json"
    if not os.path.exists(tools_path):
        print(f"Error: Tools file not found at {tools_path}")
        return False
    
    with open(tools_path, 'r') as f:
        tools_data = json.load(f)
    
    print(f"Loaded {len(tools_data)} tools from registry")
    
    # Create registry
    registry = ToolRegistry()
    
    # Test 1: Index tools
    print("\n1. Indexing tools...")
    registry.index_tools(tools_data)
    
    if registry.get_tool_count() != len(tools_data):
        print(f"Error: Expected {len(tools_data)} tools, got {registry.get_tool_count()}")
        return False
    print(f"✓ Indexed {registry.get_tool_count()} tools")
    
    # Test 2: Get tool by name
    print("\n2. Testing get_tool_by_name()...")
    test_tools = ["tavily_search", "git_commit", "browser_click", "check_memory"]
    
    for tool_name in test_tools:
        tool = registry.get_tool_by_name(tool_name)
        if tool:
            print(f"  ✓ Found '{tool_name}': {tool['description'][:50]}...")
        else:
            print(f"  ✗ Tool '{tool_name}' not found")
            return False
    
    # Test 3: Semantic search
    print("\n3. Testing semantic search...")
    test_queries = [
        ("web search engine", ["tavily_search", "tavily_crawl"]),
        ("git repository commit", ["git_commit", "git_status"]),
        ("browser click element", ["browser_click", "browser_navigate"]),
        ("system memory usage", ["check_memory", "list_processes"]),
    ]
    
    all_passed = True
    for query, expected_tools in test_queries:
        results = registry.search_tools(query, k=3)
        print(f"\n  Query: '{query}'")
        
        # Check if expected tools are in results
        found_tools = [r['name'] for r in results]
        for expected in expected_tools:
            if expected in found_tools:
                print(f"    ✓ '{expected}' found in results")
            else:
                print(f"    ✗ '{expected}' NOT found in results")
                all_passed = False
        
        # Show top result
        if results:
            top_tool = results[0]
            print(f"    Top result: {top_tool['name']} (score: {top_tool['similarity_score']:.3f})")
    
    if not all_passed:
        return False
    
    # Test 4: Token savings calculation
    print("\n4. Calculating token savings...")
    
    # Calculate token counts (approximate)
    all_tools_text = ""
    for tool in tools_data:
        all_tools_text += f"{tool.get('name', '')}: {tool.get('description', '')}\n"
        all_tools_text += f"  Parameters: {', '.join(tool.get('parameters', []))}\n\n"
    
    # Approximate token count (rough estimate: 4 characters per token)
    baseline_tokens = len(all_tools_text) // 4
    
    # With ToolRegistry (top 5 tools)
    sample_query = "search for web information"
    top_tools = registry.search_tools(sample_query, k=5)
    
    registry_text = ""
    for tool in top_tools:
        registry_text += f"{tool.get('name', '')}: {tool.get('description', '')[:100]}...\n"
    
    registry_tokens = len(registry_text) // 4
    
    print(f"  Baseline (all tools): ~{baseline_tokens} tokens")
    print(f"  With ToolRegistry (top 5): ~{registry_tokens} tokens")
    
    savings = ((baseline_tokens - registry_tokens) / baseline_tokens) * 100
    print(f"  Token savings: {savings:.1f}%")
    
    if savings < 50:
        print("  ⚠ Warning: Savings less than expected 85%")
    else:
        print("  ✓ Significant token savings achieved")
    
    # Test 5: Verify index persistence
    print("\n5. Testing index persistence...")
    
    # Create new registry instance (should load from disk)
    registry2 = ToolRegistry()
    
    if registry2.get_tool_count() != registry.get_tool_count():
        print(f"  ✗ Index not persisted: {registry2.get_tool_count()} vs {registry.get_tool_count()} tools")
        return False
    
    # Verify search works
    results2 = registry2.search_tools("web search", k=2)
    if not results2:
        print("  ✗ Search not working in new instance")
        return False
    
    print(f"  ✓ Index persisted with {registry2.get_tool_count()} tools")
    print(f"  ✓ Search works in new instance (found {len(results2)} results)")
    
    print("\n=== All tests passed! ===")
    return True


def benchmark_search():
    """Benchmark search performance."""
    print("\n=== Benchmarking search performance ===")
    
    registry = ToolRegistry()
    
    import time
    queries = [
        "web search",
        "git operations",
        "browser automation",
        "system monitoring",
        "file management",
    ]
    
    total_time = 0
    for query in queries:
        start = time.time()
        results = registry.search_tools(query, k=5)
        elapsed = time.time() - start
        total_time += elapsed
        print(f"  '{query}': {elapsed:.4f}s ({len(results)} results)")
    
    avg_time = total_time / len(queries)
    print(f"\n  Average search time: {avg_time:.4f}s")
    print(f"  Total time for {len(queries)} queries: {total_time:.4f}s")
    
    return avg_time < 0.1  # Should be fast


if __name__ == "__main__":
    print("ToolRegistry Test Suite\n")
    
    try:
        # Run main tests
        if test_tool_registry():
            print("\n✓ All functional tests passed")
        else:
            print("\n✗ Functional tests failed")
            sys.exit(1)
        
        # Run benchmarks
        if benchmark_search():
            print("\n✓ Performance benchmark passed")
        else:
            print("\n⚠ Performance slower than expected")
        
        print("\n=== Test Suite Completed Successfully ===")
        
    except Exception as e:
        print(f"\n✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
