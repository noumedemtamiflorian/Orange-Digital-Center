from django.db import models

# Create your models here.


class Fournisseur(models.Model):
    nom = models.CharField(max_length=50)
    addresse = models.CharField(max_length=15)

    def __str__(self):
        return self.nom
