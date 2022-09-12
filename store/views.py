from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
# Create your views here.


def store(request, category_slug=None):
    # Se ejecuta en el archivo store.urls
    # Requiere un parametro category_slug para poder filtrar los productos por categorias
    
    categories = None
    products = None 
    
    # Si hay un slug en la url:
    # categories guarda el objeto de la categoria segun el slug , caso contrario devuelve error 404
    # Si no hay slug lista todos los articulos del
    # products_count alamacena la cantidad de articulos listados
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products= Product.objects.all().filter(is_available=True)
        product_count = products.count()
    
    # Contexto que se pasa al template
    context = {
        'products': products,
        'product_count': product_count
    }
    
    return render(request, 'store/store.html', context)



def product_detail(request, category_slug, product_slug):
    
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    
    context = {
        'product': product,
    }
    
    return render(request, 'store/product_detail.html', context)