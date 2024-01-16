import json

def taux_wifi():
    '''
    Fonction qui affiche le taux de gare avec et sans wifi'''
    with open("./data/gares-wifi.json", "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)

    total = len(donnees)
    gares_avec = sum(1 for gare in donnees if gare['service_wifi'] == "Oui")
    gares_sans = total - gares_avec

    taux_avec_wifi = (gares_avec / total) * 100
    taux_sans_wifi = (gares_sans / total) * 100

    result = {
        "nombre_de_gares": total,
        "gares_avec_wifi": {
            "nombre": gares_avec,
            "taux": f"{taux_avec_wifi:.2f}%"
        },
        "gares_sans_wifi": {
            "nombre": gares_sans,
            "taux": f"{taux_sans_wifi:.2f}%"
        }
    }

    with open("./result/taux-wifi.json", "w", encoding="utf-8") as fichier_resultat:
        json.dump(result, fichier_resultat, indent=2)

