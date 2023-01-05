from django.db import models

from django_reactive.fields import ReactJSONSchemaField


class BasicExampleModel(models.Model):
    basic = ReactJSONSchemaField(
        help_text='Basic example',
        schema={
            'title': 'A registration form',
            'description': 'A basic form example.',
            'type': 'object',
            'required': ['firstName', 'lastName'],
            'properties': {
                'firstName': {'type': 'string', 'title': 'First name'},
                'lastName': {'type': 'string', 'title': 'Last name'},
                'age': {'type': 'integer', 'title': 'Age'},
                'bio': {'type': 'string', 'title': 'Bio'},
                'password': {'type': 'string', 'title': 'Password', 'minLength': 3},
                'telephone': {'type': 'string', 'title': 'Telephone', 'minLength': 10},
            },
        },
        ui_schema={
            'firstName': {'ui:autofocus': True, 'ui:emptyValue': ''},
            'age': {
                'ui:widget': 'updown',
                'ui:title': 'Age of person',
                'ui:description': '(earthian year)',
            },
            'bio': {'ui:widget': 'textarea'},
            'password': {'ui:widget': 'password', 'ui:help': 'Hint: Make it strong!'},
            'date': {'ui:widget': 'alt-datetime'},
            'telephone': {'ui:options': {'inputType': 'tel'}},
        },
    )


class NestedExampleModel(models.Model):
    nested = ReactJSONSchemaField(
        help_text='Nested',
        schema={
            'title': 'A list of tasks',
            'type': 'object',
            'required': ['title'],
            'properties': {
                'title': {'type': 'string', 'title': 'Task list title'},
                'tasks': {
                    'type': 'array',
                    'title': 'Tasks',
                    'items': {
                        'type': 'object',
                        'required': ['title'],
                        'properties': {
                            'title': {
                                'type': 'string',
                                'title': 'Title',
                                'description': 'A sample title',
                            },
                            'details': {
                                'type': 'string',
                                'title': 'Task details',
                                'description': 'Enter the task details',
                            },
                            'done': {
                                'type': 'boolean',
                                'title': 'Done?',
                                'default': False,
                            },
                        },
                    },
                },
            },
        },
        ui_schema={'tasks': {'items': {'details': {'ui:widget': 'textarea'}}}},
    )


class ArraysExampleModel(models.Model):
    arrays = ReactJSONSchemaField(
        help_text='Arrays',
        schema={
            'definitions': {
                'Thing': {
                    'type': 'object',
                    'properties': {'name': {'type': 'string', 'default': 'Default name'}},
                }
            },
            'type': 'object',
            'properties': {
                'listOfStrings': {
                    'type': 'array',
                    'title': 'A list of strings',
                    'items': {'type': 'string', 'default': 'bazinga'},
                },
                'multipleChoicesList': {
                    'type': 'array',
                    'title': 'A multiple choices list',
                    'items': {'type': 'string', 'enum': ['foo', 'bar', 'fuzz', 'qux']},
                    'uniqueItems': True,
                },
                'minItemsList': {
                    'type': 'array',
                    'title': 'A list with a minimal number of items',
                    'minItems': 3,
                    'items': {'$ref': '#/definitions/Thing'},
                },
                'defaultsAndMinItems': {
                    'type': 'array',
                    'title': 'List and item level defaults',
                    'minItems': 5,
                    'default': ['carp', 'trout', 'bream'],
                    'items': {'type': 'string', 'default': 'unidentified'},
                },
                'nestedList': {
                    'type': 'array',
                    'title': 'Nested list',
                    'items': {
                        'type': 'array',
                        'title': 'Inner list',
                        'items': {'type': 'string', 'default': 'lorem ipsum'},
                    },
                },
                'unorderable': {
                    'title': 'Unorderable items',
                    'type': 'array',
                    'items': {'type': 'string', 'default': 'lorem ipsum'},
                },
                'unremovable': {
                    'title': 'Unremovable items',
                    'type': 'array',
                    'items': {'type': 'string', 'default': 'lorem ipsum'},
                },
                'noToolbar': {
                    'title': 'No add, remove and order buttons',
                    'type': 'array',
                    'items': {'type': 'string', 'default': 'lorem ipsum'},
                },
            },
        },
        ui_schema={
            'listOfStrings': {'items': {'ui:emptyValue': ''}},
            'multipleChoicesList': {'ui:widget': 'checkboxes'},
            'unorderable': {'ui:options': {'orderable': False}},
            'unremovable': {'ui:options': {'removable': False}},
            'noToolbar': {'ui:options': {'addable': False, 'orderable': False, 'removable': False}},
        },
    )


