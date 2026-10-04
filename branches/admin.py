from django.contrib import admin
from .models import Branch


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ["name", "city", "phone", "manager", "is_active"]
    list_filter = ["is_active", "city"]
    search_fields = ["name", "city", "address"]
