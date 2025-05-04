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
        "rich",  # required if using rich for UI/CLI output
    ],
    entry_points={
        "console_scripts": [
            "trybox=trybox.main:main",
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

