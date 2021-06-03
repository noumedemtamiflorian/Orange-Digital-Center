from django.db import models

# Create your models here.


class Fournisseur(models.Model):
    name = models.CharField(max_length=150)
    addresse = models.CharField(max_length=150)
    number = models.IntegerField()
    email = models.EmailField(unique=True)