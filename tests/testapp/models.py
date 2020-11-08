from django.db import models

from django_reactive.fields import ReactJSONSchemaField


def modify_max_length(schema, ui_schema):
    import random

    max_length = random.randint(20, 30)
    schema["properties"]["test_field"]["maxLength"] = max_length
    ui_schema["test_field"]["ui:help"] = f"Field maximum: {max_length} characters"


def maybe_disable_field(schema, ui_schema):
    some_condition = 1
    if some_condition:
        ui_schema["another_test_field"] = {"ui:disabled": True}


class HookedSchemaModel(models.Model):
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
        },
        ui_schema={
            "test_field": {"ui:help": "Field maximum: 10 characters"},
        },
        hooks=[modify_max_length, maybe_disable_field],
    )


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
