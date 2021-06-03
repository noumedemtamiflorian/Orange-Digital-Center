#conding: utf-8

from fonctions import  *
from termcolor import colored
produts = []

def  acceuil():
    print(colored("\nBienvenue a la gestion des stocks",color='blue'))
    try:
     choix = int(input(colored("""
     \nsouhaitez-vous
     \nVoir les produits : 1
     \nAjouter un product: 2
     \nSupprimer un product: 3
     \nQuitter: 4
     \nVotre choix : ? """,color="yellow")))
    except ValueError:
        print(colored("Desole entrer un entier",color="red"))
        acceuil()

    if (choix == 1):
        afficher(produts)
        acceuil()
    elif  (choix == 2):
        ajouter(produts)
        acceuil()
    elif (choix == 3):
        supprimer(produts)
        acceuil()
    elif (choix == 4):
        print("\nAurevoir")
    else:
        print(colored("Entrer l'entier proposer :",color="red"))
        acceuil()

acceuil()