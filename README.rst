=============================
django-reactive
=============================

.. image:: https://badge.fury.io/py/django-reactive.svg
    :target: https://badge.fury.io/py/django-reactive

.. image:: https://travis-ci.org/tyomo4ka/django-reactive.svg?branch=master
    :target: https://travis-ci.org/tyomo4ka/django-reactive

.. image:: https://codecov.io/gh/tyomo4ka/django-reactive/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/tyomo4ka/django-reactive

django-reactive integrates `react-jsonschema-form <https://github.com/mozilla-services/react-jsonschema-form>`_ (RJSF)
in Django projects.

Motivation
----------

In my opinion, `JSON types <https://www.postgresql.org/docs/10/datatype-json.html>`_ is an very useful feature of
Postgres which allows to combine relational and non-relational approaches to storing data. In many cases
it leads to simpler database design.

The `JSONField  <https://docs.djangoproject.com/en/2.1/ref/contrib/postgres/fields/#jsonfield>`_ in Django provides a
nice way of integrating **json** and **jsonb** Postgres types with the ORM. ORM can even include JSON fields
in database queries. **jsonb** type also offers a way of indexing JSON documents. That makes it a powerful
tool in the application design and opens a wide range of use cases, e.g. polymorphic behaviour, storing complex
hierarchies and lists of related entities.

However, the main limitation of JSONField in Django is that it does not offer a good way of configuring such objects in
default admin UI. Defining JSON objects inside the textarea is not practical for most use cases. django-reactive
tries to address this problem by offering an integration between JSONField and an awesome
`react-jsonschema-form <https://github.com/mozilla-services/react-jsonschema-form>`_ (RJSF) JS library and Python's
`jsonschema <https://github.com/Julian/jsonschema>` for backend validation. Such integration from our practice can
significantly reduce an amount of work you need to spend on building custom forms for JSONField types.

In this case developers only need to define a JSON schema for such field and optionally UI schema to modify UI
of such forms.

A simple example is shown below:

.. code-block:: python

    from django.db import models

    from django_reactive.fields import ReactJSONSchemaField


    class TestModel(models.Model):
        simple = ReactJSONSchemaField(
            help_text='Simple',
            schema={
                "title": "A registration form",
                "description": "A simple form example.",
                "type": "object",
                "required": [
                    "firstName",
                    "lastName"
                ],
                "properties": {
                    "firstName": {
                        "type": "string",
                        "title": "First name"
                    },
                    "lastName": {
                        "type": "string",
                        "title": "Last name"
                    },
                    "age": {
                        "type": "integer",
                        "title": "Age"
                    },
                    "bio": {
                        "type": "string",
                        "title": "Bio"
                    },
                    "password": {
                        "type": "string",
                        "title": "Password",
                        "minLength": 3
                    },
                    "telephone": {
                        "type": "string",
                        "title": "Telephone",
                        "minLength": 10
                    }
                }
            },
            ui_schema={
                "firstName": {
                    "ui:autofocus": True,
                    "ui:emptyValue": ""
                },
                "age": {
                    "ui:widget": "updown",
                    "ui:title": "Age of person",
                    "ui:description": "(earthian year)"
                },
                "bio": {
                    "ui:widget": "textarea"
                },
                "password": {
                    "ui:widget": "password",
                    "ui:help": "Hint: Make it strong!"
                },
                "date": {
                    "ui:widget": "alt-datetime"
                },
                "telephone": {
                    "ui:options": {
                        "inputType": "tel"
                    }
                }
            },
        )

It will generate a form like this:

.. image:: images/simple.png

Quick start
-----------

Install django-reactive::

    pip install django-reactive

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_reactive.apps.DjangoReactJsonSchemaFormConfig',
        ...
    )

Run example app
---------------

* docker-compose up
* poetry install
* ./example/manage.py makemigrations
* ./example/manage.py migrate
* ./example/manage.py createsuperuser
* ./example/manage.py runserver
* open http://127.0.0.1:8000/admin
* Go to "Test model" to check a few examples

Features
--------

* React, RJSF and other JS assets are bundled with the package.
* Integration with default Django admin theme.
* Backend and frontend validation.

Limitations
-----------

* `Additional properties <https://github.com/mozilla-services/react-jsonschema-form#expandable-option>`_ ( a feature of RJSF) is not supported.

To implement this behaviour you can define an array schema with one property serving as a key of the object and do
transformation in your JSON class. An example will be provided later.

Future development
------------------

* Display description as tooltips
* Polish styles and HTML generated by **RJSF**
