from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    context = {
        'customers': Customer.objects.all(),
        'orders': Order.objects.all(),
        'total_orders': Order.objects.count(),
        'total_customers': Customer.objects.count(),
        'delivered': Order.objects.filter(status='Delivered').count(),
        'pending': Order.objects.filter(status='Pending').count()
        
    }
    return render(request, 'customer_app/dashboard.html', context)


def products(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'customer_app/products.html', context)


def customers(request):

    return render(request, 'customer_app/customers.html')