from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    fields = ['name', 'description', 'deadline', 'priority','status', 'file']
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')


