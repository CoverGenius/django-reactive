#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-reactive
------------

Tests for `django-reactive` models module.
"""
from django.core.exceptions import ValidationError
from django.db.models import Model
from django.test import TestCase

from django_reactive.fields import ReactJSONSchemaField


class TestReactJSONSchemaField(TestCase):

    def test_validate(self):
        class TestModel(Model):
            class Meta:
                managed = False
                app_label = 'django_reactive'

            json_field = ReactJSONSchemaField(schema={
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
                    }
                },
                'additionalProperties': False,
            })

        model = TestModel(json_field={'test_field': '6chars'})
        model.full_clean()  # no error

        model.json_field['test_field'] = 1  # not a string
        with self.assertRaises(ValidationError):
            model.full_clean()

        model.json_field['test_field'] = '3ch'  # too short
        with self.assertRaises(ValidationError):
            model.full_clean()

        model.json_field['test_field'] = '12characters'  # too long
        with self.assertRaises(ValidationError):
            model.full_clean()

        model.json_field = {'unknown_field': True}
        with self.assertRaises(ValidationError):
            model.full_clean()

        model.json_field = {}  # missed a required field
        with self.assertRaises(ValidationError):
            model.full_clean()

    def test_blank(self):
        class TestModelBlank(Model):
            class Meta:
                managed = False
                app_label = 'django_reactive'

            json_field = ReactJSONSchemaField(schema={'type': 'array'}, blank=True)

        class TestModelNotBlank(Model):
            class Meta:
                managed = False
                app_label = 'django_reactive'

            json_field = ReactJSONSchemaField(schema={'type': 'array'}, blank=False)

        model = TestModelBlank(json_field=None)
        model.full_clean()

        with self.assertRaises(ValidationError) as context:
            model = TestModelNotBlank(json_field=None)
            model.full_clean()
        self.assertEqual("{'json_field': ['This field cannot be null.']}", str(context.exception))
