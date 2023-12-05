from django.forms import ModelForm
from .models import Task, Comment

# TaskForm class
class TaskForm(ModelForm):
    # meta class
    class Meta:
        # model used
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
    # meta class
    class Meta:
        # model used
        model = Comment
 
        # fields used
        fields = [
            "message",
        ]

