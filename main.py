#!/usr/bin/env python3
"""
Command-Line tool to simplify the interaction with the Itential API.
Leverages the iap-sdk package and is based on Typer.
Works with Typer-CLI and offers autocompletion.
"""

from iap_cli import iap

if __name__ == "__main__":
    """
    This allows us to run the iap app using ./main.py instead of calling iap in the itential package directly
    """
    iap()
