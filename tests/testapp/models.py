from django.db import models

from django_reactive.fields import ReactJSONSchemaField


def modify_max_length(schema, ui_schema):
    import random

    max_length = random.randint(20, 30)
    schema['properties']['test_field']['maxLength'] = max_length
    ui_schema['test_field']['ui:help'] = f'Max {max_length}'


def modify_help_text(schema, ui_schema, instance=None):
    if instance:
        if instance.is_some_condition:
            ui_schema['test_field']['ui:help'] = 'Condition is set'
        else:
            ui_schema['test_field']['ui:help'] = 'Condition is unset'


class RenderMethodWithObjectSchemaModel(models.Model):
    is_some_condition = models.BooleanField(default=True)
    json_field = ReactJSONSchemaField(
        schema={
            'title': 'TestSchema',
            'type': 'object',
            'required': ['test_field'],
            'properties': {
                'test_field': {
                    'type': 'string',
                    'maxLength': 10,
                    'minLength': 5,
                },
                'another_test_field': {
                    'type': 'string',
                },
            },
            'additionalProperties': False,
        },
        ui_schema={
            'test_field': {'ui:help': 'Max 10'},
        },
        on_render=modify_help_text,
    )


class RenderMethodSchemaModel(models.Model):
    json_field = ReactJSONSchemaField(
        schema={
            'title': 'TestSchema',
            'type': 'object',
            'required': ['test_field'],
            'properties': {
                'test_field': {
                    'type': 'string',
                    'maxLength': 10,
                    'minLength': 5,
                },
                'another_test_field': {
                    'type': 'string',
                },
            },
            'additionalProperties': False,
        },
        ui_schema={
            'test_field': {'ui:help': 'Max 10'},
        },
        on_render=modify_max_length,
    )


class SchemaModel(models.Model):
    json_field = ReactJSONSchemaField(
        schema={
            'title': 'TestSchema',
            'type': 'object',
            'required': ['test_field'],
            'properties': {
                'test_field': {
                    'type': 'string',
                    'maxLength': 10,
                    'minLength': 5,
                },
                'another_test_field': {
                    'type': 'string',
                },
            },
            'additionalProperties': False,
        }
    )


class OptionalSchemaModel(models.Model):
    json_field = ReactJSONSchemaField(
        schema={
            'type': 'object',
            'required': ['test_field'],
            'properties': {'test_field': {'type': 'string'}},
        },
        blank=True,
    )


class ExtraMediaSchemaModel(models.Model):
    json_field = ReactJSONSchemaField(
        schema={
            'type': 'object',
            'required': ['test_field'],
            'properties': {'test_field': {'type': 'string'}},
        },
        blank=True,
        extra_css=['path/to/my/css/file.css'],
        extra_js=['path/to/my/js/file.js'],
    )


class InvalidSchemaModel(models.Model):
    invalid_json_schema_field = ReactJSONSchemaField(
        schema={
            'type': 'object',
            'properties': {'test_field': {'type': 'incorrect'}},
        }
    )
