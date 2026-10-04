from django.db import models


class Course(models.Model):
    DANCE_STYLE_CHOICES = [
        ("bharatanatyam", "Bharatanatyam"),
        ("kathak", "Kathak"),
        ("odissi", "Odissi"),
        ("kuchipudi", "Kuchipudi"),
        ("manipuri", "Manipuri"),
        ("mohiniyattam", "Mohiniyattam"),
        ("folk_dance", "Folk Dance"),
        ("contemporary", "Contemporary"),
        ("hip_hop", "Hip Hop"),
        ("bollywood", "Bollywood"),
    ]

    LEVEL_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
        ("professional", "Professional"),
    ]

    name = models.CharField(max_length=200)
    dance_style = models.CharField(max_length=50, choices=DANCE_STYLE_CHOICES)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    description = models.TextField()
    duration_months = models.PositiveIntegerField(default=3)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    syllabus = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"
