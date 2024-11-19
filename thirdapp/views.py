from django.shortcuts import render, redirect
from .models import Product, User

# Create your views here.
def login(request):
    if 'user_id' in request.session:
        return redirect ('home')
    
    message=''
    if request.method == 'POST':
        email = request.POST['email'] 
        password = request.POST['password']
        user = User.objects.filter(email=email, password=password).first()
        if user:
            request.session['user_id']=user.id
            request.session['user_name']=user.email
            return render (request,'thirdapp/home.html',{'user':user})
        else :
            message='Invalid username or password'
    return render(request, 'thirdapp\login.html',{'message':message})
def logout (request):
    if 'user_id' in request.session:
        del request.session['user_id']
        del request.session['user_name']
        return redirect('login')

    

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
        "image": "images/laptop.jpeg"
    },
    {
        "product_id": 2,
        "name": "Smartphone",
        "description": "5G enabled smartphone with 128GB storage and 48MP camera",
        "price": 799.99,
        "quantity": 50,
         "image": "images/smartphne.jpeg"
    },
    {
        "product_id": 3,
        "name": "Bluetooth Speaker",
        "description": "Portable Bluetooth speaker with 24-hour battery life",
        "price": 49.99,
        "quantity": 100,
         "image": "images/speaker.jpeg"
    },
    {
        "product_id": 4,
        "name": "Smartwatch",
        "description": "Fitness smartwatch with heart rate monitor and GPS",
        "price": 199.99,
        "quantity": 30,
         "image": "images/smartwatch.jpeg"
    },
    {
        "product_id": 5,
        "name": "Wireless Earbuds",
        "description": "Noise-canceling wireless earbuds with charging case",
        "price": 129.99,
        "quantity": 80,
         "image": "images/earbuds2.jpeg"
    }
    ]
    return render(request, 'thirdapp/home.html',{'productslist' : product_list})

def addproduct(request):
    message = ""
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        quantity = request.POST['quantity']
        image = request.FILES['image']

        product_exist = Product.objects.filter(name = name).exists()
        if product_exist:
            message = "Product already exists!"

        else:
            product = Product(name=name, description=description, price=price, quantity=quantity, image=image)
            product.save()
            message = "Product added successfully!"
            
    return render(request, 'thirdapp/addproduct.html',{'message':message})
