=============================
django-reactive
=============================

.. image:: https://badge.fury.io/py/django-reactive.svg
    :target: https://badge.fury.io/py/django-reactive

.. image:: https://travis-ci.org/tyomo4ka/django-reactive.svg?branch=master
    :target: https://travis-ci.org/tyomo4ka/django-reactive

.. image:: https://codecov.io/gh/tyomo4ka/django-reactive/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/tyomo4ka/django-reactive

Integrates react-json-schema-form in Django Forms.

Documentation
-------------

Django reactive integrates `react-jsonschema-form <https://github.com/mozilla-services/react-jsonschema-form>`_ in
your Django project.
The full documentation is at https://django-reactive.readthedocs.io.

Quickstart
----------

Install django-reactive::

    pip install django-reactive

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_react_json_schema_form.apps.DjangoReactJsonSchemaFormConfig',
        ...
    )

Features
--------

* Find a way to display description in the form
