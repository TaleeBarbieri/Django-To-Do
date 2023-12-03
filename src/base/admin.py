from django.contrib import admin
from .models import Task

from admin_extra_buttons.api import ExtraButtonsMixin, button
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import (
    AdminPasswordChangeForm,
    UserChangeForm,
    UserCreationForm,
)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password", "logo")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "last_login",)
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )

    @button(
        html_attrs={'style': 'background-color:#88FF88;color:black'})
    def refresh(self, request):
        self.message_user(request, 'Reloaded Page')

    def grant_superuser_and_staff(modeladmin, request, queryset):
        for user in queryset:
            user.is_superuser = True
            user.is_staff = True
            user.save()

    grant_superuser_and_staff.short_description = "Grant Superuser and Staff Status"

    actions = [grant_superuser_and_staff]


@admin.register(Task)  # View the (Task) section in the admin page
class TaskAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    list_display = ('title', 'user', 'complete', 'created', 'due_date',)
    search_fields = ('title',)
    list_filter = ('title', 'created', 'due_date',)
    actions = ['mark_complete', 'mark_incomplete']

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
