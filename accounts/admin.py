from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ["username", "email", "role", "is_active", "date_joined"]
    list_filter = ["role", "is_active"]
    search_fields = ["username", "email", "first_name", "last_name"]
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("role", "phone", "address", "date_of_birth", "profile_picture")}),
    )
