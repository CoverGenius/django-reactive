from django.contrib import admin

from .models import Todo, TaskType


class TodoAdmin(admin.ModelAdmin):
    pass


class TaskTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Todo, TodoAdmin)
admin.site.register(TaskType, TaskTypeAdmin)
