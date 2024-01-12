import json

import typer
from iap_cli.config import APP_DIR, CREDENTIALS_FILEPATH, INVENTORY_FILEPATH
from rich import print


def add_config():
    pass


def add_credentials():
    """
    Prompt user for username and password to be used for the server authentication.
    Creates a .env file in home directory of user. CLI app will use this .env file
    to load the values as environment variables.
    """
    print(
        "Provide the user credentials to use to authenticate with the Itential servers."
    )
    print(f"The credentials will be stored at {APP_DIR}")
    username = typer.prompt("Username: ")
    password = typer.prompt("Password: ", hide_input=True)

    if username and password:
        APP_DIR.mkdir(parents=False, exist_ok=True)
        with open(CREDENTIALS_FILEPATH, "w") as f:
            f.write(f'USERNAME = "{username}"\n')
            f.write(f'PASSWORD = "{password}"\n')


def add_server():
    """
    Add a single server to the inventory. Prompt user for a server friendly name and FQDN.
    Creates a inventory.json file in home directory of user. CLI app will use this file
    to load the server values during runtime.
    """
    print(
        "Provide the server friendly name (will be shown in CLI) and a FQDN/IP address."
    )
    print(f"The server will be stored in the {APP_DIR}/inventory.json file.")
    friendly = typer.prompt("Server Friendly Name")
    fqdn = typer.prompt("Server FQDN or IP")

    APP_DIR.mkdir(parents=False, exist_ok=True)
    if not INVENTORY_FILEPATH.exists():
        INVENTORY_FILEPATH.touch()
        json_object = json.dumps({}, indent=4)
        with open(INVENTORY_FILEPATH, "w") as f:
            f.write(json_object)

    if friendly and fqdn:
        with open(INVENTORY_FILEPATH) as f:
            servers = json.load(f)
        servers[friendly.strip()] = fqdn.strip()
        json_object = json.dumps(servers, indent=4)
        with open(INVENTORY_FILEPATH, "w") as f:
            f.write(json_object)


def add_cluster():
    """
    Add a server cluster to the inventory. Prompt user for a cluster friendly name and a list of FQDNs.
    Creates a inventory.json file in home directory of user. CLI app will use this file
    to load the server values during runtime.
    """
    print(
        "Provide the cluster friendly name (will be shown in CLI) and a comma separated list of FQDNs/IP addresses"
    )
    print(f"The cluster will be stored in the {APP_DIR}/inventory.json file.")
    friendly = typer.prompt("Cluster Friendly Name")
    fqdn = typer.prompt("Server FQDNs or IP addresses")

    APP_DIR.mkdir(parents=False, exist_ok=True)

    if not INVENTORY_FILEPATH.exists():
        INVENTORY_FILEPATH.touch()

    if friendly and fqdn:
        with open(INVENTORY_FILEPATH) as f:
            servers = json.load(f)
        fqdn_list = [f.strip() for f in fqdn.split(",")]
        servers[friendly.strip()] = fqdn_list
        json_object = json.dumps(servers, indent=4)
        with open(INVENTORY_FILEPATH, "w") as f:
            f.write(json_object)
