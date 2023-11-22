from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('submission/', views.new_task, name='submission'),
    path('open-tasks/', views.get_task_list, name='open-tasks')
]
