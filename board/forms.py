from django import forms
from django.forms import ModelForm
from .models import Task, Comment

# TaskForm class
class TaskForm(ModelForm):
    class Meta:
        model = Task
        # fields used
        fields = [
            'title',
            'description',
            'category',
            'final_date',
        ]

        labels = {
            'title': 'Task Title',
            'description': 'Description of your task',
            'category': 'Category',
            'final_date': 'Deadline',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the Title'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter the Description'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            # datepicker created with the help of below:
            # https://stackoverflow.com/questions/
            # 3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django
            'final_date': forms.widgets.DateInput(attrs={'class':'form-control', 'type': 'date'})
        }


# CommentForm class
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        # fields used
        fields = [
            'message',
        ]

        labels = {
            'message': '',
        }

        widgets = {
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter a Comment'}),
        }
