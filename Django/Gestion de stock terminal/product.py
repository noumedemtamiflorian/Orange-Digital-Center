from termcolor import colored
class product:
    
    def __init__(self,nom,prix,description):
        self.nom = nom
        self.prix = prix
        self.description = description
    
    def  __str__(self):
        return colored("{} {} {}".format(self.nom,self.prix,self.description),color="green")