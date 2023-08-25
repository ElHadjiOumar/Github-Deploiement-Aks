import requests

flow_id = "8adad023-4be1-4abf-af34-34de3aafd114"  # Remplacez par l'ID du flux que vous voulez récupérer
PREFECT_API_URL = f"http://51.138.206.187:4200/api/flows/{flow_id}"

response = requests.get(PREFECT_API_URL)

if response.status_code == 200:
    print("Détails du flow récupérés avec succès :", response.json())
elif response.status_code == 422:
    print("Erreur de validation :", response.json())
else:
    print(f"Statut de la réponse non reconnu : {response.status_code}")
