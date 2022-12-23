from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Url, User


@admin.register(Url)
class AdminUrl(ModelAdmin):
    list_display = ('id', 'short_name', 'long_name')

@admin.register(User)
class AdminUser(ModelAdmin):
    search_fields = ('username',)
    list_display = ('id', 'username', 'email')
