# from django.shortcuts import render, redirect

from django.views.generic.list import ListView      # To render tasks as a list

from django.views.generic.detail import DetailView      # This is to view the data of a specific item

from django.views.generic.edit import CreateView        # This is to create new objects in the database

from django.views.generic.edit import UpdateView        # This is to take in a value and modify an already existing data value

from django.views.generic.edit import DeleteView        # This will confirm that you want to delete an item and delete it aswell

from django.urls import reverse_lazy        # Made to create URLs for views in a flexible manner

from base.models import Task


class TaskList(ListView):
    model = Task    # Import Task to view it as a list in template
    context_object_name = 'tasks'   # It's the name that when called in the html page returns the above data
    template_name = "base/task.html"


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-create')       # This is to redirect the user to a created page


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
