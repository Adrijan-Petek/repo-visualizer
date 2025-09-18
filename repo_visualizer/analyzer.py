import os
import ast
import json
from pathlib import Path
import networkx as nx

def analyze_repo(repo_path):
    """Analyze a repository and return graph data"""
    repo_path = Path(repo_path)
    
    # Find all Python files
    python_files = list(repo_path.rglob("*.py"))
    
    # Build dependency graph
    G = nx.DiGraph()
    
    # Add nodes for all files
    for file_path in python_files:
        relative_path = file_path.relative_to(repo_path)
        G.add_node(str(relative_path), 
                  type='file', 
                  path=str(relative_path),
                  size=file_path.stat().st_size,
                  lines=count_lines(file_path))
    
    # Add edges for dependencies
    for file_path in python_files:
        relative_path = file_path.relative_to(repo_path)
        imports = extract_imports(file_path)
        
        for imp in imports:
            # Try to resolve import to a file in the repo
            target = resolve_import(imp, repo_path, relative_path.parent)
            if target and target in G:
                G.add_edge(str(relative_path), target, type='import')
    
    # Convert to JSON-serializable format
    nodes = []
    for node, data in G.nodes(data=True):
        nodes.append({
            'id': node,
            'type': data.get('type'),
            'size': data.get('size', 0),
            'lines': data.get('lines', 0)
        })
    
    edges = []
    for source, target, data in G.edges(data=True):
        edges.append({
            'source': source,
            'target': target,
            'type': data.get('type')
        })
    
    return {
        'nodes': nodes,
        'edges': edges
    }

def count_lines(file_path):
    """Count lines in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return sum(1 for _ in f)
    except:
        return 0

def extract_imports(file_path):
    """Extract import statements from a Python file"""
    imports = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module.split('.')[0])
    except:
        pass
    
    return imports

def resolve_import(import_name, repo_path, current_dir):
    """Try to resolve an import to a file in the repo"""
    # Simple resolution: look for import_name.py in current dir or subdirs
    candidates = [
        current_dir / f"{import_name}.py",
        repo_path / f"{import_name}.py",
        *(repo_path.rglob(f"{import_name}.py"))
    ]
    
    for candidate in candidates:
        if candidate.exists():
            try:
                return str(candidate.relative_to(repo_path))
            except:
                continue
    
    return None