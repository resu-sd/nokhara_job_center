from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from .models import Review,Job,JobRequirement,JobBenefit
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
    recent_jobs = Job.objects.order_by('-id')[:5]
    context = {
        "reviews": reviews,
        "recent_jobs": recent_jobs
    }

    return render(request, "visitor/home.html", context)

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

def detail(request, job_id):
    # Fetch job or 404 if not found
    job = get_object_or_404(Job, id=job_id)

    # Fetch requirements and benefits
    requirements = JobRequirement.objects.filter(job=job)
    benefits = JobBenefit.objects.filter(job=job)

    return render(request, "detail.html", {
        "job": job,
        "requirements": requirements,
        "benefits": benefits,
    })


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
    
    if request.method == "POST":
        title = request.POST.get('jobTitle')
        location = request.POST.get('location')
        job_type = request.POST.get('jobType')
        salary = request.POST.get('salaryRange')
        expiry_date = request.POST.get('expiryDate')
        description = request.POST.get('jobDescription')

        job = Job.objects.create(
         
            title=title,
            location=location,
            job_type=job_type,
            salary_range=salary,
            expiry_date=expiry_date,
            description=description
        )

       
        requirements = request.POST.getlist('requirements[]')
        for req in requirements:
            if req.strip():
                JobRequirement.objects.create(job=job, text=req)

      
        benefits = request.POST.getlist('benefits[]')
        for ben in benefits:
            if ben.strip():
                JobBenefit.objects.create(job=job, text=ben)

        messages.success(request, "Job posted successfully!")
        return redirect('post_job')

    return render(request, 'post_job.html')
  