# dwitter/admin.py

from django.contrib import admin
from django.contrib.auth.models import User, Group

from dwitter.models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username", "email"]
    list_display = ['username', 'email']
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

