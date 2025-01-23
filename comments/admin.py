from django.contrib import admin
from comments.models import PostModel


@admin.register(PostModel)
class UserModelAdmin(admin.ModelAdmin):
    ...
