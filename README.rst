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

Add django-reactive's URL patterns:

.. code-block:: python

    from django_react_json_schema_form import urls as django_react_json_schema_form_urls


    urlpatterns = [
        ...
        url(r'^', include(django_react_json_schema_form_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
