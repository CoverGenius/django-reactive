from jsonschema import Draft7Validator


def validate_json_schema(schema: dict) -> tuple[bool, list[str]]:
    """
    Validate a JSON schema using the Draft 7 validator.
    """
    validator = Draft7Validator(
        schema=Draft7Validator.META_SCHEMA,
        format_checker=Draft7Validator.FORMAT_CHECKER,
    )
    errors = [f"{'.'.join(e.path)}: {e.message}" for e in validator.iter_errors(schema)]

    return not bool(errors), errors
