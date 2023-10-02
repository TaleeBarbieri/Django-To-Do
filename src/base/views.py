from django.shortcuts import redirect

from django.views.generic.list import ListView  # To render tasks as a list

from django.views.generic.detail import DetailView  # This is to view the data of a specific item

from django.views.generic.edit import CreateView  # This is to create new objects in the database

from django.views.generic.edit import UpdateView  # This is to take in a value and modify an already existing data value

from django.views.generic.edit import \
    DeleteView  # This will confirm that you want to delete an item and delete it as well

from django.urls import reverse_lazy  # Made to create URLs for views in a flexible manner

from django.contrib.auth.views import LoginView  # This if for viewing the login page

from django.contrib.auth.mixins import \
    LoginRequiredMixin  # This will make it so you are forced to login or else it redirects you

from django.views.generic.edit import FormView  # It's a class-based view, this is used to display and handle forms

from django.contrib.auth.forms import UserCreationForm  # This is to create a page with a form to register a new user

from django.contrib.auth import login  # This is to log the user in

from django.contrib import messages  # Django's messages tool

from django import forms

from base.models import Task


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True  # This is forcing authenticated users to a specified URL

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm  # This is to show which type of form it is
    redirect_authenticated_user = True
    success_message = 'Your account has been created successfully. Now you can log in.'
    success_url = reverse_lazy('logout')

    def form_valid(self, form):
        user = form.save()  # This will get the new created user and save it
        if user is not None:
            login(self.request, user)  # Here we log the new user in
            messages.success(self.request, self.success_message)  # This shows a success message in the login page
        return super(RegisterPage, self).form_valid(form)  # super() is used to get data from another class

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args,
                                             **kwargs)  # This checks if user is authenticated is so he will not be aloud to access other pages


class TaskList(LoginRequiredMixin, ListView):
    model = Task  # Import Task to view it as a list in template
    context_object_name = 'tasks'  # It's the name that when called in the html page returns the above data
    template_name = "base/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(
            user=self.request.user)  # This is to filter out which user can see what
        context['count'] = context['tasks'].filter(
            complete=False).count()  # This will count the amount of not finished tasks

        search_input = self.request.GET.get(
            'search-area') or ''  # Here it searches for a parameter called 'search-area' which finds in the task.html and it assigns the value 'search input' to it
        if search_input:  # This checks if the user entered something to search for
            context['tasks'] = context['tasks'].filter(
                # Checks if user entered the title of one of the tasks that is in the variable 'search-input'
                title__startswith=search_input)  # Searches for the title in the tasks that matches the inputted text

        context['search_input'] = search_input  # This stores the 'search-input' value in the 'context' dict
        return context  # returns the matching input words


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "base/home.html"
    context_object_name = 'task'


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('home')  # This is to redirect the user to a created page

    def form_valid(self, form):
        form.instance.user = self.request.user  # This is to associate the specific created task to a specific user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy('home')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('home')
