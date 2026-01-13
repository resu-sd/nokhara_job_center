from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Review,User
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
