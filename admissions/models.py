from django.db import models
from django.conf import settings


class Admission(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("active", "Active"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="admissions",
    )
    batch = models.ForeignKey(
        "batches.Batch",
        on_delete=models.CASCADE,
        related_name="admissions",
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    admission_date = models.DateField(auto_now_add=True)
    approval_date = models.DateField(null=True, blank=True)
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="approved_admissions",
    )
    payment_status = models.CharField(
        max_length=20,
        choices=[("unpaid", "Unpaid"), ("partial", "Partial"), ("paid", "Paid")],
        default="unpaid",
    )
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["student", "batch"]

    def __str__(self):
        return f"{self.student.get_full_name()} - {self.batch.name}"
