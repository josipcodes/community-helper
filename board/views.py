from datetime import datetime
from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task, User, Category, Comment, Profile
from .forms import TaskForm, CommentForm, ProfileForm


def home(request):
    '''
    Renders index.html within base
    '''
    # below logic was taken (but customized) from:
    # https://www.learningaboutelectronics.com/Articles/
    # How-to-count-all-objects-of-a-database-table-in-Django.php
    all_tasks = Task.objects.all()
    published_tasks = all_tasks.filter(status="Published")
    archived_tasks = all_tasks.filter(status="Archived")
    total_published = published_tasks.count()
    total_archived = archived_tasks.count()
    total_users = User.objects.count()
    # context contains total number of published and archived tasks, users
    context = {
        'total_published': total_published,
        'total_archived': total_archived,
        'total_users': total_users,
    }
    # returns homepage
    return render(request, "index.html", context)


@login_required
def new_task(request):
    '''
    Get renders a blank task and profile (blank or prefilled)
    Post method creates a task and updates profile if needed.
    '''
    # obtains blank TaskForm
    form = TaskForm()
    # gets Profile if it exists, otherwise sets profile to None
    if Profile.objects.filter(person=request.user).exists():
        profile = get_object_or_404(Profile, person=request.user)
    else:
        profile = None
    # POST request
    if request.method == "POST":
        # obtains information from the form
        form = TaskForm(request.POST)
        # obtain final_date, change type and format to compare to today
        final_date_str = form.data['final_date']
        if final_date_str != "":
            date_format = '%Y-%m-%d'
            final_date = datetime.strptime(final_date_str, date_format).date()
            today = date.today()
            # if date in the past, display message, else allow posting
            # this is a backup for javascript used in task creation and editing
            if final_date < today:
                messages.warning(request, "Deadline cannot be in the past")
            else:
                # calls task processing if date is at least today
                return task_processing(request, profile, form)
        # calls task processing if there is no deadline
        else:
            return task_processing(request, profile, form)
    # if statement sets ProfileForm depending if it already exists or not
    if profile is not None:
        profile_form = ProfileForm(instance=profile)
    else:
        profile_form = ProfileForm()
    # GET request, context contains forms
    context = {
        'form': form,
        'profile_form': profile_form,
        }
    return render(request, "create_task.html", context)


def task_processing(request, profile, form):
    '''
    Saves a valid task, function prevents duplication of code.
    Owner, status and person are added before saving.
    '''
    if profile is not None:
        profile_form = ProfileForm(request.POST, instance=profile)
    else:
        profile_form = ProfileForm(request.POST)
    # below lines are a customized code obtained here:
    # https://www.youtube.com/watch?v=zJWhizYFKP0
    instance = form.save(commit=False)
    profile_instance = form.save(commit=False)
    if form.is_valid() and profile_form.is_valid():
        # instance saves owner and changes status
        instance.owner = request.user
        instance.status = "Published"
        instance.save()
        profile_form.instance.person = request.user
        profile_form.save()
        # returns user's own task list
        messages.success(request, "Task successfully created!")
        return list_own_tasks(request)
    # error message displayed if forms aren't valid.
    messages.error(request, "Something went wrong...")


def get_task_list(request):
    '''
    Function filters for Published tasks and obtains all profiles.
    Pagination displays number of pages depending on the number of tasks.
    '''
    # filtering tasks and obtaining profiles
    task_list = Task.objects.filter(status="Published")
    profiles = Profile.objects.all()
    # paginator logic copied from:
    # https://docs.djangoproject.com/en/4.2/topics/pagination/
    paginator = Paginator(task_list, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'task_list': task_list,
        "page_obj": page_obj,
        "profiles": profiles,
    }
    # displays the list of tasks
    return render(request, "list_tasks.html", context)


@login_required
def show_task(request, task_id):
    '''
    Get method obtains and displays the task.
    Post method saves the user as a helper.
    '''
    task = get_object_or_404(Task, id=task_id)
    owner_location = Profile.objects.get(person=task.owner).location
    # if there's no helper, user can apply.
    if task.helper is None:
        # POST request, user is saved as helper
        if request.method == "POST":
            task.helper = request.user
            task.status = "Ongoing"
            task.save()
            messages.success(request, "Task successfully accepted")
            return home(request)
        # GET request
        context = {
            'id': task_id,
            'task': task,
            'owner_location': owner_location,
        }
        return render(request, "show_task.html", context)
    # error display if there is associated helper.
    messages.error(request, "You don't seem to have access to this action.")
    return redirect(list_own_tasks)


@login_required
def edit_task(request, task_id):
    '''
    Get method displays the pre-filled task form.
    Post method saves the updated task and updates time.
    '''
    task = get_object_or_404(Task, id=task_id)
    # owner can edit request is there is no helper.
    if request.user == task.owner and task.helper is None:
        form = TaskForm(instance=task)
        # POST request
        if request.method == "POST":
            form = TaskForm(request.POST, instance=task)
            instance = form.save(commit=False)
            if form.is_valid():
                instance.updated_date = datetime.now()
                instance.save()
                messages.success(request, "Task updated successfully!")
                # redirects to show_task, since
                # edit is only available when there is no helper associated.
                return redirect(show_task, task_id)
            # error display if form isn't valid.
            messages.error(request, "Something went wrong")
        # GET request
        context = {'form': form}
        return render(request, "edit_task.html", context)
    # error message if user isn't owner or helper exists.
    messages.error(request, "You don't seem to have access to this action.")
    return redirect(list_own_tasks)


