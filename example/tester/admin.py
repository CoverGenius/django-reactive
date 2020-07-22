from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import TestModel, PydanticTestModel
from .forms import TestModelForm, PydanticTestModelForm, BasicTestModelForm


class BasicTestModel(TestModel):
    class Meta:
        proxy = True


class TestModelAdmin(ModelAdmin):
    form = TestModelForm


admin.site.register(TestModel, TestModelAdmin)


class BasicTestModelAdmin(ModelAdmin):
    form = BasicTestModelForm


admin.site.register(BasicTestModel, BasicTestModelAdmin)


class PydanticTestModelAdmin(ModelAdmin):
    form = PydanticTestModelForm


admin.site.register(PydanticTestModel, PydanticTestModelAdmin)
