from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm




def home(request):
    return render(request, "index.html")


def new_task(request):
    if request.method == "POST":
        # form = TaskForm(request.POST)
        # if form.is_valid():
        #     form.save()

        title = request.POST.get('task-title')
        description = request.POST.get('task-description')
        category = request.POST.get('category')
        final_date = request.POST.get('deadline')        
        Task.objects.create(title=title, description=description, category=category, final_date=final_date)
        return redirect('home')
    form = TaskForm()
    context = {
        "form": form
    }
    return render(request, "create-task.html")




