from django import forms
from .models import Task

# TaskForm class
class TaskForm(forms.ModelForm):
    # meta class
    class Meta:
        # model used
        model = Task
 
        # fields used
        fields = [
            "title",
            "description",
            "category",
            "final_date",
        ]

        