from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'visitor/home.html')


def register(request):
      return render(request, "visitor/register.html")

