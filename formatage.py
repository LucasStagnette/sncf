import json

def formatage(nomFichier):
    '''
    Fonction qui prend un entrée un fichier JSON et qui le
    met en page'''

    # on utilise try pour ne pas avoir de message d'erreur
    try:
        
        with open(nomFichier, 'r') as fichier:
            donnee = json.load(fichier)

        # la fonction dumps de json insert directement du json mis en page
        donneesFinal = json.dumps(donnee, indent=4, sort_keys=True)

        # on écrit le résultat avec le même nom de fichier pour ne rien changer
        with open(nomFichier, 'w') as fichier:
            fichier.write(donneesFinal)

        print(f"Traitement réussi !")

    # si nous avons une erreur on regarde déjà si l'erreur est un fichier inexistant
    except FileNotFoundError:
        print(f"Fichier inexistant")
    # ou qu'il y a un quelconque probleme en json, on l'affiche
    except json.JSONDecodeError as error:
        print(f"Erreur de JSON{error}")