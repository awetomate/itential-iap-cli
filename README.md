# itential-iap-cli
Lightweight CLI tool to simplify the process of interacting with the Itential Automation Platform.

This is an early alpha release. It is incomplete and will change.

The CLI tool is built using [Typer](https://typer.tiangolo.com/) and [Typer-CLI](https://typer.tiangolo.com/typer-cli/). It uses [iap-sdk](https://pypi.org/project/iap-sdk/) for any API calls to IAP.

This package was written for Itential Automation Platform 2023.1.

## Getting Started
Make sure you have a supported version of Python installed and then create and activate a virtual environment:
```bash
python -m venv venv

source /venv/bin/activate
```
You can install the iap_cli from Pypi as follows:
```bash
pip install iap-cli
```
Or you can install it from source as follows:
```bash
git clone https://github.com/awetomate/itential-iap-cli.git
cd itential-iap-cli
python -m pip install -r requirements.txt
python -m pip install -e .
```
