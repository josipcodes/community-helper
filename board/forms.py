from django.forms import ModelForm
from .models import Task, Comment

# TaskForm class
class TaskForm(ModelForm):
    class Meta:
        model = Task
        # fields used
        fields = [
            "title",
            "description",
            "category",
            # "final_date",
        ]


# CommentForm class
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        # fields used
        fields = [
            "message",
        ]

