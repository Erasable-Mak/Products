
# todo/admin.py

from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    # title: product, description: category, completed: status run
    list_display = ('title', 'description', 'completed')


# Register models here.
admin.site.register(Todo, TodoAdmin)
