=====
Usage
=====

To use django-reactive in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_react_json_schema_form.apps.DjangoReactJsonSchemaFormConfig',
        ...
    )

Add django-reactive's URL patterns:

.. code-block:: python

    from django_react_json_schema_form import urls as django_react_json_schema_form_urls


    urlpatterns = [
        ...
        url(r'^', include(django_react_json_schema_form_urls)),
        ...
    ]
