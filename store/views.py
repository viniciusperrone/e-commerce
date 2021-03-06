from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item
from .form import ItemForm

def create_product(request):
    return render(request, 'create_product.html')

def about_us(request):
    return render(request, 'about-us.html')
    
def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'home-page.html', context=context)

def checkout(request):
    return render(request, 'checkout.html')

def product(request, id):
    product = Item.objects.get(id=id)
    context = {
        'item': product
    }
    return render(request, 'product.html', context=context)