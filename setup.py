from setuptools import find_packages, setup
from pathlib import Path
from typing import List, Tuple

HERE = Path(__file__).parent

def get_requirements(path: str = HERE / "requirements.txt") -> Tuple[List[str], List[str]]:
    requirements = []
    extra_indices = []
    with open(path) as f:
        for line in f.readlines():
            line = line.rstrip("\r\n")
            if line.startswith("--extra-index-url "):
                extra_indices.append(line[18:])
                continue
            requirements.append(line)
    return requirements, extra_indices

requirements, extra_indices = get_requirements()

packages = find_packages(exclude=["depth_vis", "checkpoints", "assets"])

setup(
    name="depth-anything-v2",
    version="1.0",
    install_requires=[],
    packages=packages,
    extras_require={
        "all": requirements    
    }
)