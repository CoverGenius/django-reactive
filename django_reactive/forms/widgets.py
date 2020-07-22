import json

from typing import Optional

from django.forms.widgets import Widget
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class ReactJSONSchemaFormWidget(Widget):
    class Media:
        css = {"all": ("css/django_reactive.css",)}
        js = (
            "dist/react.js",
            "dist/react-dom.js",
            "dist/react-jsonschema-form.js",
            "js/django_reactive.js",
        )

    template_name = "django_reactive.html"

    def __init__(self, schema: dict, ui_schema: Optional[dict] = None, **kwargs):
        self.schema = schema
        self.ui_schema = ui_schema
        super().__init__(**kwargs)

    def render(self, name, value, attrs=None, renderer=None):
        context = {
            "data": value,
            "name": name,
            "schema": json.dumps(self.schema),
            "ui_schema": json.dumps(self.ui_schema) if self.ui_schema else "{}",
        }

        return mark_safe(render_to_string(self.template_name, context))
