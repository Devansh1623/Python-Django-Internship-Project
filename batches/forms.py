from django import forms
from .models import Batch


class BatchForm(forms.ModelForm):
    days = forms.MultipleChoiceField(
        choices=Batch.DAYS_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-checkbox"}),
        help_text="Hold Ctrl/Cmd to select multiple days"
    )

    class Meta:
        model = Batch
        fields = [
            "name", "branch", "course", "faculty",
            "start_date", "end_date", "start_time", "end_time",
            "days", "max_students", "is_active",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-input", "placeholder": "Batch Name"}),
            "branch": forms.Select(attrs={"class": "form-select"}),
            "course": forms.Select(attrs={"class": "form-select"}),
            "faculty": forms.Select(attrs={"class": "form-select"}),
            "start_date": forms.DateInput(attrs={"class": "form-input", "type": "date"}),
            "end_date": forms.DateInput(attrs={"class": "form-input", "type": "date"}),
            "start_time": forms.TimeInput(attrs={"class": "form-input", "type": "time"}),
            "end_time": forms.TimeInput(attrs={"class": "form-input", "type": "time"}),
            "max_students": forms.NumberInput(attrs={"class": "form-input", "min": 1}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
        }
