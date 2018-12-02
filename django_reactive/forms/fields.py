from django.contrib.postgres.forms.jsonb import JSONField

from .widgets import ReactJSONSchemaFormWidget


class ReactJSONSchemaFormField(JSONField):
    widget = ReactJSONSchemaFormWidget

    def widget_attrs(self, widget):
        pass
