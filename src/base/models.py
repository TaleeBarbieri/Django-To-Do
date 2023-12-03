from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), null=True, blank=True)
    profile_picture = models.ImageField(upload_to='media/', null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)

    groups = models.ManyToManyField(Group, blank=True)
    user_permissions = models.ManyToManyField(Permission, blank=True)

    def __str__(self):
        return self.username


class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.title    # This is to make an instance into human-readable text

    class Meta:
        ordering = ['complete']
        # This is the order in which the data will appear to the user
        # In this case the completed tasks will show last
