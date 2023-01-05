from django.forms import ModelForm

from .models import BasicExampleModel


class ExampleModelForm(ModelForm):
    class Meta:
        model = BasicExampleModel
        exclude = ['id']


class BasicTestModelForm(ModelForm):
    class Meta:
        model = BasicExampleModel
        fields = ['basic']
