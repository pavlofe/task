from django.urls import path

from taskapp import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('create', views.TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/update', views.TaskUpdateView.as_view(), name='task_update'),

]
