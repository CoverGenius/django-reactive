from django.db import models

from django_reactive.fields import ReactJSONSchemaField


class SchemaModel(models.Model):
    json_field = ReactJSONSchemaField(
        schema={
            "title": "TestSchema",
            "type": "object",
            "required": ["test_field"],
            "properties": {
                "test_field": {
                    "type": "string",
                    "maxLength": 10,
                    "minLength": 5,
                },
                "another_test_field": {
                    "type": "string",
                },
            },
            "additionalProperties": False,
        }
    )


class OptionalSchemaModel(models.Model):
    json_field = ReactJSONSchemaField(
        schema={
            "type": "object",
            "required": ["test_field"],
            "properties": {"test_field": {"type": "string"}},
        },
        blank=True,
    )


class ExtraMediaSchemaModel(models.Model):
    json_field = ReactJSONSchemaField(
        schema={
            "type": "object",
            "required": ["test_field"],
            "properties": {"test_field": {"type": "string"}},
        },
        blank=True,
        extra_css=["path/to/my/css/file.css"],
        extra_js=["path/to/my/js/file.js"],
    )