class NumbersExampleModel(models.Model):
    numbers = ReactJSONSchemaField(
        help_text='Numbers',
        schema={
            'type': 'object',
            'title': 'Number fields & widgets',
            'properties': {
                'number': {'title': 'Number', 'type': 'number'},
                'integer': {'title': 'Integer', 'type': 'integer'},
                'numberEnum': {
                    'type': 'number',
                    'title': 'Number enum',
                    'enum': [1, 2, 3],
                },
                'numberEnumRadio': {
                    'type': 'number',
                    'title': 'Number enum',
                    'enum': [1, 2, 3],
                },
                'integerRange': {
                    'title': 'Integer range',
                    'type': 'integer',
                    'minimum': 42,
                    'maximum': 100,
                },
                'integerRangeSteps': {
                    'title': 'Integer range (by 10)',
                    'type': 'integer',
                    'minimum': 50,
                    'maximum': 100,
                    'multipleOf': 10,
                },
            },
        },
        ui_schema={
            'integer': {'ui:widget': 'updown'},
            'numberEnumRadio': {'ui:widget': 'radio', 'ui:options': {'inline': True}},
            'integerRange': {'ui:widget': 'range'},
            'integerRangeSteps': {'ui:widget': 'range'},
        },
    )


class WidgetExampleModel(models.Model):
    widgets = ReactJSONSchemaField(
        help_text='Widgets',
        schema={
            'title': 'Widgets',
            'type': 'object',
            'properties': {
                'stringFormats': {
                    'type': 'object',
                    'title': 'String formats',
                    'properties': {
                        'email': {'type': 'string', 'format': 'email'},
                        'uri': {'type': 'string', 'format': 'uri'},
                    },
                },
                'boolean': {
                    'type': 'object',
                    'title': 'Boolean field',
                    'properties': {
                        'default': {
                            'type': 'boolean',
                            'title': 'checkbox (default)',
                            'description': 'This is the checkbox-description',
                        },
                        'radio': {
                            'type': 'boolean',
                            'title': 'radio buttons',
                            'description': 'This is the radio-description',
                        },
                        'select': {
                            'type': 'boolean',
                            'title': 'select box',
                            'description': 'This is the select-description',
                        },
                    },
                },
                'string': {
                    'type': 'object',
                    'title': 'String field',
                    'properties': {
                        'default': {'type': 'string', 'title': 'text input (default)'},
                        'textarea': {'type': 'string', 'title': 'textarea'},
                        'color': {
                            'type': 'string',
                            'title': 'color picker',
                            'default': '#151ce6',
                        },
                    },
                },
                'secret': {'type': 'string', 'default': "I'm a hidden string."},
                'disabled': {
                    'type': 'string',
                    'title': 'A disabled field',
                    'default': 'I am disabled.',
                },
                'readonly': {
                    'type': 'string',
                    'title': 'A readonly field',
                    'default': 'I am read-only.',
                },
                'widgetOptions': {
                    'title': 'Custom widget with options',
                    'type': 'string',
                    'default': 'I am yellow',
                },
                'selectWidgetOptions': {
                    'title': 'Custom select widget with options',
                    'type': 'string',
                    'enum': ['foo', 'bar'],
                    'enumNames': ['Foo', 'Bar'],
                },
            },
        },
        ui_schema={
            'boolean': {
                'radio': {'ui:widget': 'radio'},
                'select': {'ui:widget': 'select'},
            },
            'string': {
                'textarea': {'ui:widget': 'textarea', 'ui:options': {'rows': 5}},
                'color': {'ui:widget': 'color'},
            },
            'secret': {'ui:widget': 'hidden'},
            'disabled': {'ui:disabled': True},
            'readonly': {'ui:readonly': True},
            'widgetOptions': {'ui:options': {'backgroundColor': 'yellow'}},
            'selectWidgetOptions': {'ui:options': {'backgroundColor': 'pink'}},
        },
    )


