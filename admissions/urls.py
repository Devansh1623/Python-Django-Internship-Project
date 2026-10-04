from django.urls import path
from . import views

urlpatterns = [
    path("", views.admission_list, name="admission_list"),
    path("apply/", views.admission_apply, name="admission_apply"),
    path("approve/<int:pk>/", views.admission_approve, name="admission_approve"),
    path("reject/<int:pk>/", views.admission_reject, name="admission_reject"),
]
