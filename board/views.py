from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm




def home(request):
    return render(request, "index.html")

# @login_required(login_url="")
def new_task(request):
    form = TaskForm()
    if request.method == "POST":
        if form.is_valid():
            # instance = form.save(commit=False)
            # instance.owner = request.user
            # instance.save()
            # form.save()
            return redirect('home')
        # title = request.POST.get('task-title')
        # description = request.POST.get('task-description')
        # category = request.POST.get('category')
        # final_date = request.POST.get('deadline')        
        # Task.objects.create(title=title, description=description, category=category, final_date=final_date)
    context = {'form': form}
    return render(request, "create-task.html", context)




