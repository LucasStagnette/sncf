import json

def wifi():
    '''
    Fonction qui trie '''
    with open("data/gares-wifi.json", "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)
    wifi_triee = sorted(donnees, key=lambda x: x['service_wifi'] == "Oui", reverse=True)

    avec_wifi = {}
    sans_wifi = {}
    for gare in wifi_triee:
        nom_gare = gare['nom_de_la_gare']
        service_wifi = gare['service_wifi']
        if service_wifi == "Oui":
            avec_wifi[nom_gare] = service_wifi
        else:
            sans_wifi[nom_gare] = service_wifi

    result = {**avec_wifi, **sans_wifi}
    with open("./result/gares-wifi.json", "w", encoding="utf-8") as fichier_resultat:
        json.dump(result, fichier_resultat, indent=2)
