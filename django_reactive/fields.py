from django.contrib.postgres.fields import JSONField as BaseJSONField
from django.core.exceptions import ValidationError
from jsonschema import validate, ValidationError as JSONSchemaValidationError

from .forms.fields import ReactJSONSchemaFormField
from .forms.widgets import ReactJSONSchemaFormWidget


class ReactJSONSchemaField(BaseJSONField):
    def __init__(self, schema=None, ui_schema=None, hooks=None, extra_css=None, extra_js=None, **kwargs):
        kwargs.setdefault("default", dict)
        super(ReactJSONSchemaField, self).__init__(**kwargs)
        self.hooks = hooks
        self.schema = schema
        self.ui_schema = ui_schema
        self.extra_css = extra_css
        self.extra_js = extra_js

    def formfield(self, **kwargs):
        defaults = {
            "required": not self.blank,
        }
        defaults.update(**kwargs)
        return ReactJSONSchemaFormField(
            widget=ReactJSONSchemaFormWidget(
                schema=self.schema,
                ui_schema=self.ui_schema,
                hooks=self.hooks,
                extra_css=self.extra_css,
                extra_js=self.extra_js,
            ),
            **defaults,
        )

    def validate(self, value, model_instance):
        super(ReactJSONSchemaField, self).validate(value, model_instance)
        try:
            validate(value, self.schema)
        except JSONSchemaValidationError:
            raise ValidationError("This field has errors.")
