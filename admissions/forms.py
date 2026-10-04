from django import forms
from .models import Admission


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ["batch", "notes"]
        widgets = {
            "batch": forms.Select(attrs={"class": "form-select"}),
            "notes": forms.Textarea(attrs={"class": "form-input", "rows": 3, "placeholder": "Any special requirements..."}),
        }
