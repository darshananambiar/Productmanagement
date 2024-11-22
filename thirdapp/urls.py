from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.signup, name='signup'),
    path('home/',views.home, name='home'),
    path('logout/',views.logout,name='logout'),
    path('addproduct',views.addproduct, name='addproduct'),
    path('products/<int:pid>',views.product_details, name='products'),
    path('addcategory/',views.addcategory ,name='addcategory')

    
]
