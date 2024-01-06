# testapp/urls.py

from django.urls import path, re_path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, SMSListView, add_task, get_all_tasks, get_task, create_task, update_task, task_get_one

urlpatterns = [
    path('sms/', SMSListView.as_view(), name='sms-list'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/add/', add_task, name='add-task'),

    # Использование регулярных выражений для detail и update
    re_path(r'^tasks/(?P<pk>\d+)/$', TaskDetailView.as_view(), name='task-detail'),
    re_path(r'^tasks/(?P<pk>\d+)/update/$', TaskUpdateView.as_view(), name='task-update'),

    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('tasks/', get_all_tasks, name='get_all_tasks'),
    path('tasks/<int:task_id>/', get_task, name='get_task'),
    path('tasks/create/', create_task, name='create_task'),
    path('tasks/<int:task_id>/update/', update_task, name='update_task'),
    path('tasks/get_one/<int:task_id>/', task_get_one, name='get-one-task'),

]

