from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'visitor/home.html')


def register(request):
      return render(request, "visitor/register.html")

def detail(request):
     return render(request,"detail.html")


def faq(request):
     return render(request,"faq.html")


def login(request):
     return render(request,"login.html")

def search(request):
     return render(request,'visitor/search.html')


def post_job(request):
     return render(request,'post_job.html')