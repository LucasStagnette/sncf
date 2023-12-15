# -*- coding:utf-8 -*-
import json
def trie_frequentation_2022():
    # ouverture et stockage dans une variable du fichier json
    with open("json_files/frequentation.json", "r") as fichier:
        data = json.load(fichier)
    json_data = json.dumps(data, indent=2)  
    data = json.loads(json_data)
    
    max = -100000
    nom = ""
    for i in range(len(data)-1):
        for gare in data:
            nb = gare['total_voyageurs_2022']
            if nb > max:
                max = nb 
                nom = gare['nom_gare']



trie_frequentation_2022()