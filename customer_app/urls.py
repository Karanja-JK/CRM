from django.urls import include, path
from customer_app import views

urlpatterns = [   
    path('', views.home, name='dashboard'),
    path('products/', views.products, name='products'),
    path('customers/', views.customers, name='customers'),
]