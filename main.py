import requests
import json
import os

def request_tgv():
    cle_api = '2513128f-8f52-459a-97b0-e2c675472568'

    url = 'https://api.sncf.com/v1/coverage/sncf/stop_areas/stop_area:SNCF:87391003/departures'
    params = {
        'datetime': '2023-12-05T08:51:10',
        'key': cle_api
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return(data)
    else:
        return(f"Erreur de requête : {response.status_code}\n{response.text}")
    

def save_tgv(nom_fichier):

    fichier = open(nom_fichier+".txt", 'w')
    fichier.write(str(request_tgv()))
def affichage(nom_fichier):
    
    fichier = open(nom_fichier, "r")
    json_s = fichier.read()
    donnees = json.loads(json_s)
    for cle, valeur in donnees.items():
        print(f"{cle}: {valeur}")