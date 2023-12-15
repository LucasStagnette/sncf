# -*- coding:utf-8 -*-

import json
def trie_frequentation():
    with open("j.json", "r") as fichier:
        data = json.load(fichier)

    json_data = json.dumps(data, indent=2)  

    data = json.loads(json_data)

