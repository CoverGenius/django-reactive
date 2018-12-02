from django import forms
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from django_reactive.forms.widgets import ReactJSONSchemaFormWidget
from . import models


class TestAdminForm(forms.ModelForm):
    class Meta:
        model = models.TestModel
        fields = [
            'test_field',
            'test_widget',
        ]
        widgets = {
            'test_widget': ReactJSONSchemaFormWidget(schema={
                'title': 'Todo 1',
                'type': 'object',
                'required': ['title'],
                'properties': {
                    'title': {
                        'type': 'string',
                        'title': 'title',
                        'default': 'title2',
                    },
                }
            }),
        }


class TestAdmin(ModelAdmin):
    form = TestAdminForm


admin.site.register(models.TestModel, TestAdmin)
