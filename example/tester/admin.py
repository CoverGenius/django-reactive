from django import forms
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from . import models


class TestAdminForm(forms.ModelForm):
    class Meta:
        model = models.TestModel
        exclude = ['id']


class TestAdmin(ModelAdmin):
    form = TestAdminForm


admin.site.register(models.TestModel, TestAdmin)
