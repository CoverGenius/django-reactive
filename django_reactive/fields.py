from django.core.exceptions import ValidationError
from django.core import checks
from jsonschema import validate, ValidationError as JSONSchemaValidationError

from .widget.fields import ReactJSONSchemaFormField
from .widget.widgets import ReactJSONSchemaFormWidget
from .schema_validator import validate_json_schema

try:
    # DJANGO 3.1
    from django.db.models import JSONField as BaseJSONField
except ImportError:
    from django.contrib.postgres.fields import JSONField as BaseJSONField


class ReactJSONSchemaField(BaseJSONField):
    def __init__(self, schema=None, ui_schema=None, on_render=None, extra_css=None, extra_js=None, **kwargs):
        kwargs.setdefault('default', dict)
        super().__init__(**kwargs)
        self.schema = schema
        self.ui_schema = ui_schema
        self.on_render = on_render
        self.extra_css = extra_css
        self.extra_js = extra_js

    def formfield(self, **kwargs):
        defaults = {
            'required': not self.blank,
        }
        defaults.update(**kwargs)
        return ReactJSONSchemaFormField(
            widget=ReactJSONSchemaFormWidget(
                schema=self.schema,
                ui_schema=self.ui_schema,
                on_render=self.on_render,
                extra_css=self.extra_css,
                extra_js=self.extra_js,
            ),
            **defaults,
        )

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        try:
            validate(value, self.schema)
        except JSONSchemaValidationError:
            raise ValidationError('This field has errors.')

    def check(self, **kwargs):
        errors = super().check(**kwargs)
        res, schema_errors = validate_json_schema(self.schema)
        if not res:
            msg = ','.join(schema_errors)
            errors = [
                checks.Error(
                    f'JSON schema is not valid: {msg}',
                    obj=self.model,
                    id='fields.JSON_SCHEMA_ERROR',
                )
            ]

        return errors
