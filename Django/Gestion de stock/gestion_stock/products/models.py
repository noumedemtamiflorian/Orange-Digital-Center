from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Category(models.Model):

    def __str__(self):
        return self.name
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField()


class Product(models.Model):

    name = models.CharField(max_length=30, unique=True,
                            blank=False, null=False)
    description = HTMLField(models.TextField(blank=False, null=False))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    image = models.ImageField(
        upload_to='./products/static/products/images/%Y/%m/%d/',
        default=None,
        blank=True,
        null=False
    )
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name
