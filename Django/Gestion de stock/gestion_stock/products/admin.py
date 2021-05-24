from django.contrib import admin
from .models import Product, Category
# Register your models here.


class ProduitAdmin(admin.ModelAdmin):
    list_display = ['__str__','name','price','quantity','description']
    search_fields = ['name']
    list_display_links = ['name']
    list_per_page = 10
    class Meta:
        model = Product


admin.site.register(Product,ProduitAdmin)
admin.site.register(Category)
