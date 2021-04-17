from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.http import HttpResponse
from .models import *
from .forms import OrderForm, CreateUserForm
from .filter import OrderFilter
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user


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
    myFilter = OrderFilter(request.GET, queryset = orders)
    orders = myFilter.qs
    context = {'customer':customer, 'orders':orders, 'orders_count':orders_count, 'myFilter':myFilter}

    return render(request, 'customer_app/customers.html', context)


# Create Order
def createOrder(request, pk):
    
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        #form = OrderForm(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset':formset}
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


# register view
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account successful for' + user)
            return redirect('login')
    
    context = {'form': form}
    return render(request, 'customer_app/register.html', context)


# login view
@unauthenticated_user
def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect!')
    
    context = {}
    return render(request, 'customer_app/login.html', context)


# logout view
def logoutPage(request):
    logout(request)
    return redirect('login')


# user page
def userPage(request):
    context = {}
    return render(request, 'customer_app/user.html', context)
    