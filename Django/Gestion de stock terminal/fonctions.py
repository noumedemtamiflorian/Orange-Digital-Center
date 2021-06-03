#coding: utf-8
from product import *
from termcolor import colored

def repeat(message, action, product):
    choice = str(input(colored(message,color="magenta")))
    if choice.lower() == "oui":
        action(product)
    else:
        pass


def ajouter(produts):
    print(colored("\n\n\nVous etes entrain d'ajouter un produit",color="blue"))
    try:
        nom = str(input(colored("\nEntrer le nom du produit : ",color="yellow")))
        prix = int(input(colored("\nS'il vous plait son prix : ",color="yellow")))
        description = str(
            input(colored("\nEt enfin sa description : ",color="yellow")))
    except ValueError:
        print(colored("\nEntrer un bonne element",color="red"))
        ajouter(produts)
    produts.append(product(nom, prix, description))
    repeat(
        "\nAimeriez vous ajouter un produit [Oui | Non => autres] ? ", ajouter, produts)


def afficher(produts):
    if len(produts) > 0:
        print(colored("\n\n\nVoici la liste de vos produits\n",color="blue"))
        for value in produts:
            print(colored(produts.index(value),color="yellow"), " : ", value)
        print("")
    else:
        print(colored("\n\nAucun produits n'est disponible dans le stock \n",color="red"))


def supprimer(products):
    if len(products) > 0:
        afficher(products)
        numero = int(
            input("Quel est le numero de l'element que vous voulez supprimer ? "))
        del products[numero]
        repeat(
            "\naimeriez vous supprimer un autre article ? [Oui | Non => autres] ? ", supprimer, products)

    else:
        print(colored("Aucun produit n'est disponible pour l'instant",color="red"))


if __name__ == "__main__":

    def plusOne(nombre):
        print(nombre+2)
    repeat("Entrer : [Oui | Non => autres] ", plusOne, 2)
