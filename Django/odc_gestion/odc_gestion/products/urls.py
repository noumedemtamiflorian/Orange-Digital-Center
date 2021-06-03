from django.urls import path

from . views import produit_list,show_produit

urlpatterns = [
    path("", produit_list,name="produit_list"),
    path("<int:id>", show_produit,name="show_produit")
]