from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import Task
from .forms import TaskForm

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')
    form_class = TaskForm

