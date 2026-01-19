from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Review,User,Job,JobBenefit,JobRequirement,JobSeekerApplication,Category
admin.site.register(Review)
class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields', {'fields': ('phone',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Fields', {'fields': ('phone',)}),
    )

admin.site.register(User, CustomUserAdmin)

from django.contrib import admin
from .models import Job, JobRequirement, JobBenefit


class JobRequirementInline(admin.TabularInline):
    model = JobRequirement
    extra = 0


class JobBenefitInline(admin.TabularInline):
    model = JobBenefit
    extra = 0


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'location',
        'job_type',
        'category',
        'expiry_date',
        'views_count',
        'created_at',
    )
    list_filter = ('job_type', 'category', 'created_at', 'expiry_date')
    search_fields = ('title', 'location', 'description')
    date_hierarchy = 'created_at'
    inlines = [JobRequirementInline, JobBenefitInline]


@admin.register(JobRequirement)
class JobRequirementAdmin(admin.ModelAdmin):
    list_display = ('text', 'job')
    search_fields = ('text',)


@admin.register(JobBenefit)
class JobBenefitAdmin(admin.ModelAdmin):
    list_display = ('text', 'job')
    search_fields = ('text',)

admin.site.register(JobSeekerApplication)
admin.site.register(Category)
