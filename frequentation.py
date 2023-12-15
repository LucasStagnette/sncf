import json
from formatage import formater_json

def trie_frequentation_2022():
    with open("data/frequentation.json", "r") as fichier:
        data = json.load(fichier)
    
    # triage de la liste avec comme clef total_voyageurs_2022
    data = sorted(data, key=lambda x: x['total_voyageurs_2022'], reverse=True)

    with open("result/frequentation22.json", 'w') as fichier:
        json.dump(data, fichier, indent=2)

    formater_json("result/frequentation22.json")

def trie_frequentation_2021():
    with open("data/frequentation.json", "r") as fichier:
        data = json.load(fichier)
    
    # triage de la liste avec comme clef total_voyageurs_2021
    data = sorted(data, key=lambda x: x['total_voyageurs_2021'], reverse=True)

    with open("result/frequentation21.json", 'w') as fichier:
        json.dump(data, fichier, indent=2)

    formater_json("result/frequentation21.json")

def trie_frequentation_2020():
    with open("data/frequentation.json", "r") as fichier:
        data = json.load(fichier)
    
    # triage de la liste avec comme clef total_voyageurs_2020
    data = sorted(data, key=lambda x: x['total_voyageurs_2020'], reverse=True)

    with open("result/frequentation20.json", 'w') as fichier:
        json.dump(data, fichier, indent=2)

    formater_json("result/frequentation20.json")

def trie_frequentation_2019():
    with open("data/frequentation.json", "r") as fichier:
        data = json.load(fichier)
    
    # triage de la liste avec comme clef total_voyageurs_2019
    data = sorted(data, key=lambda x: x['total_voyageurs_2019'], reverse=True)

    with open("result/frequentation19.json", 'w') as fichier:
        json.dump(data, fichier, indent=2)

    formater_json("result/frequentation19.json")

def trie_frequentation_2018():
    with open("data/frequentation.json", "r") as fichier:
        data = json.load(fichier)
    
    # triage de la liste avec comme clef total_voyageurs_2018
    data = sorted(data, key=lambda x: x['total_voyageurs_2018'], reverse=True)

    with open("result/frequentation18.json", 'w') as fichier:
        json.dump(data, fichier, indent=2)

    formater_json("result/frequentation18.json")

def trie_frequentation_2017():
    with open("data/frequentation.json", "r") as fichier:
        data = json.load(fichier)
    
    # triage de la liste avec comme clef total_voyageurs_2017
    data = sorted(data, key=lambda x: x['totalvoyageurs2017'], reverse=True)

    with open("result/frequentation17.json", 'w') as fichier:
        json.dump(data, fichier, indent=2)

    formater_json("result/frequentation17.json")

def trie_frequentation_2016():
    with open("data/frequentation.json", "r") as fichier:
        data = json.load(fichier)
    
    # triage de la liste avec comme clef total_voyageurs_2016
    data = sorted(data, key=lambda x: x['total_voyageurs_2016'], reverse=True)

    with open("result/frequentation16.json", 'w') as fichier:
        json.dump(data, fichier, indent=2)

    formater_json("result/frequentation16.json")

def trie_frequentation_2015():
    with open("data/frequentation.json", "r") as fichier:
        data = json.load(fichier)
    
    # triage de la liste avec comme clef total_voyageurs_2015
    data = sorted(data, key=lambda x: x['total_voyageurs_2015'], reverse=True)

    with open("result/frequentation15.json", 'w') as fichier:
        json.dump(data, fichier, indent=2)

    formater_json("result/frequentation15.json")

trie_frequentation_2015()
trie_frequentation_2016()
trie_frequentation_2017()
trie_frequentation_2018()
trie_frequentation_2019()
trie_frequentation_2020()
trie_frequentation_2022()
trie_frequentation_2021()
import matplotlib.pyplot as plt
def affichage():
    plt.plot([1,2,3,4])
    plt.ylabel('Label 1')
    plt.title("Graphe")
    plt.show()
