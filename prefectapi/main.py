import requests
import json
from prefect import flow
from prefect_airbyte.server import AirbyteServer
from prefect_airbyte.connections import AirbyteConnection
from prefect_airbyte.flows import run_connection_sync

server = AirbyteServer(server_host="http://20.19.18.134", server_port=8000)
connection = AirbyteConnection(
    airbyte_server=server,
    connection_id="5cd27fba-6aed-4cb2-ba4b-3e0757d9bfe7",
    status_updates=True,
)

@flow(name="flow_airbyte")
def airbyte_syncs():
    sync_result = run_connection_sync(
        airbyte_connection=connection,
    )
    print(f'UNE ACTUALISATION AIRBYTE : {sync_result.records_synced}')

PREFECT_API_URL = "http://51.138.206.187:4200/api"  # Change to your API endpoint

# Create airbyte_syncs flow
data = {
    "name": "flow_airbyte",
    "tags": ["airbyte", "syncs"],
}


response = requests.post(PREFECT_API_URL + "/flows", data=json.dumps(data))
if response.status_code != 200 | response.status_code != 201:
    print("Failed to create flow_airbyte: {response.status_code}")
else:
    print("Flow créé avec succès.")
    print("Détails du flow :", response.json())
    flow_airbyte_id = response.json()["id"]

# Create dbt_flow
data = {
    "name": "flow_dbt",
    "tags": ["dbt", "flow"],
}
response = requests.post(PREFECT_API_URL + "/flows", data=json.dumps(data))
if response.status_code != 200 | response.status_code != 201:
    print("Failed to create flow_airbyte: {response.status_code}")
else:
    print("Flow créé avec succès.")
    print("Détails du flow :", response.json())
    flow_dbt_id = response.json()["id"]


# Exécuter le flux airbyte_syncs
data = {
    "name": "run_flow_airbyte",
    "flow_id": "392c2e32-9343-4dca-8446-b5f89d101cce",
    "tags": ["run", "airbyte", "syncs"],
    "parameters": {},  # Si des paramètres spécifiques sont nécessaires pour votre flux, ajoutez-les ici
    "state": {
        "type": "SCHEDULED",
        "name": "string",
        "message": "Run started",
    },
}

response = requests.post(PREFECT_API_URL + "/flow_runs", data=json.dumps(data))
if response.status_code != 200 | response.status_code != 201:
    print(f"Failed to run flow_airbyte: {response.status_code}")
else:
    print("Flow airbyte_syncs a démarré avec succès.")
    print("Détails du flow :", response.json())

# Exécuter le flux dbt_flow
data = {
    "name": "run_dbt_flow",
    "flow_id": "1cf6eff6-f58d-46b3-b7d9-5f63de3e5e59",
    "tags": ["run", "dbt", "flow"],
    "parameters": {},  # Si des paramètres spécifiques sont nécessaires pour votre flux, ajoutez-les ici
    "state": {
        "type": "SCHEDULED",
        "name": "string",
        "message": "Run started",
    },
}

response = requests.post(PREFECT_API_URL + "/flow_runs", data=json.dumps(data))
if response.status_code != 200 | response.status_code != 201:
    print(f"Failed to run dbt_flow: {response.status_code}")
else:
    print("Flow dbt_flow a démarré avec succès.")
    print("Détails du flow :", response.json())