class OrderingExampleModel(models.Model):
    ordering = ReactJSONSchemaField(
        help_text='Ordering',
        schema={
            'title': 'A registration form',
            'type': 'object',
            'required': ['firstName', 'lastName'],
            'properties': {
                'password': {'type': 'string', 'title': 'Password'},
                'lastName': {'type': 'string', 'title': 'Last name'},
                'bio': {'type': 'string', 'title': 'Bio'},
                'firstName': {'type': 'string', 'title': 'First name'},
                'age': {'type': 'integer', 'title': 'Age'},
            },
        },
        ui_schema={
            'ui:order': ['firstName', 'lastName', '*', 'password'],
            'age': {'ui:widget': 'updown'},
            'bio': {'ui:widget': 'textarea'},
            'password': {'ui:widget': 'password'},
        },
    )


class ReferencesExampleModel(models.Model):
    references = ReactJSONSchemaField(
        help_text='',
        schema={
            'definitions': {
                'address': {
                    'type': 'object',
                    'properties': {
                        'street_address': {'type': 'string'},
                        'city': {'type': 'string'},
                        'state': {'type': 'string'},
                    },
                    'required': ['street_address', 'city', 'state'],
                },
                'node': {
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string'},
                        'children': {
                            'type': 'array',
                            'items': {'$ref': '#/definitions/node'},
                        },
                    },
                },
            },
            'type': 'object',
            'properties': {
                'billing_address': {
                    'title': 'Billing address',
                    '$ref': '#/definitions/address',
                },
                'shipping_address': {
                    'title': 'Shipping address',
                    '$ref': '#/definitions/address',
                },
                'tree': {'title': 'Recursive references', '$ref': '#/definitions/node'},
            },
        },
        ui_schema={'ui:order': ['shipping_address', 'billing_address', 'tree']},
    )


class ErrorsExampleModel(models.Model):

    errors = ReactJSONSchemaField(
        help_text='Errors',
        schema={
            'title': 'Contextualized errors',
            'type': 'object',
            'properties': {
                'firstName': {
                    'type': 'string',
                    'title': 'First name',
                    'minLength': 8,
                    'pattern': '\\d+',
                },
                'active': {'type': 'boolean', 'title': 'Active'},
                'skills': {
                    'type': 'array',
                    'items': {'type': 'string', 'minLength': 5},
                },
                'multipleChoicesList': {
                    'type': 'array',
                    'title': 'Pick max two items',
                    'uniqueItems': True,
                    'maxItems': 2,
                    'items': {'type': 'string', 'enum': ['foo', 'bar', 'fuzz']},
                },
            },
        },
        ui_schema={},
    )


class LargeExampleModel(models.Model):
    large = ReactJSONSchemaField(
        help_text='Large',
        schema={
            'definitions': {
                'largeEnum': {
                    'type': 'string',
                    'enum': [
                        'option #0',
                        'option #1',
                        'option #2',
                        'option #3',
                        'option #4',
                        'option #5',
                        'option #6',
                        'option #7',
                        'option #8',
                        'option #9',
                        'option #10',
                        'option #11',
                        'option #12',
                        'option #13',
                        'option #14',
                        'option #15',
                        'option #16',
                        'option #17',
                        'option #18',
                        'option #19',
                        'option #20',
                        'option #21',
                        'option #22',
                        'option #23',
                        'option #24',
                        'option #25',
                        'option #26',
                        'option #27',
                        'option #28',
                        'option #29',
                        'option #30',
                        'option #31',
                        'option #32',
                        'option #33',
                        'option #34',
                        'option #35',
                        'option #36',
                        'option #37',
                        'option #38',
                        'option #39',
                        'option #40',
                        'option #41',
                        'option #42',
                        'option #43',
                        'option #44',
                        'option #45',
                        'option #46',
                        'option #47',
                        'option #48',
                        'option #49',
                        'option #50',
                        'option #51',
                        'option #52',
                        'option #53',
                        'option #54',
                        'option #55',
                        'option #56',
                        'option #57',
                        'option #58',
                        'option #59',
                        'option #60',
                        'option #61',
                        'option #62',
                        'option #63',
                        'option #64',
                        'option #65',
                        'option #66',
                        'option #67',
                        'option #68',
                        'option #69',
                        'option #70',
                        'option #71',
                        'option #72',
                        'option #73',
                        'option #74',
                        'option #75',
                        'option #76',
                        'option #77',
                        'option #78',
                        'option #79',
                        'option #80',
                        'option #81',
                        'option #82',
                        'option #83',
                        'option #84',
                        'option #85',
                        'option #86',
                        'option #87',
                        'option #88',
                        'option #89',
                        'option #90',
                        'option #91',
                        'option #92',
                        'option #93',
                        'option #94',
                        'option #95',
                        'option #96',
                        'option #97',
                        'option #98',
                        'option #99',
                    ],
                }
            },
            'title': 'A rather large form',
            'type': 'object',
            'properties': {
                'string': {'type': 'string', 'title': 'Some string'},
                'choice1': {'$ref': '#/definitions/largeEnum'},
                'choice2': {'$ref': '#/definitions/largeEnum'},
                'choice3': {'$ref': '#/definitions/largeEnum'},
                'choice4': {'$ref': '#/definitions/largeEnum'},
                'choice5': {'$ref': '#/definitions/largeEnum'},
                'choice6': {'$ref': '#/definitions/largeEnum'},
                'choice7': {'$ref': '#/definitions/largeEnum'},
                'choice8': {'$ref': '#/definitions/largeEnum'},
                'choice9': {'$ref': '#/definitions/largeEnum'},
                'choice10': {'$ref': '#/definitions/largeEnum'},
            },
        },
        ui_schema={'choice1': {'ui:placeholder': 'Choose one'}},
    )


