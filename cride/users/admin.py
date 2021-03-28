"""Django custom user model and profile in admin page"""

# Admin
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

# User and Profile

from cride.users.models import User, Profile


class CustomUserAdmin(UserAdmin):
    
    list_display = ("email", "username", "first_name", "last_name", "is_staff", "is_client")

    list_filter = ("is_client", "is_staff", "created", "modified")


class CustomProfileAdmin(admin.ModelAdmin):

    list_display = ("user","reputation", "rides_taken", "rides_offered")

    search_fields = ("user__username", "user__email", "user__first_name", "user__last_name")

    list_filter = ("reputation",)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, CustomProfileAdmin)