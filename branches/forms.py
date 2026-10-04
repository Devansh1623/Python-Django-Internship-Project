from django import forms
from .models import Branch


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ["name", "address", "city", "phone", "email", "manager", "is_active"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-input", "placeholder": "Branch Name"}),
            "address": forms.Textarea(attrs={"class": "form-input", "rows": 3, "placeholder": "Full Address"}),
            "city": forms.TextInput(attrs={"class": "form-input", "placeholder": "City"}),
            "phone": forms.TextInput(attrs={"class": "form-input", "placeholder": "+91 XXXXXXXXXX"}),
            "email": forms.EmailInput(attrs={"class": "form-input", "placeholder": "branch@example.com"}),
            "manager": forms.Select(attrs={"class": "form-select"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
        }
