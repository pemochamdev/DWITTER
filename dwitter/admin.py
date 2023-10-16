# dwitter/admin.py

from django.contrib import admin
from django.contrib.auth.models import User, Group

from dwitter.models import Profile, Dweet


@admin.register(Dweet)
class DweetAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'created_at']
    



class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username", "email"]
    list_display = ['username', 'email']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)




@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    #list_display = ['user', 'follows']
    fields = ['user', 'follows']
    
