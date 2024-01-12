import json

def calculer_pourcentage_non_conformite():
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


def conf_inf_60():
    '''Fonction qui garde toutes les gares qui ont un taux de conformité
    inférieur à 60%, et affiche le résultat total de personnes qui sont
    passés ici'''
    with open('result/conformite.json', 'r') as ficher:
        donnees = json.load(ficher)

    with open('result/frequentation2022.json', 'r') as fichierFrequentation:
        frequentation = json.load(fichierFrequentation)

    garesInf60 = {gare: taux for gare, taux in donnees.items() if taux < 60}

    garesInf60triee = dict(sorted(garesInf60.items()))

    resultat = [{"nom_gare": gare, "taux_conformite": taux} for gare, taux in garesInf60triee.items()]

    with open('result/gares_inferieur_60.json', 'w') as fichierFinal:
        json.dump(resultat, fichierFinal, indent=2)

    total_voyageurs_2022 = sum(gare_info["total_voyageurs_2022"] for gare_info in frequentation if gare_info["nom_gare"] in garesInf60)
    total_frequentation = 2906990820
    pourcentage = total_voyageurs_2022/total_frequentation*100
    print(f"Le nombre de personnes qui ont été dans des gares avec un taux de conformité inférieur à 60% est de : {total_voyageurs_2022} sur 2906990820.")
    print(f"Ce qui represente {pourcentage:.3f}%.")

def conf_inf_80():
    '''Fonction qui garde toutes les gares qui ont un taux de conformité
    inférieur à 80%, et affiche le résultat total de personnes qui sont
    passés ici'''
    with open('result/conformite.json', 'r') as ficher:
        donnees = json.load(ficher)

    with open('result/frequentation2022.json', 'r') as fichierFrequentation:
        frequentation = json.load(fichierFrequentation)

    garesInf80 = {gare: taux for gare, taux in donnees.items() if taux < 80}

    garesInf80triee = dict(sorted(garesInf80.items()))

    resultat = [{"nom_gare": gare, "taux_conformite": taux} for gare, taux in garesInf80triee.items()]

    with open('result/gares_inferieur_80.json', 'w') as fichierFinal:
        json.dump(resultat, fichierFinal, indent=2)

    total_voyageurs_2022 = sum(gare_info["total_voyageurs_2022"] for gare_info in frequentation if gare_info["nom_gare"] in garesInf80)
    total_frequentation = 2906990820
    pourcentage = total_voyageurs_2022/total_frequentation*100
    print(f"Le nombre de personnes qui ont été dans des gares avec un taux de conformité inférieur à 80% est de : {total_voyageurs_2022} sur 2906990820.")
    print(f"Ce qui represente {pourcentage:.3f}%.")