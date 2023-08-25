import requests

TEST_API = "http://51.138.206.187:4200/api/version"
response_test_api = requests.get(TEST_API)

HEALTH_API = "http://51.138.206.187:4200/api/health"
response_health_api = requests.get(HEALTH_API)

HELLO_API = "http://51.138.206.187:4200/api/hello"
response_hello_api = requests.get(HELLO_API)

READY_API = "http://51.138.206.187:4200/api/ready"
response_ready_api = requests.get(READY_API)

if response_test_api.status_code == 200:
    print("Prefect est bien installé et fonctionne correctement : ", response_test_api.json())
else:
    print("Il y a eu un problème avec la connexion à Prefect.")

if response_health_api.status_code == 200:
    print("Prefect est en bonne santé.")
else:
    print("Il y a un problème avec Prefect.")


if response_hello_api.status_code == 200:
    print("Réponse reçue avec succès :", response_hello_api.json())
elif response_hello_api.status_code == 422:
    print("Erreur de validation :", response_hello_api.json())
else:
    print(f"Statut de la réponse non reconnu : {response_hello_api.status_code}")


if response_ready_api.status_code == 200:
    print("Prefect est prêt.")
elif response_ready_api.status_code == 422:
    print("Erreur de validation :", response_ready_api.json())
else:
    print(f"Statut de la réponse non reconnu : {response_ready_api.status_code}")