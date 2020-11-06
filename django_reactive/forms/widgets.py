import json

from django.forms import Media
from django.forms.widgets import Widget
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class ReactJSONSchemaFormWidget(Widget):

    template_name = 'django_reactive.html'

    def __init__(self, schema, ui_schema=None, extra_css=None, extra_js=None, **kwargs):
        self.schema = schema
        self.ui_schema = ui_schema
        self.extra_css = extra_css
        self.extra_js = extra_js
        super(ReactJSONSchemaFormWidget, self).__init__(**kwargs)

    @property
    def media(self):
        css = ['css/django_reactive.css']
        if self.extra_css:
            css.extend(self.extra_css)
        js = [
            'dist/react.js',
            'dist/react-dom.js',
            'dist/react-jsonschema-form.js',
            'js/django_reactive.js',
        ]
        if self.extra_js:
            js.extend(self.extra_js)

        return Media(css={'all': css}, js=js)

    def render(self, name, value, attrs=None, renderer=None):
        context = {
            'data': value,
            'name': name,
            'schema': json.dumps(self.schema),
            'ui_schema': json.dumps(self.ui_schema) if self.ui_schema else '{}',
        }

        return mark_safe(render_to_string(self.template_name, context))
