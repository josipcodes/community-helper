from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Task, User, Category, Comment, Profile
from .forms import TaskForm, CommentForm, ProfileForm
from datetime import datetime


# renders index.html within base
def home(request):
    # below logic was taken (but customized) from:
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


@login_required
def new_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        # below lines are a customized code obtained here:
        # https://www.youtube.com/watch?v=zJWhizYFKP0
        instance = form.save(commit=False)
        if form.is_valid():
            # instance saves owner and changes status
            instance.owner = request.user
            instance.status = "Published"
            instance.save()
            return list_own_tasks(request)
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


@login_required
def show_task(request, task_id):
    current_user = request.user
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        # below lines are a customized code obtained here:
        # https://www.youtube.com/watch?v=zJWhizYFKP0#
        # task saves user as helper, changes status
        task.helper = request.user
        task.status = "Ongoing"
        task.save()
        return show_ongoing_task(request, task_id)
    context = {
        'id': task_id,
        'task': task
    }
    return render(request, "show_task.html", context)


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        instance = form.save(commit=False)
        if form.is_valid():
            instance.updated_date = datetime.now()
            instance.save()
        return redirect(show_task, task_id)
    context = {'form': form}
    return render(request, "edit_task.html", context)


@login_required
def delete_task(request, task_id):
    current_user = request.user
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        if current_user == task.owner:
            task.delete()
            return list_own_tasks(request)
    context = {'task': task}
    return render(request, "delete_task.html", context)


@login_required
def list_own_tasks(request):
    current_user = request.user
    # below filtering by using status__in adopted from:
    # https://copyprogramming.com/howto/django-filter-multiple-values
    # filter for Published and Ongoing tasks
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


@login_required
def show_ongoing_task(request, task_id):
    form = CommentForm()
    task = get_object_or_404(Task, id=task_id)
    comments = task.comments.all()
    current_user = request.user
    context = {
            'id': task_id,
            'task': task,
            'form': form,
            'comments': comments,
        }
    if request.method == "POST":
        form = CommentForm(request.POST)
            # below lines are a customized code obtained here:
            # https://www.youtube.com/watch?v=zJWhizYFKP0
        instance = form.save(commit=False)
        if form.is_valid():
            # instance saves comment author and associated task
            instance.author = request.user
            instance.post = task
            instance.save()
            form = CommentForm()
            context = {
                'id': task_id,
                'task': task,
                'form': form,
                "comments": comments,
            }
            return render(request, "show_ongoing_task.html", context)
    return render(request, "show_ongoing_task.html", context)


@login_required
def archive_task(request, task_id):
    current_user = request.user
    task = get_object_or_404(Task, id=task_id)
    context = {
        "task": task,
        "id": task_id
    }
    if request.method == "POST":
        if current_user == task.owner:
            # status change
            task.status = "Archived"
            task.save()
            return list_own_tasks(request)
    return render(request, "archive_task.html", context)


@login_required
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
            # used to render back-up button if more than 3 tasks exist
            filtered_tasks_count = filtered_tasks.count()
            context = {
                "categories": categories,
                "filtered_tasks": filtered_tasks,
                "filtered_tasks_count": filtered_tasks_count
            }
            return render(request, "filter_category.html", context)
    return render(request, "filter_category.html", context)



# @login_required
# def view_profile(request, user_id):
#     current_user = request.user
#     user = get_object_or_404(User, id=current_user.id)
#     profile = Profile.objects.filter(person=user)
#     context = {
#         "user.id": user.id,
#         "profile": profile,
#     }
#     return render(request, "view_profile.html", context)


def create_profile(request, user_id):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        instance = form.save(commit=False)
        if form.is_valid():
            instance.person = request.user
            instance.save()
            return view_profile(request, user_id)
    context = {
        "user.id": user_id,
        'form': form
        }
    return render(request, "create_profile.html", context)


# user can currently access anyone's profile
@login_required
def edit_profile(request, user_id):
    current_user = request.user
    profile = get_object_or_404(Profile, id=user_id)
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        # below lines are a customized code obtained here:
        # https://www.youtube.com/watch?v=zJWhizYFKP0
        if form.is_valid():
            form.save()
            form = ProfileForm(instance=profile)
            context = {
                "form": form,
                "user_id": current_user.id
            }
            return render(request, "edit_profile.html", context)
    context = {
        "form": form,
    }
    return render(request, "edit_profile.html", context)


# @login_required
# def edit_profile(request,):
#     current_user = request.user
#     try:
#         profile = get_object_or_404(Profile, id=user_id)
#         form = ProfileForm(instance=profile)
#         if request.method == "POST":
#             form = ProfileForm(request.POST, instance=profile)
#             # below lines are a customized code obtained here:
#             # https://www.youtube.com/watch?v=zJWhizYFKP0
#             if form.is_valid():
#                 form.save()
#                 form = ProfileForm(instance=profile)
#                 context = {
#                     "form": form,
#                     "user_id": current_user.id
#                 }
#                 return render(request, "edit_profile.html", context)
#         context = {
#         "form": form,
#                 }
#         return render(request, "edit_profile.html", context)
#     except:
#         return create_profile(request, user_id)