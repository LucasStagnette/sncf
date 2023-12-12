# -*- coding:utf-8 -*-

import json

with open("j.json", "r") as fichier:
    data = json.load(fichier)

json_data = json.dumps(data, indent=2)  

parsed_data = json.loads(json_data)



fichier = open("result.txt", "w")

for gare in parsed_data:
    fichier.write(str(gare['nom_gare'])+ ": " + str(gare["total_voyageurs_2018"])+"\n")