import pytest

from testapp.models import SchemaModel, OptionalSchemaModel


@pytest.fixture
def get_schema_model(optional=False):
    def _inner(optional=optional):
        if optional:
            return OptionalSchemaModel
        return SchemaModel

    return _inner
