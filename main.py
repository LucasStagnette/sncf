import requests

# Remplacez 'VOTRE_CLE_API' par votre clé API réelle
cle_api = 'VOTRE_CLE_API'

# Exemple de requête pour obtenir les horaires d'un train
url = 'https://api.sncf.com/v1/coverage/sncf/journeys'
params = {
    'from': 'Paris',
    'to': 'Marseille',
    'datetime': '2023-01-01T08:00:00',
    'key': cle_api
}

response = requests.get(url, params=params)

# Traitez la réponse
if response.status_code == 200:
    data = response.json()
    # Faites quelque chose avec les données
else:
    print(f"Erreur de requête : {response.status_code}")
    print(response.text)
