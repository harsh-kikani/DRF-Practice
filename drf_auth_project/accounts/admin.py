# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Register User model (usually already included in Django admin)
admin.site.unregister(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff', 'is_active']
    search_fields = ['username', 'email']

# Register Token model to view user tokens
@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['key', 'user', 'created']
    search_fields = ['user__username', 'key']

