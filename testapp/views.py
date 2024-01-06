from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task, SMS
from .forms import TaskForm

class SMSListView(ListView):
    model = SMS
    template_name = 'sms_list.html'
    context_object_name = 'sms_list'

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('task-list')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {'form': form})

def get_all_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def get_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'task_detail.html', {'task': task})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_all_tasks')
    else:
        form = TaskForm()

    return render(request, 'create_task.html', {'form': form})

def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('get_all_tasks')
    else:
        form = TaskForm(instance=task)

    return render(request, 'update_task.html', {'form': form, 'task': task})

def task_get_one(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'get_one_task.html', {'task': task})
