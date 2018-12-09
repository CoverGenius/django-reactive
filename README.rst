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

In our opinion, `JSON types <https://www.postgresql.org/docs/10/datatype-json.html>`_ is an extremely useful feature of
Postgres. It helps developers to combine relational and non-relational approaches to storing data which in many cases
can significantly simplify database design for web applications.

The `JSONField  <https://docs.djangoproject.com/en/2.1/ref/contrib/postgres/fields/#jsonfield>`_ in Django provides a
nice way of integrating **json** and **jsonb** Postgres types with the ORM in that way that we even can include such
fields in database queries. Considering **jsonb** type offers a way of indexing JSON documents it becomes a powerful
tool in the application design opening a wide range of use cases, e.g. polymorphic behaviour, storing complex
hierarchies and lists of related entities.

However, the main limitation of JSONField in Django is that it does not offer a nice way of configuring such objects in
default admin UI. Defining JSON objects inside the textarea is not practical for most use cases. Thus, django-reactive
tries to close this gap by offering an integration of JSONField with an awesome
`react-jsonschema-form <https://github.com/mozilla-services/react-jsonschema-form>`_ (RJSF) JS library and Python's
`jsonschema <https://github.com/Julian/jsonschema>` for backend validation. Such integration from our practice can
significantly reduce an amount of work you need to spend on building custom forms for JSONField types.

In this case developers only need to come up with JSON schema for such field and optionally UI schema to modify behavior
of such forms.

The simplest example would looks like this:

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

Will generate a form like shown on the screenshot below:

.. image:: images/simple.png

Quickstart
----------

Install django-reactive::

    pip install django-reactive

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_reactive.apps.DjangoReactJsonSchemaFormConfig',
        ...
    )

Features
--------

* React, RJSF and other JS assets are bundled with the package.
* Integration with default Django admin theme.
* Backend adn frontend validation.

Limitations
-----------

* `Additional properties <https://github.com/mozilla-services/react-jsonschema-form#expandable-option>`_ feature of
**RJSF** is not supported. To implement this behaviour you can define an array schema with one property serving as a key
of the object and do transformation in your JSON class. An example will be provided later.

Future development
------------------

* Display description in the form as a tooltip.
* Polish styles and HTML generated by **RJSF**.
