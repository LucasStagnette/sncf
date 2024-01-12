import json

def formatage(nomFichier):
    '''
    Fonction qui prend un entrée un fichier JSON et qui le
    met en page'''
    # on regarde si il n'y a pas d'erreur
    try:
        
        with open(nomFichier, 'r') as fichier:
            donnee = json.load(fichier)

        # on met en page le json
        donneesFinal = json.dumps(donnee, indent=4, sort_keys=True)

        # on écrit le résultat
        with open(nomFichier, 'w') as fichier:
            fichier.write(donneesFinal)

        print(f"Le fichier JSON mis en page est enregistré à ce nom : {nomFichier}")

    # sinon on regarde si le fichier est trouvé ou non
    except FileNotFoundError:
        print(f"Le fichier {nomFichier} n'a pas été trouvé.")
    # ou que le fichier a un problème en json
    except json.JSONDecodeError as e:
        print(f"Erreur de JSON{e}")