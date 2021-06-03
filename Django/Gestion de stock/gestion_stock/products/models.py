from django.db import models
from tinymce.models import HTMLField

# Create your models here.
from tinymce import  models as tinymce_models


class Category(models.Model):

    def __str__(self):
        return self.name
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField()


class Product(models.Model):

    name = models.CharField(max_length=30, unique=True,
                            blank=False, null=False)
    description = tinymce_models.HTMLField(blank=False, null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    image=models.ImageField(
        upload_to='images',
        blank=True,
        null=True
    )
    quantity=models.IntegerField(default=0)

    def __str__(self):
        return self.name
