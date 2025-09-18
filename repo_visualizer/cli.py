import click
import os
from .analyzer import analyze_repo

@click.group()
def main():
    """Repo Visualizer - Generate interactive dependency graphs for repositories"""
    pass

@main.command()
@click.argument('repo_path', type=click.Path(exists=True))
@click.option('--output', '-o', default='graph.json', help='Output file for the graph JSON')
def analyze(repo_path, output):
    """Analyze a repository and generate dependency graph"""
    click.echo(f"Analyzing repository: {repo_path}")
    graph_data = analyze_repo(repo_path)
    
    import json
    with open(output, 'w') as f:
        json.dump(graph_data, f, indent=2)
    
    click.echo(f"Graph saved to {output}")

@main.command()
@click.option('--port', default=5000, help='Port to run the server on')
def serve(port):
    """Serve the visualization web app"""
    from .web import app
    click.echo(f"Serving visualization on http://localhost:{port}")
    app.run(debug=True, port=port)

if __name__ == '__main__':
    main()