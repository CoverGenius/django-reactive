import json
from typing import Optional

from django.contrib.postgres.fields import JSONField as BaseJSONField
from django.core.exceptions import ValidationError

from jsonschema import validate, ValidationError as JSONSchemaValidationError
from pydantic.main import ModelMetaclass
from pydantic.error_wrappers import ValidationError as PydanticValidationError

from .forms.fields import ReactJSONSchemaFormField
from .forms.widgets import ReactJSONSchemaFormWidget


class ReactJSONSchemaField(BaseJSONField):
    def __init__(
        self, schema: Optional[dict] = None, ui_schema: Optional[dict] = None, **kwargs
    ):
        kwargs.setdefault("default", dict)
        super().__init__(**kwargs)
        if isinstance(schema, ModelMetaclass):
            self.pydantic_schema = schema
            schema = schema.schema()
        else:
            self.pydantic_schema = None
        self.schema = schema
        self.ui_schema = ui_schema

    def formfield(self, **kwargs):
        defaults = {"required": not self.blank}
        defaults.update(**kwargs)

        if isinstance(self.schema, ModelMetaclass):
            self.schema = self.schema.schema()

        return ReactJSONSchemaFormField(
            widget=ReactJSONSchemaFormWidget(
                schema=self.schema, ui_schema=self.ui_schema
            ),
            **defaults
        )

    def validate(self, value, model_instance):
        if self.pydantic_schema:
            try:
                self.pydantic_schema(**value)
            except PydanticValidationError as exc:
                errors = {
                    error["loc"][0]: {"errors": [error["msg"]]}
                    for error in exc.errors()
                }
                raise ValidationError(json.dumps(errors))

        super().validate(value, model_instance)

        try:
            validate(value, self.schema)
        except JSONSchemaValidationError:
            raise ValidationError("JSONSchema validation errors.")
