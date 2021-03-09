from .widgets import ReactJSONSchemaFormWidget

try:
    # DJANGO 3.1
    from django.forms import JSONField
except ImportError:
    from django.contrib.postgres.forms.jsonb import JSONField


class ReactJSONSchemaFormField(JSONField):
    widget = ReactJSONSchemaFormWidget
