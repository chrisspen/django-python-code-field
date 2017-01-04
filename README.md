Python Source Code Field
==========================

[![](https://img.shields.io/pypi/v/django-python-code-field.svg)](https://pypi.python.org/pypi/django-python-code-field) [![Build Status](https://img.shields.io/travis/chrisspen/django-python-code-field.svg?branch=master)](https://travis-ci.org/chrisspen/django-python-code-field) [![](https://pyup.io/repos/github/chrisspen/django-python-code-field/shield.svg)](https://pyup.io/repos/github/chrisspen/django-python-code-field)

If you need to store python source code in a field in a django model, this
is the app you need.

Obviously, you should not be accepting any old user data if you will be
executing it, but for my use case (admin users only, needed complex data
rules that varied between models), python code was the best choice.

So, you use it by:

    * ``$ python setup.py install``
    
    * add ``python_field`` to your ``settings.INSTALLED_APPS`` (optional, but
      required if you want syntax highlighting).
    
    * Use as follows in your model::
    
        from django.db import models
        from python_field.fields import PythonCodeField
        
        class MyModel(models.Model):
            ....
            source = PythonCodeField(blank=True, null=True)
            
            ....

The text will be compiled using the inbuild python ``compile()`` function,
and errors will be shown in the form errors field.

CodeMirror and Syntax Highlighting
-------------------------------------

This package uses parts of the CodeMirror package for syntax highlighting, 
and for replacing the ``textarea`` with an editable iframe.

Parts of the CodeMirror package that are not required have not been included,
and the package has been minified. [This is not the case just yet.]

The original license file is included for your reference.

CodeMirror can be found at http://codemirror.net/

Development
-----------

Tests require the Python development headers to be installed, which you can install on Ubuntu with:

    sudo apt-get install python-dev python3-dev python3.4-dev

To run unittests across multiple Python versions, install:

    sudo apt-get install python3.4-minimal python3.4-dev python3.5-minimal python3.5-dev

To run all [tests](http://tox.readthedocs.org/en/latest/):

    export TESTNAME=; tox

To run tests for a specific environment (e.g. Python 2.7 with Django 1.4):
    
    export TESTNAME=; tox -e py27-django15

To run a specific test:
    
    export TESTNAME=.testTimezone2; tox -e py27-django15

To run the [documentation server](http://www.mkdocs.org/#getting-started) locally:

    mkdocs serve -a :9999

To [deploy documentation](http://www.mkdocs.org/user-guide/deploying-your-docs/), run:

    mkdocs gh-deploy --clean

To build and deploy a versioned package to PyPI, verify [all unittests are passing](https://travis-ci.org/chrisspen/django-python-code-field), and then run:

    python setup.py sdist
    python setup.py sdist upload
