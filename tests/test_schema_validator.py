from django_reactive.schema_validator import validate_json_schema


def test_valid_json_schema():
    schema = {
        'type': 'object',
        'properties': {
            'name': {'type': 'string'},
            'age': {'type': 'integer'},
        },
    }
    result, errors = validate_json_schema(schema)
    assert result
    assert errors == []


def test_invalid_json_schema():
    schema = {
        'type': 'object',
        'properties': {
            'name': {'type': 'string'},
            'age': {'type': 'invalid'},  # Invalid type for age property
        },
    }
    result, errors = validate_json_schema(schema)
    assert not result
    assert errors == ["properties.age.type: 'invalid' is not valid under any of the given schemas"]
