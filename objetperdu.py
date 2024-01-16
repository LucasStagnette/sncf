import json
def perte():
    with open('data/objet.json', 'r', encoding='utf-8') as fichier:
        objetsperdu = json.load(fichier)

    with open('result/frequentation2022.json', 'r', encoding='utf-8') as fichier:
        frequentation = json.load(fichier)

    # Calculer le nombre d'objets perdus par gare
    objetGare = {}
    for objet in objetsperdu:
        gare = objet['gc_obo_gare_origine_r_name']
        objetGare[gare] = objetGare.get(gare, 0) + 1

    resultats = []
    # Calculer le rapport entre le nb objet perdu et les voyageurs
    for gareInfo in frequentation:
        nomGare = gareInfo.get('nomGare', '')
        totVoyGare = gareInfo.get('total_voyageurs_2022', 0)
        objetPerduGare = objetGare.get(nomGare, 0)

        if totVoyGare != 0:
            rapport = (objetPerduGare / totVoyGare) * 100
            resultats.append({"nomGare": nomGare, "rapport_perte_objets": rapport})

    # Trier la liste par ordre décroissant du pourcentage le plus élevé
    resultat = sorted(resultats, key=lambda x: x["rapport_perte_objets"], reverse=True)

    with open('result/perte_objets.json', 'w', encoding='utf-8') as fichier:
        json.dump(resultat, fichier, ensure_ascii=False, indent=2)

