from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('submission/', views.new_task, name='submission'),
    path('open-tasks/', views.get_task_list, name='open-tasks'),
    path('display-task/<int:task_id>', views.show_task, name='display-task'),
    path('edit-task/<int:task_id>', views.edit_task, name='edit-task'),
    path('delete-task/<int:task_id>', views.delete_task, name='delete-task'),
    path('task-list/', views.list_own_tasks, name='task-list'),
    path('ongoing-task/<int:task_id>',
         views.show_ongoing_task, name='ongoing-task'),
    path('filter/', views.filter_category, name='filter-category'),
    path('archive-task/<int:task_id>',
         views.archive_task, name='archive-task'),
    path('profile/', views.edit_profile, name='profile'),
]
