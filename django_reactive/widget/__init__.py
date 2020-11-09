from django.forms import ModelForm

from .fields import ReactJSONSchemaFormField


class ReactJSONSchemaModelForm(ModelForm):
    """
    Provides the instance object of a ModelForm to all of the schema field widgets.
    """

    def __init__(self, *args, **kwargs):
        on_render_object = kwargs.get("instance", None)
        super().__init__(*args, **kwargs)
        for field_name, field_value in self.fields.items():
            if isinstance(field_value, django_reactive.forms.fields.ReactJSONSchemaFormField):
                self.fields[field_name].widget.on_render_object = on_render_object
