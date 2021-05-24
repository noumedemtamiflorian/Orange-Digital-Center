from django.db import models

class Category(models.Model):
    nom = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.nom

# Create your models here.

class Produits(models.Model):
    nom = models.CharField(max_length=50, blank=False, null=False, unique=True)
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    marque = models.CharField(max_length=50, blank=False, null=False)
    code = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.nom