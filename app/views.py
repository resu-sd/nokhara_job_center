from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from .models import Review
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()

def home(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        full_name = request.POST.get("full_name")
        profession = request.POST.get("profession")
        if comment and full_name:
            Review.objects.create(
                comment=comment,
                full_name=full_name,
                profession=profession
            )
            return redirect('home')  

   
    reviews = Review.objects.all()
    return render(request, "visitor/home.html", {"reviews": reviews})

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        
        if not (phone.startswith("97") or phone.startswith("98")) or len(phone) != 10:
            messages.error(request, "Invalid phone number")
            return redirect("register")

      
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("register")

        if User.objects.filter(phone=phone).exists():
            messages.error(request, "Phone number already exists")
            return redirect("register")

       
        user = User.objects.create_user(
            username=username,
           email=email,
            phone=phone,
             password=password)

        messages.success(request, "Account created successfully")
        return redirect("login")

    return render(request, "visitor/register.html")

def detail(request):
     return render(request,"detail.html")


def faq(request):
     return render(request,"faq.html")

def login_view(request):
    if request.method == "POST":
        identifier = request.POST.get("username_or_email")
        password = request.POST.get("password")
        user = authenticate(request, username=identifier, password=password)

        
        if user is None:
            try:
                u = User.objects.get(email=identifier)
                user = authenticate(request, username=u.username, password=password)
            except User.DoesNotExist:
                user = None

        if user:
            auth_login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username/email or password")

    return render(request, "visitor/login.html")

def logout_view(request):
    logout(request)
    return redirect('home')

        


def search(request):
     return render(request,'visitor/search.html')


def post_job(request):
     return render(request,'post_job.html')