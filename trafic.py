
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import json

# Définition des valeurs choisi pour l'axe X
an = [
    1840,1850, 1860, 1870, 1880, 1890, 
    1900, 1910, 1920, 1930, 1940, 1950, 
    1960, 1970, 1980, 1990, 
    2000, 2010, 2020
]

plt.xlim(1840,2020)

# Ouverture du fichier de data
fichier = open("data/trafic.json", "r")

data = json.load(fichier)

data = sorted(data, key=lambda x: x['annee'])

# Récuperation des valeurs depuis le fichier data
annee2 = [entry['annee'] for entry in data]

tonne = [entry['tonnes']for entry in data]

voyageurs = [entry['voyageurs']for entry in data]

annee = [int(i) for i in annee2]

# Affichage graphique des valeurs 
plt.plot(annee,tonne, color='brown', label='tonne')

plt.plot(annee,voyageurs, color='green', label='voyageurs')

plt.xticks(an,labels=an)

plt.legend(['voyageurs (Millions)','Marchandises (tonnes)'])

plt.title('Courbes des voyageurs et marchandises de la sncf depuis 1841')

plt.xlabel('Années')

plt.ylabel('Voyageurs (Millions) / marchandises (Tonnes)')

plt.show()

with open("result/data_voy_march.json", 'w') as fichier:
    json.dump(data,fichier, indent=2)