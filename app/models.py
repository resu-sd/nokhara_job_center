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
    

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
        ('Remote', 'Remote'),
    ]

 
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES)
    salary_range = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    expiry_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class JobRequirement(models.Model):
     job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='requirements')
     text = models.CharField(max_length=255)

     def __str__(self):
        return self.text


class JobBenefit(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='benefits')
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text