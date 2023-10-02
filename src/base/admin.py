from django.contrib import admin
from .models import Task
from admin_extra_buttons.api import ExtraButtonsMixin, button


@admin.register(Task)  # View the (Task) section in the admin page
class TaskAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    list_display = ('title', 'user', 'complete', 'created','due_date', )
    search_fields = ('title',)
    list_filter = ('title', 'created', 'due_date', )
    actions = ['mark_complete','mark_incomplete']

    @button(
        html_attrs={'style': 'background-color:#88FF88;color:black'})
    def refresh(self, request):
        self.message_user(request, 'Reloaded Page')

    @admin.action(description="Mark Task as Complete")
    def mark_complete(self, request, queryset):
        # This method is used to mark selected tasks as complete.
        # 'queryset' is a list of selected Task objects.
        queryset.update(complete=True)

    @admin.action(description="Mark Task as Incomplete")
    def mark_incomplete(self, request, queryset):
    # This method is used to mark selected tasks as complete.
    # 'queryset' is a list of selected Task objects.
        queryset.update(complete=False)
