import json

def frequentation_par_annee(annee):
    '''
    Fonction qui prend en entrée une année de 2015 à 2022, et qui crée un fichier
    JSON avec le résultat de l'année en entrée'''
    with open("data/frequentation.json", "r") as fichier:
        donnee = json.load(fichier)
    
    # triage de la liste avec comme clef total_voyageurs_2022
    donnee = sorted(donnee, key=lambda x: x['total_voyageurs_'+str(annee)], reverse=True)

    with open("result/frequentation"+str(annee)+".json", 'w') as fichier:
        json.dump(donnee, fichier, indent=2)