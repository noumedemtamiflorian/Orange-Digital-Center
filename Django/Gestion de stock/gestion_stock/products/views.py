from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from django.core.paginator import Paginator
from django.views.generic import ListView
from .forms import ProductForm, CategoryForm


# Create your views here.


def index(request):
    produits = Paginator(Product.objects.all(),10).page(1)
    return render(request, 'products/index.html', {
        'products': produits,
    })

def index_category(request):
    categories = Paginator(Category.objects.all(),10).page(1)
    return render(request, 'category/index.html', {
        'categories': categories,
    })

@login_required
def detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/detail.html', {'product': product})

@login_required
def productByCategory(request, slug):
    category = Category.objects.get(slug=slug)
    categories = Category.objects.all()
    products = Product.objects.filter(category=category.id)
    return render(request, 'products/postByCategory.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


@login_required
def new(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/products/")
    return render(request, 'products/new.html', {
        'form': form
    })

@login_required
def new_category(request, id):
    pass

@login_required
def edit(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST or None, instance=product)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect("/products/")
    return render(request, 'products/edit.html', {
        'form': form
    })

@login_required
def edit_category(request, id):
    category = get_object_or_404(Category, pk=id)
    form = CategoryForm(instance=category)
    if request.method == "POST":
        form = CategoryForm(request.POST or None, instance=category)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect("/categories/")
    return render(request, 'category/edit.html', {
        'form': form
    })

@login_required
def delete(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        product.delete()
        return redirect("/products/")
    return render(request, 'products/delete.html', {
        "product": product
    })


@login_required
def delete_category(request, id):
    category = get_object_or_404(Category, pk=id)
    if request.method == "POST":
        category.delete()
        return redirect("/categories/")
    return render(request, 'category/delete.html', {
        "category": category
    })