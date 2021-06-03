from .forms import addProduitForm
from django.shortcuts import render, get_object_or_404
from .models import Produits
from django.http import JsonResponse ,HttpResponse
from django.core import serializers

# Create your views here.


def produit_list(request):
    produits = Produits.objects.all()
    form = addProduitForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            produit = form.save()
            form = addProduitForm()
    return render(request, "liste-produit.html", context={
        "produits": produits,
        'form': form
    })


def show_produit(request, **kargs):
    id = kargs.get("id")
    produit = get_object_or_404(Produits, pk=id)
    produit_json = serializers.serialize('jsonl',[produit],use_natural_foreign_keys=True)
    return HttpResponse(produit_json)