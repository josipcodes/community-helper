from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('submission/', views.new_task, name='submission'),
    path('open-tasks/', views.get_task_list, name='open-tasks'),
    path('display-task/<task_id>', views.show_task, name='display-task'),
    path('edit-task/<task_id>', views.edit_task, name='edit-task'),
    path('delete-task/<task_id>', views.delete_task, name='delete-task'),
    path('task-list/', views.list_own_tasks, name='display-tasks'),
]
