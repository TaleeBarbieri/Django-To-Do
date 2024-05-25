from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from base.views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage, \
    EditProfile, PasswordsChangeView
from django.contrib.auth.views import LogoutView  # This is the LogoutView without having to create a custom view

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('register/', RegisterPage.as_view(), name='register'),  # This is the register user page
                  path('login/', CustomLoginView.as_view(), name='login'),  # This is the page to login
                  path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # This is the page to logout
                  path('home/', TaskList.as_view(), name='home'),
                  # The (.as_view) is used to display a classed base view
                  path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
                  # This will create a page to view the detail of one of the tasks with a ordered number value to it
                  # ---> (<int:pk>)
                  path('task-create/', TaskCreate.as_view(), name='task-create'),  # This will create a new task form
                  path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
                  # This will go to an existing task and allow to edit it
                  path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
                  path('edit_user/<str:username>/', EditProfile.as_view(), name='edit_user'),
                  path('', include('social_django.urls', namespace='social')),
                  path('change_password/',
                       PasswordsChangeView.as_view(template_name='base/change_password.html'),
                       name='change_password'),
                  path('password_change_done/', PasswordsChangeView.password_success,
                       name='password_change_done'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
