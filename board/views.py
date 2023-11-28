from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Task, User
from .forms import TaskForm



# renders index.html
def home(request):
    # below logic was taken (but custoomized) from:
    # https://www.learningaboutelectronics.com/Articles/How-to-count-all-objects-of-a-database-table-in-Django.php
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
    return render(request, "create_task.html", context)


def get_task_list(request):
    task_list = Task.objects.filter(status="Published")
    # paginator logic copied from:
    # https://docs.djangoproject.com/en/4.2/topics/pagination/
    paginator = Paginator(task_list, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'task_list': task_list,
        "page_obj": page_obj
    }
    return render(request, "list_tasks.html", context)


def show_task(request, task_id):
    current_user = request.user
    task = get_object_or_404(Task, id=task_id)
    context = {
        'id': task_id,
        'task': task
    }
    return render(request, "show_task.html", context)


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect(show_task, task_id)
    context = {
        'form': form
    }
    return render(request, "edit_task.html", context)


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect(home)


def list_own_tasks(request):
    current_user = request.user
    own_tasks = Task.objects.filter(owner=current_user)
    context = {
        'current_user': current_user,
        'own_tasks': own_tasks
    }
    return render(request, "list_own_tasks.html", context)
