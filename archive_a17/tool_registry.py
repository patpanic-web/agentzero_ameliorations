"""
ToolRegistry - Semantic search for MCP tools

This module provides semantic indexing and search capabilities for MCP tools,
reducing token usage by returning only the most relevant tools instead of all.

Usage:
    from extensions.tool_registry import ToolRegistry
    
    # Load tools from registry
    with open('/a0/usr/projects/agentzero_ameliorations/.a0proj/knowledge/tools_registry.json') as f:
        tools_data = json.load(f)
    
    # Create and index tools
    registry = ToolRegistry()
    registry.index_tools(tools_data)
    
    # Search for relevant tools
    results = registry.search_tools("web search engine", k=5)
    
    # Get tool by exact name
    tool = registry.get_tool_by_name("tavily_search")

Architecture:
    - Uses FAISS for vector similarity search
    - Uses SentenceTransformer for embeddings
    - Stores index in /a0/usr/memory/tools/
    - No dependencies on Agent-Zero core modules

Performance:
    - Baseline: ~613 tokens (all tools description)
    - With ToolRegistry: ~50-100 tokens (top-K tools)
    - Token savings: ~85%
"""

import json
import os
from typing import List, Dict, Any, Optional
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle
import logging

logger = logging.getLogger(__name__)


class ToolRegistry:
    """
    Registry for indexing and searching MCP tools using semantic search.
    Uses FAISS for vector similarity search with SentenceTransformer embeddings.
    
    Attributes:
        index_dir (str): Directory for storing FAISS index and metadata
        embedding_model (SentenceTransformer): Model for generating embeddings
        dimension (int): Dimension of embedding vectors
        index (faiss.IndexFlatIP): FAISS index for similarity search
        tools_by_id (Dict[str, Dict]): Tool metadata by ID
        tool_names (Dict[str, str]): Mapping from tool name to ID
    """
    
    def __init__(self, index_dir: str = "/a0/usr/memory/tools"):
        """
        Initialize ToolRegistry.
        
        Args:
            index_dir: Directory to store FAISS index and metadata
        """
        self.index_dir = index_dir
        os.makedirs(index_dir, exist_ok=True)
        
        # Use lightweight model for embeddings
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.dimension = self.embedding_model.get_sentence_embedding_dimension()
        
        self.index = None
        self.tools_by_id = {}
        self.tool_names = {}
        
        # Try to load existing index
        self._load_index()
    
    def _load_index(self) -> None:
        """Load existing FAISS index and tool metadata."""
        index_path = os.path.join(self.index_dir, "index.faiss")
        metadata_path = os.path.join(self.index_dir, "index.pkl")
        
        if os.path.exists(index_path) and os.path.exists(metadata_path):
            try:
                self.index = faiss.read_index(index_path)
                with open(metadata_path, 'rb') as f:
                    metadata = pickle.load(f)
                    self.tools_by_id = metadata['tools_by_id']
                    self.tool_names = metadata['tool_names']
                logger.info(f"Loaded existing index with {len(self.tools_by_id)} tools")
            except Exception as e:
                logger.warning(f"Failed to load index: {e}")
                self._create_new_index()
        else:
            self._create_new_index()
    
    def _create_new_index(self) -> None:
        """Create a new FAISS index."""
        self.index = faiss.IndexFlatIP(self.dimension)  # Inner product similarity
        logger.info("Created new FAISS index")
    
    def _save_index(self) -> None:
        """Save FAISS index and tool metadata."""
        index_path = os.path.join(self.index_dir, "index.faiss")
        metadata_path = os.path.join(self.index_dir, "index.pkl")
        
        if self.index:
            faiss.write_index(self.index, index_path)
        
        metadata = {
            'tools_by_id': self.tools_by_id,
            'tool_names': self.tool_names
        }
        with open(metadata_path, 'wb') as f:
            pickle.dump(metadata, f)
        
        logger.info(f"Saved index with {len(self.tools_by_id)} tools")
    
    def index_tools(self, tools: List[Dict[str, Any]]) -> None:
        """
        Index a list of tools for semantic search.
        
        Args:
            tools: List of tool dictionaries with 'name', 'description', 'category', etc.
        """
        if not tools:
            logger.warning("No tools provided for indexing")
            return
        
        # Clear existing index
        self._create_new_index()
        self.tools_by_id = {}
        self.tool_names = {}
        
        texts_to_embed = []
        
        for i, tool in enumerate(tools):
            # Create embedding text combining key fields
            name = tool.get('name', '')
            description = tool.get('description', '')
            category = tool.get('category', '')
            parameters = ' '.join(tool.get('parameters', []))
            server = tool.get('server', '')
            
            tool_text = f"{name} {description} {category} {parameters} {server}"
            texts_to_embed.append(tool_text)
            
            # Store tool metadata
            tool_id = str(i)
            self.tools_by_id[tool_id] = tool
            self.tool_names[name] = tool_id
        
        # Generate embeddings
        embeddings = self.embedding_model.encode(texts_to_embed, normalize_embeddings=True)
        
        # Add to FAISS index
        self.index.add(np.array(embeddings).astype('float32'))
        
        # Save index
        self._save_index()
        logger.info(f"Indexed {len(tools)} tools")
    
    def search_tools(self, query: str, k: int = 5) -> List[Dict[str, Any]]:
        """
        Search for tools semantically similar to the query.
        
        Args:
            query: Search query text
            k: Number of results to return (default: 5)
            
        Returns:
            List of tool dictionaries sorted by relevance, with added 'similarity_score' field
        """
        if not self.index or self.index.ntotal == 0:
            logger.warning("No tools indexed")
            return []
        
        # Validate k
        k = max(1, min(k, self.index.ntotal))
        
        # Encode query
        query_embedding = self.embedding_model.encode([query], normalize_embeddings=True)
        query_vector = np.array(query_embedding).astype('float32')
        
        # Search in FAISS index
        distances, indices = self.index.search(query_vector, k)
        
        # Convert to tool results
        results = []
        for distance, idx in zip(distances[0], indices[0]):
            if idx >= 0 and str(idx) in self.tools_by_id:
                tool = self.tools_by_id[str(idx)].copy()
                tool['similarity_score'] = float(distance)
                results.append(tool)
        
        logger.debug(f"Search query '{query}' returned {len(results)} results")
        return results
    
    def get_tool_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Get a tool by its exact name.
        
        Args:
            name: Exact tool name
            
        Returns:
            Tool dictionary or None if not found
        """
        tool_id = self.tool_names.get(name)
        if tool_id:
            return self.tools_by_id.get(tool_id)
        return None
    
    def get_all_tools(self) -> List[Dict[str, Any]]:
        """
        Get all indexed tools.
        
        Returns:
            List of all tool dictionaries
        """
        return list(self.tools_by_id.values())
    
    def get_tool_count(self) -> int:
        """
        Get number of indexed tools.
        
        Returns:
            Number of tools in index
        """
        return len(self.tools_by_id)


# Convenience function for quick initialization
def get_tool_registry() -> ToolRegistry:
    """
    Get or create ToolRegistry instance.
    
    Returns:
        ToolRegistry instance
    """
    return ToolRegistry()


if __name__ == "__main__":
    # Example usage
    import json
    
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    
    # Load tools data
    tools_path = "/a0/usr/projects/agentzero_ameliorations/.a0proj/knowledge/tools_registry.json"
    if os.path.exists(tools_path):
        with open(tools_path, 'r') as f:
            tools_data = json.load(f)
        
        # Create registry
        registry = ToolRegistry()
        
        # Index tools
        registry.index_tools(tools_data)
        
        print(f"Indexed {registry.get_tool_count()} tools")
        
        # Test searches
        test_queries = [
            "web search engine",
            "git commit repository",
            "browser automation click",
            "system memory monitoring"
        ]
        
        for query in test_queries:
            results = registry.search_tools(query, k=3)
            print(f"\nQuery: '{query}'")
            for i, tool in enumerate(results):
                print(f"  {i+1}. {tool['name']} ({tool['category']}) - score: {tool['similarity_score']:.3f}")
        
        # Test get by name
        tool = registry.get_tool_by_name("git_commit")
        print(f"\nTool 'git_commit': {tool['name'] if tool else 'Not found'}")
    else:
        print(f"Tools file not found at {tools_path}")
