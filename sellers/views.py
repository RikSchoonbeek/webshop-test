from django.shortcuts import render

from sellers.models import Seller


def sellers(request):
    sellers = Seller.objects.order_by('username')
    return render(request, 'sellers.html', {'sellers': sellers})


def seller_details(request, id):
    seller = Seller.objects.get(id=id)
    return render(request, 'seller_details.html', {'seller': seller})
