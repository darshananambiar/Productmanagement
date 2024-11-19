from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import logout
# Create your views here.
def login(request):
    return render(request, 'thirdapp\login.html')

def signup(request):
    message=""
    if request.method == 'POST' :
        email = request.POST.get('email')
        password = request.POST.get('password')

        userexist = User.objects.filter(email=email, password=password).exists()

        if userexist:
            message="user already registered"
        else:
            user = User(email=email,password=password)
            user.save()
            message ="user registered successsfully"
    
    return render(request, 'thirdapp\signup.html',{'message':message})

def home(request):
    product_list = [
    {
        "product_id": 1,
        "name": "Laptop",
        "description": "High-performance laptop with Intel i7 processor, 16GB RAM, 512GB SSD",
        "price": 1099.99,
        "quantity": 15,
        "image": "images/laptop.avif"
    },
    {
        "product_id": 2,
        "name": "Smartphone",
        "description": "5G enabled smartphone with 128GB storage and 48MP camera",
        "price": 799.99,
        "quantity": 50,
         "image": "images/mobile.avif"
    },
    {
        "product_id": 3,
        "name": "Neckchain",
        "description": "Portable Bluetooth speaker with 24-hour battery life",
        "price": 49.99,
        "quantity": 100,
         "image": "images/neckchain.avif"
    },
    {
        "product_id": 4,
        "name": "Smarttv",
        "description": "Fitness smartwatch with heart rate monitor and GPS",
        "price": 199.99,
        "quantity": 30,
         "image": "images/tv.avif"
    },
    {
        "product_id": 5,
        "name": "Washingmachine",
        "description": "Noise-canceling wireless earbuds with charging case",
        "price": 129.99,
        "quantity": 80,
         "image": "images/washing machine.avif"
    },
    {
        "product_id": 6,
        "name": "smartwatch",
        "description": "Noise-canceling wireless earbuds with charging case",
        "price": 129.99,
        "quantity": 80,
         "image": "images/smartwatch.avif"
    },
    {
        "product_id": 7,
        "name": "Bracelet",
        "description": "Noise-canceling wireless earbuds with charging case",
        "price": 129.99,
        "quantity": 80,
         "image": "images/bracelet.avif"
    },
    {
        "product_id": 7,
        "name": "Makeupset",
        "description": "Noise-canceling wireless earbuds with charging case",
        "price": 129.99,
        "quantity": 80,
         "image": "images/makeup.avif"
    }
    ]
    return render(request, 'thirdapp/home.html',{'productslist' : product_list})



def logout_view(request):
    logout(request)
    return redirect('home')