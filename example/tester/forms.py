from django.forms import ModelForm

from .models import TestModel, PydanticTestModel


class TestModelForm(ModelForm):
    class Meta:
        model = TestModel
        exclude = ["id"]


class BasicTestModelForm(ModelForm):
    class Meta:
        model = TestModel
        fields = ["basic"]


class PydanticTestModelForm(ModelForm):
    class Meta:
        model = PydanticTestModel
        exclude = ["id"]
