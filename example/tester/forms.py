from django.forms import ModelForm

from .models import TestModel


class TestModelForm(ModelForm):
    class Meta:
        model = TestModel
        exclude = ["id"]


class BasicTestModelForm(ModelForm):
    class Meta:
        model = TestModel
        fields = ["basic"]
