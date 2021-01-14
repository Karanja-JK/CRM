from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm


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


def customers(request, pk):
    
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    context = {'customer':customer, 'orders':orders, 'orders_count':orders_count}

    return render(request, 'customer_app/customers.html', context)


def createOrder(request):
    
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request, 'customer_app/order_form.html', context)


# Update Order
def updateOrder(request, pk):
    
    order = Order.objects.get(id=pk) 
    form = OrderForm(instance=order) # ensures the form is auto-filled
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
    if form.is_valid():
        form.save()
        return redirect('/')
    
    context = {'form':form}
    return render(request, 'customer_app/order_form.html', context)


# Delete Order
def deleteOrder(request, pk):
    
   order = Order.objects.get(id=pk) 
   if request.method == 'POST':
       order.delete()
       return redirect('/')
   
   context = {'item':order}
   return render(request, 'customer_app/delete.html', context)
    