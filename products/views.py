from django.shortcuts import render

from products.models import Product

# Create your views here.
def show_products(request):
    products = Product.objects.all()
    return render(request, 'products/show_products.html', {'products': products})


def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'products/product_details.html', {'product': product})


def show_food(request, category):
    category_first_letter_upper = category[:1].upper() + category[1:]
    products = Product.objects.filter(category=category_first_letter_upper)
    return render(request, 'products/show_products.html', {'products': products, 'category': category})


def show_non_food(request, category):
    category_first_letter_upper = category[:1].upper() + category[1:]
    products = Product.objects.filter(category=category_first_letter_upper)
    return render(request, 'products/show_products.html', {'products': products, 'category': category})
