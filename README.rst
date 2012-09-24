Python Source Code Field
==========================

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