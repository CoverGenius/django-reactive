from django.db import models

from django_reactive.fields import ReactJSONSchemaField

from .constants import TODO_SCHEMA, TODO_UI_SCHEMA, set_task_types


class Todo(models.Model):
    """
    A collection of task lists for a todo.
    """

    name = models.CharField(max_length=255)
    task_lists = ReactJSONSchemaField(
        help_text='Task lists',
        schema=TODO_SCHEMA,
        ui_schema=TODO_UI_SCHEMA,
        on_render=set_task_types,
        extra_css=['css/extra.css'],
        extra_js=['js/extra.js'],
    )


class TaskType(models.Model):
    """
    A task type used to dynamically populate a todo list schema field dropdown.
    """

    name = models.CharField(max_length=255)
