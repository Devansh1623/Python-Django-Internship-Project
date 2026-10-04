from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ("super_admin", "Super Admin"),
        ("admin", "Admin"),
        ("manager", "Manager"),
        ("faculty", "Faculty"),
        ("student", "Student"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="student")
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"

    def is_super_admin(self):
        return self.role == "super_admin"

    def is_admin_role(self):
        return self.role in ["super_admin", "admin"]

    def is_manager(self):
        return self.role == "manager"

    def is_faculty(self):
        return self.role == "faculty"

    def is_student(self):
        return self.role == "student"
