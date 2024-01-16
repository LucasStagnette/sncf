import json

def nonConf():
    # fonction qui trie et nettoie le fichier json
    chemin_fichier = "./data/proprete-en-gare.json"
    with open(chemin_fichier, "r", encoding="utf-8") as fichier:
        donnees = json.load(fichier)

    proprete_en_gare_triee = sorted(donnees, key=lambda x: x['nom_gare'])

    non_conformites_par_gare = {}
    for gare in proprete_en_gare_triee:
        nom_gare = gare['nom_gare']
        taux = gare['taux_de_conformite']
        non_conformites_par_gare[nom_gare] = taux

    with open("result/conformite.json", "w", encoding="utf-8") as fichier_resultat:
        json.dump(non_conformites_par_gare, fichier_resultat, indent=2)


def confInf60():
    '''Fonction qui garde toutes les gares qui ont un taux de conformité
    inférieur à 60%, et affiche le résultat total de personnes qui sont
    passés ici'''
    with open('result/conformite.json', 'r') as ficher:
        donnees = json.load(ficher)

    with open('result/frequentation2022.json', 'r') as fichierFrequentation:
        frequentation = json.load(fichierFrequentation)

    # on ajoute les gares qui ont un taux inférieur à 60%
    garesInf60 = {}
    for gare,taux in donnees.items():
        if taux < 60:
            garesInf60[gare] = taux
    
    # on trie les gares par ordre alphabétique
    garesInf60triee = dict(sorted(garesInf60.items()))

    # on crée la liste final avec seulement leur noms et leur taux de conformité
    resultat = [{"nom_gare": gare, "taux_conformite": taux} for gare, taux in garesInf60triee.items()]

    with open('result/gares_inferieur_60.json', 'w') as fichierFinal:
        json.dump(resultat, fichierFinal, indent=2)

    # total des voyageus qui sont allés dans une gare avec un taux inférieur à 60%
    totVoyageurs2022 = 0
    for infoGare in frequentation:
        if infoGare["nom_gare"] in garesInf60:
            totVoyageurs2022 += infoGare["total_voyageurs_2022"]

    totalFreq = 2906990820
    pourcentage = totVoyageurs2022/totalFreq*100
    print(f"Le nombre de personnes qui ont été dans des gares avec un taux de conformité inférieur à 60% est de : {totVoyageurs2022} sur 2906990820.")
    print(f"Ce qui represente {pourcentage:.3f}%.")

def confInf80():
    '''Fonction qui garde toutes les gares qui ont un taux de conformité
    inférieur à 80%, et affiche le résultat total de personnes qui sont
    passés ici'''
    with open('result/conformite.json', 'r') as ficher:
        donnees = json.load(ficher)

    with open('result/frequentation2022.json', 'r') as fichierFrequentation:
        frequentation = json.load(fichierFrequentation)

    # on ajoute les gares qui ont un taux inférieur à 80%
    garesInf80 = {}
    for gare,taux in donnees.items():
        if taux < 80:
            garesInf80[gare] = taux

    # on trie les gares par ordre alphabétique
    garesInf80triee = dict(sorted(garesInf80.items()))

    # on crée la liste final avec seulement leur noms et leur taux de conformité
    resultat = [{"nom_gare": gare, "taux_conformite": taux} for gare, taux in garesInf80triee.items()]

    with open('result/gares_inferieur_80.json', 'w') as fichierFinal:
        json.dump(resultat, fichierFinal, indent=2)

    # total des voyageus qui sont allés dans une gare avec un taux inférieur à 60%
    totVoyageurs2022 = 0
    for infoGare in frequentation:
        if infoGare["nom_gare"] in garesInf80:
            totVoyageurs2022 += infoGare["total_voyageurs_2022"]

    totalFreq = 2906990820
    pourcentage = totVoyageurs2022/totalFreq*100
    print(f"Le nombre de personnes qui ont été dans des gares avec un taux de conformité inférieur à 80% est de : {totVoyageurs2022} sur 2906990820.")
    print(f"Ce qui represente {pourcentage:.3f}%.")