from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            "name", "dance_style", "level", "description",
            "duration_months", "fee", "syllabus", "is_active",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-input", "placeholder": "Course Name"}),
            "dance_style": forms.Select(attrs={"class": "form-select"}),
            "level": forms.Select(attrs={"class": "form-select"}),
            "description": forms.Textarea(attrs={"class": "form-input", "rows": 4, "placeholder": "Course description..."}),
            "duration_months": forms.NumberInput(attrs={"class": "form-input", "min": 1}),
            "fee": forms.NumberInput(attrs={"class": "form-input", "placeholder": "0.00", "step": "0.01"}),
            "syllabus": forms.Textarea(attrs={"class": "form-input", "rows": 4, "placeholder": "Syllabus outline..."}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
        }
