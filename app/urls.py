from django.urls import path
from .views import home,register,detail,faq,login,search,post_job


urlpatterns = [
    path('', home, name='home'),
  path("register/", register, name="register"),
  path("detail/",detail,name="detail"),
  path("faq/",faq,name="faq"),
  path("register/",register,name="register"),
  path("login/",login,name='login'),
  path("search/",search,name='search'),
  path("post_job",post_job,name='post_job')
  
]