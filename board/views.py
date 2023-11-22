from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm




def home(request):
    return render(request, "index.html")

# @login_required(login_url="")
def new_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        # below lines are a customized code obtained here:
        # https://www.youtube.com/watch?v=zJWhizYFKP0
        instance = form.save(commit=False)
        if form.is_valid():
            instance.owner = request.user
            instance.status = "Published"
            instance.save()
            return redirect('home')
    context = {'form': form}
    return render(request, "create-task.html", context)


def get_task_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, "list_tasks.html", context)




