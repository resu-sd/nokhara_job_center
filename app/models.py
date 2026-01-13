from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
   
    phone = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.username
    



class Review(models.Model):
    full_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField()
    
    

    def __str__(self):
        return f"{self.full_name} "