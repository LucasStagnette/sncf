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


def voyageur_conformite_inferieur_60():
    # fonction qui regarde quelles gares ont un taux de conformite inferieur à 60% et le nombre de voyageurs qui l'a visite chaque annee
    with open('result/conformite.json', 'r') as conformite_file:
        taux_conformite_data = json.load(conformite_file)

    with open('result/frequentation2022.json', 'r') as frequentation_file:
        frequentation_data = json.load(frequentation_file)

    total_voyageurs_2022 = 0

    gares_inferieur_60 = [gare for gare, taux in taux_conformite_data.items() if taux < 60]

    for gare_info in frequentation_data:
        if gare_info["nom_gare"] in gares_inferieur_60:
            # Ajouter le nombre de voyageurs en 2022
            total_voyageurs_2022 += gare_info["total_voyageurs_2022"]

    print("Le nombre de voyageurs transportés qui ont accès à des gares avec un taux de conformité inférieur à 60% est de :", total_voyageurs_2022, "sur 1244000 de voyageurs.")

voyageur_conformite_inferieur_60()