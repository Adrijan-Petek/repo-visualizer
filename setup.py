from setuptools import setup, find_packages

setup(
    name="repo-visualizer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "astroid",
        "networkx",
    ],
    entry_points={
        "console_scripts": [
            "repo-vis=repo_visualizer.cli:main",
        ],
    },
    author="Your Name",
    description="Interactive dependency graph generator for GitHub repositories",
    long_description=open("README.md").read() if "README.md" in open("README.md").read() else "",
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/repo-visualizer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)