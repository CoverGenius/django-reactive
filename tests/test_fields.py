import pytest

from django.core.exceptions import ValidationError

from testapp.models import SchemaModel, ExtraMediaSchemaModel


@pytest.mark.django_db
@pytest.mark.parametrize(
    "field_name,field_value",
    [("test_field", 1), ("test_field", "3ch"), ("test_field", "12characters"), ("unknown_field", True)],
)
def test_validation(field_name, field_value):
    obj = SchemaModel(json_field={"test_field": "6chars"})
    obj.full_clean()

    obj.json_field[field_name] = field_value
    with pytest.raises(ValidationError) as excinfo:
        obj.full_clean()

    assert str(excinfo.value) == "{'json_field': ['This field has errors.']}"


@pytest.mark.django_db
@pytest.mark.parametrize("blank_value", [None, {}, []])
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
    obj = ExtraMediaSchemaModel(json_field={"test_field": "6chars"})
    widget = obj._meta.get_field("json_field").formfield().widget
    assert widget.media._css == {"all": ["css/django_reactive.css", "path/to/my/css/file.css"]}
    assert widget.media._js == [
        "dist/react.js",
        "dist/react-dom.js",
        "dist/react-jsonschema-form.js",
        "js/django_reactive.js",
        "path/to/my/js/file.js",
    ]
