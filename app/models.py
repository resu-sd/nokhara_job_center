from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField
from django.utils.text import slugify
# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=10, unique=True,null=True, blank=True)

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
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES)
    salary_range = models.CharField(max_length=100, blank=True)
    description = HTMLField()
    expiry_date = models.DateField()
    views_count = models.PositiveIntegerField(default=0)
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
    


class JobSeekerApplication(models.Model):
    full_name = models.CharField(max_length=100)
    cv = models.FileField(upload_to='cvs/')
    phone = models.CharField(max_length=10)
    address = models.TextField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.job.title}"
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug= models.SlugField(unique=True,blank=True)
    color = models.CharField(max_length=7, default='#FF0000', help_text='color name or Hex color code, e.g. #FF0000 or red')
    icon_class = models.CharField(max_length=100, blank=True, help_text='FontAwesome icon classname only, e.g. book, pen')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Categories"