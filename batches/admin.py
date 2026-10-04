from django.contrib import admin
from .models import Batch


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ["name", "branch", "course", "faculty", "start_date", "is_active"]
    list_filter = ["branch", "course", "is_active"]
    search_fields = ["name", "branch__name", "course__name"]
