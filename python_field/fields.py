import django
from django.db import models
from django import forms

import six

unicode = six.text_type # pylint: disable=redefined-builtin

class PythonCodeWidget(forms.Textarea):
    def render(self, name, value, attrs=None):
        """
        TODO: have a syntax hilight feature, where instead of a TextArea,
        you get a div that can be double-clicked in to make it editable,
        and after leaving it re-highlights.
        """
        if value is None:
            value = ""
        if attrs is None:
            attrs = {}
        if attrs.has_key('class'):
            attrs['class'] += " python-code"
        else:
            attrs['class'] = "python-code"
        return super(PythonCodeWidget, self).render(name, value, attrs=attrs)
    
    class Media:
        js = (
            "admin/js/jquery.min.js",
            "python_field/js/codemirror.js",
            "python_field/js/python_field.js",
        )
        css = {
            'all':(
                "python_field/css/line-numbers.css",
            )
        }

class PythonCodeFormField(forms.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['widget'] = PythonCodeWidget
        super(PythonCodeFormField, self).__init__(*args, **kwargs)
    
    def clean(self, value):
        """
        We need to ensure that the code that was entered validates as
        python code.
        """
        
        if not value:
            return
        
        if isinstance(value, six.string_types):
            try:
                value = value.replace('\r', '')
                compile(value, "<string>", 'exec')
            except SyntaxError as e:
                raise forms.ValidationError(u'Syntax Error: %s' % unicode(e))
            return value

class PythonCodeField(models.TextField):
    """
    A field that will ensure that data that is entered into it is syntactically
    valid python code.
    """
    
    # SubfieldBase was removed in Django 1.10.
    # http://stackoverflow.com/a/36744699/247542
    if django.VERSION < (1, 10, 0):
        __metaclass__ = models.SubfieldBase
        
    description = "Python Source Code"
    
    def formfield(self, **kwargs):
        return super(PythonCodeField, self).formfield(form_class=PythonCodeFormField, **kwargs)
        
    def from_db_value(self, value, expression, connection, context):
        return value

    def to_python(self, value):
        return value
    
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], [r'^python_field\.fields\.PythonCodeField'])
except ImportError:
    pass
