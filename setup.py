"""
Omni-Inference-in-Action Setup Script
全模态大模型高效推理实战
"""

from setuptools import setup, find_packages
from pathlib import Path

# 读取 README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# 读取依赖
requirements = []
with open("requirements.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#"):
            requirements.append(line)

setup(
    name="omni-inference-in-action",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="全模态大模型高效推理实战 - Multi-Modal Large Model Efficient Inference in Action",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-org/omni-inference-in-action",
    packages=find_packages(exclude=["tests", "docs", "examples", "benchmarks"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.3",
            "pytest-cov>=4.1.0",
            "pytest-asyncio>=0.21.1",
            "black>=23.12.0",
            "flake8>=6.1.0",
            "mypy>=1.7.1",
            "isort>=5.13.0",
        ],
        "docs": [
            "sphinx>=7.2.0",
            "sphinx-rtd-theme>=2.0.0",
            "myst-parser>=2.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "omni-inference=frameworks.common.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)

