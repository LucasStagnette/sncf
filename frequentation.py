import json
from formatage import formater_json

def trie_frequentation_2022(a):
    with open("data/frequentation.json", "r") as fichier:
        data = json.load(fichier)
    
    # triage de la liste avec comme clef total_voyageurs_2022
    data = sorted(data, key=lambda x: x['total_voyageurs_'+str(a)], reverse=True)

    with open("result/frequentation"+str(a)+".json", 'w') as fichier:
        json.dump(data, fichier, indent=2)

    formater_json("result/frequentation"+str(a)+".json")
trie_frequentation_2022(2022)

import matplotlib.pyplot as plt
def affichage():
    plt.plot([1,2,3,4])
    plt.ylabel('Label 1')
    plt.title("Graphe")
    plt.show()

