from django.contrib import admin
from .models import Admission


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ["student", "batch", "status", "payment_status", "admission_date"]
    list_filter = ["status", "payment_status"]
    search_fields = ["student__username", "batch__name"]