@login_required
def delete_task(request, task_id):
    '''
    Get method asks for confirmation of deletion.
    Post method deletes the task.
    '''
    task = get_object_or_404(Task, id=task_id)
    # check if user is owner and there is no helper.
    if request.user == task.owner and task.helper is None:
        # POST request
        if request.method == "POST":
            task.delete()
            messages.success(request, "Task deleted!")
            # returns user's list of task for a secondary deletion confirmation
            return redirect(list_own_tasks)
        # GET request
        context = {'task': task}
        return render(request, "delete_task.html", context)
    # error display if user isn't owner or helper exists.
    messages.error(request, "You don't seem to have access to this action.")
    return redirect(list_own_tasks)


@login_required
def list_own_tasks(request):
    '''
    Function filters for user's active tasks and displays them.
    '''
    # below filtering by using status__in adopted from:
    # https://copyprogramming.com/howto/django-filter-multiple-values
    # filter for Published and Ongoing tasks
    own_tasks = Task.objects.filter(owner=request.user).filter(
        status__in=["Published", "Ongoing"]
        )
    # filter for tasks where user is the helper
    helper_tasks = Task.objects.filter(helper=request.user, status="Ongoing")
    profiles = Profile.objects.all()
    context = {
        'own_tasks': own_tasks,
        'helper_tasks': helper_tasks,
        'profiles': profiles,
    }
    return render(request, "list_own_tasks.html", context)


@login_required
def show_ongoing_task(request, task_id):
    '''
    Get method displays the task, comment form and existing comments if any.
    Post method adds a comment and shows empty comment form again.
    '''
    # empty comment form
    form = CommentForm()
    task = get_object_or_404(Task, id=task_id)
    owner_details = Profile.objects.filter(person=task.owner).values()
    # obtaining all comments
    comments = task.comments.all()
    # check if helper exists
    if task.helper is not None:
        # check if user is owner or helper
        if (
            request.user == task.owner or request.user == task.helper
                ) and task.status == "Ongoing":
            # POST request
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
                    messages.success(request, "Your comment was posted!")
                    return redirect(show_ongoing_task, task_id)
                # error display if form isn't valid.
                messages.error(request, "Something went wrong...")
            # GET request
            context = {
                'id': task_id,
                'task': task,
                'form': form,
                'comments': comments,
                'owner_details': owner_details,
            }
            return render(request, "show_ongoing_task.html", context)
        # error display if user isn't owner or helper
        messages.error(request, "You don't have access to this request.")
        return redirect(list_own_tasks)
    # error display in case helper doesn't exist.
    messages.error(request, "There's nothing here...")
    return redirect(list_own_tasks)


@login_required
def archive_task(request, task_id):
    '''
    Get method asks for confirmation of archiving.
    Post method updates the task as archived.
    '''
    task = get_object_or_404(Task, id=task_id)
    # ownership check
    if request.user == task.owner and task.status == "Ongoing":
        # POST request
        if request.method == "POST":
            # check if helper exists
            if task.helper is not None:
                # status change
                task.status = "Archived"
                task.save()
                messages.success(request, "Glad it got sorted!")
                return redirect(list_own_tasks)
            # error display in case helper exists
            messages.error(
                request,
                "You don't seem to have access to this action."
                )
            return redirect(show_task, task_id)
        # GET request
        context = {
            "task": task,
            "id": task_id
        }
        return render(request, "archive_task.html", context)
    # error display if user isn't the owner
    messages.error(request, "You don't seem to have access to this action.")
    return redirect(list_own_tasks)


@login_required
def filter_category(request):
    '''
    Get method allows user to filter a task.
    Post method displays tasks based on filtering.
    '''
    categories = Category.objects.all()
    # POST request
    if request.method == "POST":
        # category and post filtering
        published_tasks = Task.objects.filter(status="Published")
        profiles = Profile.objects.all()
        filtered_category = request.POST.get("category-filter")
        if filtered_category != "Choose Task Category":
            filtered_tasks = published_tasks.filter(category=filtered_category)
            # used to render back-up button if more than 3 tasks exist
            filtered_tasks_count = filtered_tasks.count()
            # used to render filtered tasks depending on the category
            context = {
                "categories": categories,
                "filtered_tasks": filtered_tasks,
                "filtered_tasks_count": filtered_tasks_count,
                "profiles": profiles,
            }
            return render(request, "filter_category.html", context)
        # error display if user filters for none-category
        messages.error(request, "Please choose a category")
    # GET request
    context = {
        "categories": categories
    }
    return render(request, "filter_category.html", context)


@login_required
def edit_profile(request):
    '''
    Get method displays a blank or pre-filled form if exists.
    Post method creates/edits it.
    '''
    # check for existing profile
    if Profile.objects.filter(person=request.user).exists():
        profile = get_object_or_404(Profile, person=request.user)
    else:
        profile = None
    # POST request
    if request.method == "POST":
        if profile is not None:
            form = ProfileForm(request.POST, instance=profile)
        else:
            form = ProfileForm(request.POST)
        # below lines are a customized code obtained here:
        # https://www.youtube.com/watch?v=zJWhizYFKP0
        if form.is_valid():
            form.instance.person = request.user
            form.save()
            messages.success(request, "Profile updated")
            context = {"form": form}
            return render(request, "profile.html", context)
        # error display in case form isn't valid
        messages.error(request, "Error: Please try again")
    # renders existing or empty profile, if one doesn't exist
    if profile is not None:
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()
    # GET request
    context = {
        "form": form,
    }
    return render(request, "profile.html", context)
