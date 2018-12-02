from django.contrib.postgres.fields import JSONField as BaseJSONField

from .forms.fields import ReactJSONSchemaFormField
from .forms.widgets import ReactJSONSchemaFormWidget


class ReactJSONSchemaField(BaseJSONField):

    def __init__(self, schema=None, **kwargs):
        self.schema = schema
        kwargs['default'] = kwargs.get('default', dict)
        super().__init__(**kwargs)

    def formfield(self, **kwargs):
        return ReactJSONSchemaFormField(widget=ReactJSONSchemaFormWidget(
            schema=self.schema,
        ), **kwargs)
