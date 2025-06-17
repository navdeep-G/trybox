from setuptools import setup, find_packages

setup(
    name="trybox",
    version="0.1.0",
    description="Terminal-based Python snippet runner for safe, local experimentation.",
    author="Navdeep Gill",
    url="https://github.com/navdeep-G/trybox",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=[
        "rich>=13.7.0",
        "typer>=0.12.3",
        "click<8.2.0",  # Required for Typer compatibility
    ],
    entry_points={
        "console_scripts": [
            "trybox=trybox.main:main",
            "trybox-cli=trybox.cli:app",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: Developers",
    ],
)
