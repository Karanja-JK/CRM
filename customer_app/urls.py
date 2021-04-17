from django.urls import include, path
from customer_app import views

urlpatterns = [   
    
    # user profile links
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('user/', views.userPage, name='user-page'),
    
    # menu bar links
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customers/<int:pk>/', views.customers, name='customers'),
    
    # crud links
    path('create_order/<str:pk>/', views.createOrder, name='create_order'),
    path('update_order/<int:pk>/', views.updateOrder, name='update_order'),
    path('delete_order/<int:pk>/', views.deleteOrder, name='delete_order'),
    
]