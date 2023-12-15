# -*- coding:utf-8 -*-

import json

with open("j.json", "r") as fichier:
    data = json.load(fichier)

json_data = json.dumps(data, indent=2)  

parsed_data = json.loads(json_data)



fichier = open("result.txt", "w")
top1 = [parsed_data[0]['nom_gare'], parsed_data[0]["total_voyageurs_2018"]]
top2 = [parsed_data[1]['nom_gare'], parsed_data[1]["total_voyageurs_2018"]]
top3 = [parsed_data[2]['nom_gare'], parsed_data[2]["total_voyageurs_2018"]]
top4 = [parsed_data[3]['nom_gare'], parsed_data[3]["total_voyageurs_2018"]]
top5 = [parsed_data[4]['nom_gare'], parsed_data[4]["total_voyageurs_2018"]]
top6 = [parsed_data[5]['nom_gare'], parsed_data[5]["total_voyageurs_2018"]]
top7 = [parsed_data[6]['nom_gare'], parsed_data[6]["total_voyageurs_2018"]]
top8 = [parsed_data[7]['nom_gare'], parsed_data[7]["total_voyageurs_2018"]]
top9 = [parsed_data[8]['nom_gare'], parsed_data[8]["total_voyageurs_2018"]]
top10 = [parsed_data[9]['nom_gare'], parsed_data[9]["total_voyageurs_2018"]]

''''
for gare in parsed_data:
    fichier.write(str(gare['nom_gare'])+ ": " + str(gare["total_voyageurs_2018"])+"\n")'''

for gare in parsed_data:
    print(type(gare['total_voyageurs_2018']))
    print(type(top1[1]))
    if gare['total_voyageurs_2018']>top1[1]:
        top1 = [gare['nom_gare'], gare["total_voyageurs_2018"]]
    elif gare['total_voyageurs_2018']>top2[1]:
        top2 = [gare['nom_gare'], gare["total_voyageurs_2018"]]
    elif gare['total_voyageurs_2018']>top3[1]:
        top3 = [gare['nom_gare'], gare["total_voyageurs_2018"]]
    elif gare['total_voyageurs_2018']>top4[1]:
        top4 = [gare['nom_gare'], gare["total_voyageurs_2018"]]
    elif gare['total_voyageurs_2018']>top5[1]:
        top5 = [gare['nom_gare'], gare["total_voyageurs_2018"]]
    elif gare['total_voyageurs_2018']>top6[1]:
        top6 = [gare['nom_gare'], gare["total_voyageurs_2018"]]
    elif gare['total_voyageurs_2018']>top7[1]:
        top7 = [gare['nom_gare'], gare["total_voyageurs_2018"]]
    elif gare['total_voyageurs_2018']>top8[1]:
        top8 = [gare['nom_gare'], gare["total_voyageurs_2018"]]
    elif gare['total_voyageurs_2018']>top9[1]:
        top9 = [gare['nom_gare'], gare["total_voyageurs_2018"]]
    elif gare['total_voyageurs_2018']>top10[1]:
        top10 = [gare['nom_gare'], gare["total_voyageurs_2018"]]
    

print(top1, top2, top3, top4, top5, top6, top7, top8, top9, top10)