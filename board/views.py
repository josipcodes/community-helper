from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Task, User, Category, Comment
from .forms import TaskForm, CommentForm



# renders index.html
def home(request):
    # below logic was taken (but custoomized) from:
    # https://www.learningaboutelectronics.com/Articles/
    # How-to-count-all-objects-of-a-database-table-in-Django.php
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
            # decide if this is a good practice + there is no direct confirmation to the user
            # return redirect('home')
            return get_task_list(request)
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
    if request.method == "POST":
        # below lines are a customized code obtained here:
        # https://www.youtube.com/watch?v=zJWhizYFKP0
        task.helper = request.user
        task.status = "Ongoing"
        task.save()
        # return render(request, "show_ongoing_task.html", context)
        return show_ongoing_task(request, task_id)
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
    context = {'form': form}
    return render(request, "edit_task.html", context)


def delete_task(request, task_id):
    current_user = request.user
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        if current_user == task.owner:
            task.delete()
            return list_own_tasks(request)
    context = {'task': task}
    return render(request, "delete_task.html", context)


def list_own_tasks(request):
    current_user = request.user
    # below filtering by using status__in adopted from:
    # https://copyprogramming.com/howto/django-filter-multiple-values
    own_tasks = Task.objects.filter(owner=current_user).filter(
        status__in=["Published", "Ongoing"]
        )
    helper_tasks = Task.objects.filter(helper=current_user, status="Ongoing")
    context = {
        'current_user': current_user,
        'own_tasks': own_tasks,
        'helper_tasks': helper_tasks
    }
    return render(request, "list_own_tasks.html", context)


def show_ongoing_task(request, task_id):
    form = CommentForm()
    task = get_object_or_404(Task, id=task_id)
    # comment = get_object_or_404(Comment, post=task)
    # comments = Comment.objects.filter(post=task)
    comments = task.comments.all()
    current_user = request.user
    context = {
            'id': task_id,
            'task': task,
            'form': form,
            'comments': comments,
        }
    if request.method == "POST":
        # if request.POST["comment"] == "comment":
        form = CommentForm(request.POST)
        print(form)
        if form != None:
            # below lines are a customized code obtained here:
            # https://www.youtube.com/watch?v=zJWhizYFKP0
            instance = form.save(commit=False)
            if form.is_valid():
                instance.author = request.user
                instance.post = task
                instance.save()
                context = {
                    'id': task_id,
                    'task': task,
                    'form': form,
                    "comments": comments,
                }
                return render(request, "show_ongoing_task.html", context)
        else:
            if current_user == task.owner:
            # below lines are a customized code obtained here:
            # https://www.youtube.com/watch?v=zJWhizYFKP0
                task.status = "Archived"
                task.save()
            # return render(request, "show_ongoing_task.html", context)
                return list_own_tasks(request)
            
    return render(request, "show_ongoing_task.html", context)


def filter_category(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    if request.method == "POST":
        published_tasks = Task.objects.filter(status="Published")
        filtered_category = request.POST.get("category-filter")
        if filtered_category != "Choose Task Category":
            filtered_tasks = published_tasks.filter(category=filtered_category)
            context = {
                "categories": categories,
                "filtered_tasks": filtered_tasks
            }
            return render(request, "filter_category.html", context)
    return render(request, "filter_category.html", context)