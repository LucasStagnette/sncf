import json
import matplotlib.pyplot as plt

with open('data/regularite.json', 'r') as fichier:
    data = json.load(fichier)

abscisse = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

date2 = [valeur["date"] for valeur in data]
ponctualite_origine = [valeur["ponctualite_origine"] for valeur in data]
date = [int(i[:4]) for i in date2]
plt.bar(date2, ponctualite_origine, color='black')
plt.xlabel('Mois')
plt.ylabel('Ponctualité (%)')
plt.xticks(date,labels=date)

plt.show()
