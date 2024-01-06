# testapp/urls.py

from django.urls import path, re_path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, SMSListView, add_task
urlpatterns = [
    path('sms/', SMSListView.as_view(), name='sms-list'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/add/', add_task, name='add-task'),

    # Использование регулярных выражений для detail и update
    re_path(r'^tasks/(?P<pk>\d+)/$', TaskDetailView.as_view(), name='task-detail'),
    re_path(r'^tasks/(?P<pk>\d+)/update/$', TaskUpdateView.as_view(), name='task-update'),

    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),

]
