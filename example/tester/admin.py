from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import TestModel
from .forms import TestModelForm


class TestModelAdmin(ModelAdmin):
    form = TestModelForm


admin.site.register(TestModel, TestModelAdmin)
