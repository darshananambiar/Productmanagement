from django.shortcuts import render, redirect
from .models import Product, User,Category
from django.db.models import Sum,Avg,Min,Max,Count
from django.db.models.functions import Lower, Upper,Length,Concat,Replace,Abs,Round
from django.core.paginator import Paginator

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
   
    # product_list = Product.objects.all().annotate(title = Upper('name'))
    # product_list = Product.objects.values('name','price','id')
    # product_list =Product.objects.filter(price__gt = 10000) .order_by('-price')
    # product_list =Product.objects.filter(name__icontains = 'neck')
    # product_list =Product.objects.filter(name__istartswith = 'w')
    # product_list =Product.objects.filter(name__iendswith = 'e')
    # product_list =Product.objects.filter(price__range =(5000 ,20000))
    total_price = Product.objects.aggregate(total=Sum("price"))
    avg_price= Product.objects.aggregate(average=Avg("price"))
    min_price= Product.objects.aggregate(min=Min("price"))
    max_price= Product.objects.aggregate(maximum=Max("price"))
    count_total= Product.objects.aggregate(counttotal=Count("price"))
    print ('totalprice', total_price)
    print ('averageprice',  avg_price)
    print ('minpriceprice', min_price)
    print ('maximumprice',  max_price)
    print ('count',  count_total)


    category_list=Category.objects.all()

    category=request.GET.get('category','all')
    if category=='all':
        product_list = Product.objects.all()
    else:
        product_list=Product.objects.filter(category_id=category)

    search_text=request.GET.get('serch_text','')
    if search_text:
        product_list=Product.objects.filter(name__icontains=search_text)

    paginator= Paginator(product_list, 8)
    page_number = request.GET.get('page')  # Default is None
    page_obj = paginator.get_page(page_number)

    context={
        'category_list':category_list,
        'productslist':page_obj,
        
       
    }
    return render(request, 'thirdapp/home.html',context)

def addproduct(request):
    category_list=Category.objects.all()
    message = ""
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']

        description = request.POST['description']
        price = request.POST['price']
        quantity = request.POST['quantity']
        image = request.FILES['image']

        product_exist = Product.objects.filter(name = name).exists()
        if product_exist:
            message = "Product already exists!"

        else:
            product = Product(name=name, description=description, price=price, quantity=quantity, image=image,category_id=category)
            product.save()
            message = "Product added successfully!"
            
    context={
        'category_list':category_list,
        'message':message,
    } 
    return render(request, 'thirdapp/addproduct.html',context)

def product_details(request,pid):
    product=Product.objects.get(id=pid)
    return render(request, 'thirdapp/productdetail.html',{'product':product})
    
def addcategory(request):
    message=""
    if request.method == 'POST':
        name=request.POST.get("name")
        description=request.POST.get("description")
        category,create=Category.objects.get_or_create(name=name,defaults={"name":name,"description":description})
        if create:
            message="Category added successfully"
        else:
            message="Category already exists"
    return render(request,"thirdapp/addcategory.html",{"message":message})
    
    

