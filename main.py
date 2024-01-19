# Ici vous pouvez utiliser toutes les fonctions, leur utilité est inscrite dans le rapport, 
# toutes les fonctions sont commentées dans les fichiers de ce dossier

from formatage import formatage
from conformite import nonConf, confInf60, confInf80
from frequentation import frequentation_par_annee
from taux_wifi import taux_wifi
from trafic import trafic
from voywifi import voywifi
from wifi_gare import wifi
# l'ordre recommandé est celui ci, car il y a certaines fonctions qui nécéssitent des résultats d'autres fonctions

frequentation_par_annee(2022)
nonConf()
confInf60()
confInf80()
taux_wifi()
wifi()
voywifi()
trafic()

# tous les résultats seront stockés dans le dossier result