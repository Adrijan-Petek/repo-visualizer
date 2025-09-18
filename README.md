# Repo Visualizer

[![CI](https://github.com/Adrijan-Petek/repo-visualizer/actions/workflows/ci.yml/badge.svg)](https://github.com/Adrijan-Petek/repo-visualizer/actions/workflows/ci.yml)

A tool that analyzes a GitHub repository and generates an interactive graph showing the structure of the codebase — files, modules, dependencies, and their relationships.

## Installation

```bash
pip install -r requirements.txt
python setup.py develop
```

## Usage

### Analyze a repository

```bash
python -m repo_visualizer.cli analyze /path/to/your/repo
```

This will generate a `graph.json` file containing the dependency graph.

### Serve the visualization

```bash
python -m repo_visualizer.cli serve
```

Open http://localhost:5000 in your browser to see the interactive graph.

## Features

- **Interactive Graph**: Nodes represent files, edges represent dependencies
- **Hover Info**: Shows file details like lines of code and file size
- **Draggable Nodes**: Click and drag to rearrange the graph
- **Zoom/Pan**: Use mouse wheel to zoom, drag background to pan

## Development

The project structure:

- `repo_visualizer/analyzer.py`: Core analysis logic
- `repo_visualizer/cli.py`: Command-line interface
- `repo_visualizer/web.py`: Flask web server
- `templates/index.html`: D3.js visualization

## License

MIT