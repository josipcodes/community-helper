from django.forms import ModelForm
from .models import Task

# TaskForm class
class TaskForm(ModelForm):
    # meta class
    class Meta:
        # model used
        model = Task
        # category = forms.ModelChoice(queryset=Category.objects.all())
 
        # fields used
        fields = [
            "title",
            "description",
            "category",
            "final_date",
        ]

        