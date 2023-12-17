from django import forms
from django.forms import ModelForm
from .models import Task, Comment, Profile


class TaskForm(ModelForm):
    '''
    Task form class with fields, labels and widgets
    '''
    class Meta:
        model = Task

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


class CommentForm(ModelForm):
    '''
    Comment form class with a field, label and a widget
    '''
    class Meta:
        model = Comment

        fields = [
            'message',
        ]

        labels = {
            'message': '',
        }

        widgets = {
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter a Comment'}),
        }


class ProfileForm(ModelForm):
    '''
    Profile form class with a fields, labels and widgets
    '''
    class Meta:
        model = Profile

        # We are not using person as it's a foreign key pointing to a User.
        # instead of removing person, I've decided that it's wiser to list needed fields.
        fields = [
            'name',
            'surname',
            'address',
            'location',
            'city',
            'country',
        ]

        labels = {
            'name': 'First Name',
            'surname': 'Last Name',
            'address': 'Address',
            'city': 'City',
            'location': 'General location',
            'country': 'Country',
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Name'}),
            'surname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Last Name'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Address'}),
            'city': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your City'}),
            'location': forms.TextInput(attrs={
                'class':'form-control', 
                'placeholder':'Your General Location; this will be visible to all potential helpers'}),
            'country': forms.Select(attrs={'class':'form-control'}),
        }