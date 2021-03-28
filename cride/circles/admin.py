"""Django admin registration"""

# Admin
from django.contrib import admin

# Model
from cride.circles.models import Circle


class AdminCircles(admin.ModelAdmin):

    list_display = ("name", "rides_offered", "rides_taken", "verified", "is_public", "members_limit")

    list_filter = ("is_public", "verified", "is_limited")

    search_fields = ("name", "slug", "")

admin.site.register(Circle, AdminCircles)
