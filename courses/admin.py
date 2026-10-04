from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "dance_style", "level", "fee", "duration_months", "is_active"]
    list_filter = ["dance_style", "level", "is_active"]
    search_fields = ["name", "description"]
