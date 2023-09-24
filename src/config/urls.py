"""todo_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete
# import base.views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TaskList.as_view(), name='home'),      # The (.as_view) is used to display a classed base view
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),     # This will create a page to view the detail of one of the tasks with a ordered number value to it ---> (<int:pk>)
    path('task-create/', TaskCreate.as_view(), name='task-create'),     # This will create a new task form
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),    # This will go to an existing task and allow to edit it
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]
