from setuptools import setup, find_packages

setup(
    name="trybox",
    version="0.1.0",
    description="A terminal-based Python snippet runner for safe, local experimentation.",
    author="Navdeep Gill",
    url="https://github.com/navdeep-G/trybox",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
     "rich>=13.7.0",
     "typer>=0.12.3",
     "click<8.2.0",  # Avoids incompatibility with Typer
    ],
    entry_points={
        "console_scripts": [
            "trybox=trybox.main:main",
            "trybox-cli=trybox.cli:app",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

