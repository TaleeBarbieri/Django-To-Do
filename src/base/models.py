from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.title    # This is to make an instance into human-readable text

    class Meta:
        ordering = ['complete', ]
        # This is the order in which the data will appear to the user
        # In this case the completed tasks will show last
