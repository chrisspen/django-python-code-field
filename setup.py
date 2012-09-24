from distutils.core import setup

setup(
    name = "django-python-code-field",
    version = "0.1.0",
    description = "Store python source code (syntax checked) in database.",
    url = "http://bitbucket.org/schinckel/django-python-code-field/",
    author = "Matthew Schinckel",
    author_email = "matt@schinckel.net",
    packages = [
        "python_field",
        
    ],
    classifiers = [
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django',
    ],
)
