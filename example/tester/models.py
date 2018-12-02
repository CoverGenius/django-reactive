from django.contrib.postgres.fields import JSONField
from django.db import models

from django_reactive.fields import ReactJSONSchemaField


class TestModel(models.Model):
    test_field = ReactJSONSchemaField(
        help_text='A field to test react-json-schema-form widget.',
        schema={
            'title': 'Name form',
            'type': 'object',
            'required': ['title'],
            'properties': {
                'title': {
                    'type': 'string',
                    'title': 'TITLE',
                    'default': 'A new task',
                },
                'another_field': {
                    'type': 'string',
                    'title': 'ANOTHER_FIELD',
                },
            }
        }
    )

    test_widget = JSONField(
        null=False, default=dict,
        help_text='A field to test react-json-schema-form widget.',
    )
