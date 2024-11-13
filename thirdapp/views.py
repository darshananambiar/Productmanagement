from django.shortcuts import render
from .models import User

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
    return render(request, 'thirdapp\home.html')
