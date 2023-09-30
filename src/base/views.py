# from django.shortcuts import render, redirect

from django.views.generic.list import ListView      # To render tasks as a list

from django.views.generic.detail import DetailView      # This is to view the data of a specific item

from django.views.generic.edit import CreateView        # This is to create new objects in the database

from django.views.generic.edit import UpdateView        # This is to take in a value and modify an already existing data value

from django.views.generic.edit import DeleteView        # This will confirm that you want to delete an item and delete it as well

from django.urls import reverse_lazy        # Made to create URLs for views in a flexible manner

from django.contrib.auth.views import LoginView     # This if for logging in

from django.contrib.auth.mixins import LoginRequiredMixin       # This will make it so you are forced to login or else it redirects you

from base.models import Task


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class TaskList(LoginRequiredMixin, ListView):
    model = Task        # Import Task to view it as a list in template
    context_object_name = 'tasks'       # It's the name that when called in the html page returns the above data
    template_name = "base/task.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)      # This is to filter out which user can see what
        context['count'] = context['tasks'].filter(complete=False).count()
        return context


class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('task-create')       # This is to redirect the user to a created page


    def form_valid(self, form):
        form.instace.user = self.request.user       # This is to associate the specific created task to a specific user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('home')


class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('home')
