import pytest

from django.core.exceptions import ValidationError

from testapp.models import (
    SchemaModel,
    ExtraMediaSchemaModel,
    RenderMethodSchemaModel,
    RenderMethodWithObjectSchemaModel,
    InvalidSchemaModel,
)


@pytest.mark.django_db
@pytest.mark.parametrize(
    'field_name,field_value',
    [
        ('test_field', 1),
        ('test_field', '3ch'),
        ('test_field', '12characters'),
        ('unknown_field', True),
    ],
)
def test_validation(field_name, field_value):
    obj = SchemaModel(json_field={'test_field': '6chars'})
    obj.full_clean()

    obj.json_field[field_name] = field_value
    with pytest.raises(ValidationError) as excinfo:
        obj.full_clean()

    assert str(excinfo.value) == "{'json_field': ['This field has errors.']}"


@pytest.mark.django_db
@pytest.mark.parametrize('blank_value', [None, {}, []])
def test_blank_values(blank_value, get_schema_model):
    model = get_schema_model()
    obj = model(json_field=blank_value)
    with pytest.raises(ValidationError) as excinfo:
        obj.full_clean()

    assert str(excinfo.value) in (
        "{'json_field': ['This field cannot be blank.']}",
        "{'json_field': ['This field cannot be null.']}",
    )

    model = get_schema_model(optional=True)
    obj = model(json_field=blank_value)


@pytest.mark.django_db
def test_extra_form_media():
    obj = ExtraMediaSchemaModel(json_field={'test_field': '6chars'})
    widget = obj._meta.get_field('json_field').formfield().widget
    assert widget.media._css == {'all': ['css/django_reactive.css', 'path/to/my/css/file.css']}
    assert widget.media._js == [
        'dist/react.js',
        'dist/react-dom.js',
        'dist/react-jsonschema-form.js',
        'js/django_reactive.js',
        'path/to/my/js/file.js',
    ]


@pytest.mark.django_db
def test_on_render():
    obj = RenderMethodSchemaModel(json_field={'test_field': 'testing'})
    widget = obj._meta.get_field('json_field').formfield().widget
    initial_max_length = 10
    initial_schema = {
        'title': 'TestSchema',
        'type': 'object',
        'required': ['test_field'],
        'properties': {
            'test_field': {
                'type': 'string',
                'maxLength': initial_max_length,
                'minLength': 5,
            },
            'another_test_field': {
                'type': 'string',
            },
        },
        'additionalProperties': False,
    }
    initial_ui_schema = {
        'test_field': {'ui:help': 'Max 10'},
    }
    assert widget.schema == initial_schema
    assert widget.ui_schema == initial_ui_schema

    widget.mutate()

    assert widget.schema['properties']['test_field']['maxLength'] > initial_max_length
    assert int(widget.ui_schema['test_field']['ui:help'].split()[1]) > initial_max_length


@pytest.mark.django_db
@pytest.mark.parametrize('condition', [True, False])
def test_on_render_object(condition):
    obj = RenderMethodWithObjectSchemaModel.objects.create(
        is_some_condition=condition, json_field={'test_field': 'testing'}
    )
    widget = obj._meta.get_field('json_field').formfield().widget
    widget.on_render_object = obj
    widget.mutate()

    help_text = 'Condition is set' if condition else 'Condition is unset'
    assert widget.ui_schema == {'test_field': {'ui:help': help_text}}


def test_schema_validation():
    obj = InvalidSchemaModel(invalid_json_schema_field={'test_field': '6chars'})
    field = obj._meta.get_field('invalid_json_schema_field')
    errors = field.check()
    assert len(errors) == 1
    assert (
        errors[0].msg
        == "JSON schema is not valid: properties.test_field.type: 'incorrect' is not valid under any of the given schemas"
    )
