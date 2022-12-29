from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import (
    BasicExampleModel,
    NestedExampleModel,
    ArraysExampleModel,
    NumbersExampleModel,
    WidgetExampleModel,
    OrderingExampleModel,
    ReferencesExampleModel,
    ErrorsExampleModel,
    LargeExampleModel,
    DateAndTimeExampleModel,
    ValidationExampleModel,
    FileTestModel,
    AlternativesExample,
    PropertyDependenciesExample,
    SchemaDependenciesExampleModel,
    MultipleExampleModel,
)
from .forms import ExampleModelForm


class TestModelAdmin(ModelAdmin):
    form = ExampleModelForm


admin.site.register(BasicExampleModel, TestModelAdmin)
admin.site.register(NestedExampleModel)
admin.site.register(ArraysExampleModel)
admin.site.register(NumbersExampleModel)
admin.site.register(WidgetExampleModel)
admin.site.register(OrderingExampleModel)
admin.site.register(ReferencesExampleModel)
admin.site.register(ErrorsExampleModel)
admin.site.register(LargeExampleModel)
admin.site.register(DateAndTimeExampleModel)
admin.site.register(ValidationExampleModel)
admin.site.register(FileTestModel)
admin.site.register(AlternativesExample)
admin.site.register(PropertyDependenciesExample)
admin.site.register(SchemaDependenciesExampleModel)
admin.site.register(MultipleExampleModel)
