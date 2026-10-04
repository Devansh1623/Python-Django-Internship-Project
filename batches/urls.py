from django.urls import path
from . import views

urlpatterns = [
    path("", views.batch_list, name="batch_list"),
    path("create/", views.batch_create, name="batch_create"),
    path("edit/<int:pk>/", views.batch_edit, name="batch_edit"),
    path("delete/<int:pk>/", views.batch_delete, name="batch_delete"),
]