class DateAndTimeExampleModel(models.Model):
    date_and_time = ReactJSONSchemaField(
        help_text='Date and time',
        schema={
            'title': 'Date and time widgets',
            'type': 'object',
            'properties': {
                'native': {
                    'title': 'Native',
                    'description': 'May not work on some browsers, notably Firefox Desktop and IE.',
                    'type': 'object',
                    'properties': {
                        'datetime': {'type': 'string', 'format': 'date-time'},
                        'date': {'type': 'string', 'format': 'date'},
                    },
                },
                'alternative': {
                    'title': 'Alternative',
                    'description': 'These work on most platforms.',
                    'type': 'object',
                    'properties': {
                        'alt-datetime': {'type': 'string', 'format': 'date-time'},
                        'alt-date': {'type': 'string', 'format': 'date'},
                    },
                },
            },
        },
        ui_schema={
            'alternative': {
                'alt-datetime': {
                    'ui:widget': 'alt-datetime',
                    'ui:options': {'yearsRange': [1980, 2030]},
                },
                'alt-date': {
                    'ui:widget': 'alt-date',
                    'ui:options': {'yearsRange': [1980, 2030]},
                },
            }
        },
    )


class ValidationExampleModel(models.Model):
    validation = ReactJSONSchemaField(
        help_text='Validation',
        schema={
            'title': 'Custom validation',
            'description': 'This form defines custom validation rules checking that the two passwords match.',
            'type': 'object',
            'properties': {
                'pass1': {'title': 'Password', 'type': 'string', 'minLength': 3},
                'pass2': {'title': 'Repeat password', 'type': 'string', 'minLength': 3},
                'age': {'title': 'Age', 'type': 'number', 'minimum': 18},
            },
        },
        ui_schema={
            'pass1': {'ui:widget': 'password'},
            'pass2': {'ui:widget': 'password'},
        },
    )


class FileTestModel(models.Model):
    file = ReactJSONSchemaField(
        help_text='Files',
        schema={
            'title': 'Files',
            'type': 'object',
            'properties': {
                'file': {
                    'type': 'string',
                    'format': 'data-url',
                    'title': 'Single file',
                },
                'files': {
                    'type': 'array',
                    'title': 'Multiple files',
                    'items': {'type': 'string', 'format': 'data-url'},
                },
            },
        },
        ui_schema={},
    )


class AlternativesExample(models.Model):
    alternatives = ReactJSONSchemaField(
        help_text='Alternatives',
        schema={
            'definitions': {
                'Color': {
                    'title': 'Color',
                    'type': 'string',
                    'anyOf': [
                        {'type': 'string', 'enum': ['#ff0000'], 'title': 'Red'},
                        {'type': 'string', 'enum': ['#00ff00'], 'title': 'Green'},
                        {'type': 'string', 'enum': ['#0000ff'], 'title': 'Blue'},
                    ],
                }
            },
            'title': 'Image editor',
            'type': 'object',
            'required': ['currentColor', 'colorMask', 'blendMode'],
            'properties': {
                'currentColor': {'$ref': '#/definitions/Color', 'title': 'Brush color'},
                'colorMask': {
                    'type': 'array',
                    'uniqueItems': True,
                    'items': {'$ref': '#/definitions/Color'},
                    'title': 'Color mask',
                },
                'colorPalette': {
                    'type': 'array',
                    'title': 'Color palette',
                    'items': {'$ref': '#/definitions/Color'},
                },
                'blendMode': {
                    'title': 'Blend mode',
                    'type': 'string',
                    'enum': ['screen', 'multiply', 'overlay'],
                    'enumNames': ['Screen', 'Multiply', 'Overlay'],
                },
            },
        },
        ui_schema={'blendMode': {'ui:enumDisabled': ['multiply']}},
    )


