import pathlib

import setuptools

setuptools.setup(
    name="iap_sdk",
    version="2024.1a1",
    description="Lightweight CLI tool to simplify the process of interacting with the Itential Automation Platform.",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/awetomate/itential-iap-cli",
    author="John Frauchiger",
    author_email="john@awetomate.net",
    license="MIT",
    project_urls={
        "Documentation": "https://github.com/awetomate/itential-iap-cli",
        "Source": "https://github.com/awetomate/itential-iap-cli",
    },
    classifiers=[
        "Development Status :: 4 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Utilities"
    ],
    python_requires=">=3.9,<3.12",
    install_requires=[
        "iap-sdk",
        "pydantic",
        "python-dotenv",
        "typer[all]",
        "typer-cli"
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
)
