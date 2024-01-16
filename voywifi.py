import json
def voywifi():

    # on importe les données
    with open('result/frequentation2022.json', 'r') as fichier:
        frequentationGares = json.load(fichier)
    with open('result/gares-wifi.json', 'r') as fichier:
        wifi = json.load(fichier)

    gare = {}

    # pour chaque gare on met dans un dictionnaire son nom et valeur la frequentation et le statut du wifi
    for frequentation in frequentationGares:
        nom = frequentation['nom_gare']
        gare[nom] = {'total_voyageurs_2022': frequentation['total_voyageurs_2022'],'wifi': wifi.get(nom, 'Non')}

    # le nombre de voyageurs avec et sans wifi
    voyWifi = sum(data['total_voyageurs_2022'] for data in gare.values() if data['wifi'] == 'Oui')
    voySansWifi = sum(data['total_voyageurs_2022'] for data in gare.values() if data['wifi'] == 'Non')

    # dictionnaire final 
    resultat = {'total_personnes_avec_wifi': voyWifi,'total_personnes_sans_wifi': voySansWifi}

    with open('result/voyageurs-wifi.json', 'w') as fichier:
        json.dump(resultat, fichier, indent=2)