class PropertyDependenciesExample(models.Model):

    property_dependencies = ReactJSONSchemaField(
        help_text='Property dependencies',
        schema={
            'title': 'Property dependencies',
            'description': 'These samples are best viewed without live validation.',
            'type': 'object',
            'properties': {
                'unidirectional': {
                    'title': 'Unidirectional',
                    'src': 'https://spacetelescope.github.io/understanding-json-schema'
                    '/reference/object.html#dependencies',
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string'},
                        'credit_card': {'type': 'number'},
                        'billing_address': {'type': 'string'},
                    },
                    'required': ['name'],
                    'dependencies': {'credit_card': ['billing_address']},
                },
                'bidirectional': {
                    'title': 'Bidirectional',
                    'src': 'https://spacetelescope.github.io/understanding-json-schema'
                    '/reference/object.html#dependencies',
                    'description': 'Dependencies are not bidirectional, '
                    'you can, of course, define the bidirectional dependencies explicitly.',
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string'},
                        'credit_card': {'type': 'number'},
                        'billing_address': {'type': 'string'},
                    },
                    'required': ['name'],
                    'dependencies': {
                        'credit_card': ['billing_address'],
                        'billing_address': ['credit_card'],
                    },
                },
            },
        },
        ui_schema={},
    )


class SchemaDependenciesExampleModel(models.Model):
    schema_dependencies = ReactJSONSchemaField(
        help_text='Schema dependencies',
        schema={
            'title': 'Schema dependencies',
            'description': 'These samples are best viewed without live validation.',
            'type': 'object',
            'properties': {
                'simple': {
                    'src': 'https://spacetelescope.github.io/understanding-json-schema'
                    '/reference/object.html#dependencies',
                    'title': 'Simple',
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string'},
                        'credit_card': {'type': 'number'},
                    },
                    'required': ['name'],
                    'dependencies': {
                        'credit_card': {
                            'properties': {'billing_address': {'type': 'string'}},
                            'required': ['billing_address'],
                        }
                    },
                },
                'conditional': {'title': 'Conditional', '$ref': '#/definitions/person'},
                'arrayOfConditionals': {
                    'title': 'Array of conditionals',
                    'type': 'array',
                    'items': {'$ref': '#/definitions/person'},
                },
            },
            'definitions': {
                'person': {
                    'title': 'Person',
                    'type': 'object',
                    'properties': {
                        'Do you have any pets?': {
                            'type': 'string',
                            'enum': ['No', 'Yes: One', 'Yes: More than one'],
                            'default': 'No',
                        }
                    },
                    'required': ['Do you have any pets?'],
                    'dependencies': {
                        'Do you have any pets?': {
                            'oneOf': [
                                {'properties': {'Do you have any pets?': {'enum': ['No']}}},
                                {
                                    'properties': {
                                        'Do you have any pets?': {'enum': ['Yes: One']},
                                        'How old is your pet?': {'type': 'number'},
                                    },
                                    'required': ['How old is your pet?'],
                                },
                                {
                                    'properties': {
                                        'Do you have any pets?': {'enum': ['Yes: More than one']},
                                        'Do you want to get rid of any?': {'type': 'boolean'},
                                    },
                                    'required': ['Do you want to get rid of any?'],
                                },
                            ]
                        }
                    },
                }
            },
        },
        ui_schema=(),
    )


class MultipleExampleModel(models.Model):
    first = ReactJSONSchemaField(
        help_text='First field',
        schema={
            'title': 'A form',
            'description': 'Demonstrates two RJSF fields can be used simultaneously.',
            'type': 'object',
            'required': ['firstName'],
            'properties': {
                'firstName': {'type': 'string', 'title': 'First name'},
            },
        },
        ui_schema={
            'firstName': {'ui:autofocus': True, 'ui:emptyValue': ''},
        },
    )
    second = ReactJSONSchemaField(
        help_text='Second field',
        schema={
            'title': 'Another form',
            'description': 'Demonstrates two RJSF fields can be used simultaneously.',
            'type': 'object',
            'required': ['lastName'],
            'properties': {
                'lastName': {'type': 'string', 'title': 'Last name'},
            },
        },
    )
