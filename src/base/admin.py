from django.contrib import admin
from .models import Task
from admin_extra_buttons.api import ExtraButtonsMixin, button
@admin.register(Task) # View the (Task) section in the admin page
class TaskAdmin(ExtraButtonsMixin,admin.ModelAdmin):
    list_display = ('title','complete','create')
    search_fields = ('title',)
    list_filter = ('title','create',)
    @button(
            html_attrs={'style': 'background-color:#88FF88;color:black'})
    def refresh(self, request):
        self.message_user(request, 'Reloaded Page')