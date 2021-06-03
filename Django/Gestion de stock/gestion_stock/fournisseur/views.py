from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Fournisseur
from django.core.paginator import Paginator
from .forms import FournisseurForm
from django.http import JsonResponse

# Create your views here.


def index(request):
    fournisseurs = Fournisseur.objects.all()
    produits_paginator = Paginator(fournisseurs, 2)
    pages = request.GET.get('page')
    if pages == None:
        pages = 1
    page = produits_paginator.page(pages)
    return render(request, 'fournisseurs/index.html', {
        'count': produits_paginator.count,
        'page': page
    })


def detail(request, id):
    product = Fournisseur.objects.get(id=id)
    reponse = {
        "id": product.id,
        'email': product.email,
        'addresse': product.addresse,
        'name': product.name
    }
    data = {
        'response': reponse
    }
    return JsonResponse(data)

    return
    # return render(request, 'fournisseurs/detail.html', {'product': product})


@login_required
def new(request):
    form = FournisseurForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/fournisseurs/")
    return render(request, 'fournisseurs/new.html', {
        'form': form
    })


@login_required
def edit(request, id):
    fournisseur = get_object_or_404(Fournisseur, pk=id)
    form = FournisseurForm(instance=fournisseur)
    if request.method == "POST":
        form = FournisseurForm(request.POST or None, instance=fournisseur)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect("/fournisseurs/")
    return render(request, 'fournisseurs/edit.html', {
        'form': form
    })


@login_required
def delete(request, id):
    product = get_object_or_404(Fournisseur, pk=id)
    if request.method == "POST":
        product.delete()
        return redirect("/fournisseurs/")
    return render(request, 'fournisseurs/delete.html', {
        "product": product
    })
