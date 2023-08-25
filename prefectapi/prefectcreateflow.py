import requests
import json

PREFECT_API_URL = "http://51.138.206.187:4200/api/flows"

data = {
    "name": "flow-oumar",
    "tags": ["tag-4", "tag-9"]
}

response = requests.post(PREFECT_API_URL, data=json.dumps(data))

if response.status_code == 200 | response.status_code == 201:
    print("Flow créé avec succès.")
    print("Détails du flow :", response.json())
elif response.status_code == 422:
    print("Erreur de validation :", response.json())
else:
    print(f"Statut de la réponse non reconnu : {response.status_code}")
