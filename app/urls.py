from django.urls import path
from .views import home,register,detail,faq,search,post_job,login_view,logout_view


urlpatterns = [
    path('', home, name='home'),
  path("register/", register, name="register"),
  path("detail/",detail,name="detail"),
  path("faq/",faq,name="faq"),
  path("register/",register,name="register"),
  path("login_view/",login_view,name='login'),
  path("search/",search,name='search'),
  path("post_job",post_job,name='post_job'),
  path("logout_view",logout_view,name="logout_view")
  
]