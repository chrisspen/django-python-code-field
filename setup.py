from distutils.core import setup

import python_field

setup(
    name = "django-python-code-field",
    version = python_field.__version__,
    description = "Store python source code (syntax checked) in database.",
    url = "https://github.com/chrisspen/django-python-code-field/",
    author = "Chris Spencer",
    author_email = "chrisspen@gmail.com",
    packages = [
        "python_field",
    ],
    classifiers = [
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Programming Language :: Python :: 2.7',
        'Environment :: Web Environment',
    ],
    zip_safe = False,
    install_requires = ['Django>=1.4'],
)
