from django.shortcuts import render, redirect
from .models import Task, User
from .forms import TaskForm



# renders index.html
def home(request):
    # below logic was taken (but custoomized) from:
    # https://stackoverflow.com/questions/53243835/django-how-to-display-number-of-items
    published_tasks = Task.objects.filter(status="Published")
    archived_tasks = Task.objects.filter(status="Archived")
    total_published = published_tasks.count()
    total_archived = archived_tasks.count()
    total_users = User.objects.count()
    # context contains total number of published and archived tasks, users
    context = {
        'total_published': total_published,
        'total_archived': total_archived,
        'total_users': total_users,
    }
    return render(request, "index.html", context)

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


# def total_tasks(request):
#     count_of_tasks = Task.objects.all().count()
#     context = {
#         'count_of_tasks': count_of_tasks
#     }
#     return render(request, "index.html", context)




