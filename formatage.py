import json

def formater_json(nom_fichier):
    try:
        # Chargement du fichier JSON
        with open(nom_fichier, 'r') as fichier:
            donnees = json.load(fichier)

        # Mise en forme du JSON de manière lisible
        json_formate = json.dumps(donnees, indent=4, sort_keys=True)

        # Écriture du JSON formate dans le même fichier
        with open(nom_fichier, 'w') as fichier:
            fichier.write(json_formate)

        print(f"Le fichier JSON a été correctement formatté et enregistré dans {nom_fichier}")

    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
    except json.JSONDecodeError as e:
        print(f"Erreur de décodage JSON : {e}")