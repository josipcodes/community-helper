from django.shortcuts import render, HttpResponse
# from .models import Task




def home(request):
    return render(request, "index.html")


def NewTask(request):
    return render(request, "create-task.html")