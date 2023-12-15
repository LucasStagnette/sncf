import json
from formatage import formater_json

def trie_frequentation_2022():
    with open("json_files/frequentation.json", "r") as fichier:
        data = json.load(fichier)
    
    data = sorted(data, key=lambda x: x['total_voyageurs_2022'], reverse=True)

    with open("result_frequentation.json", 'w') as fichier:
        json.dump(data, fichier, indent=2)

    formater_json("result_frequentation.json")

trie_frequentation_2022()
