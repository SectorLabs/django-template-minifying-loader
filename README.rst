Django Spaceless Templates
==========================

Django application, providing simple template loader. It reduces HTML output in templates by stripping out whitespace
characters between HTML and django template tags. With cached template loader, whitespace stripping is done only once
during template compilation. This is more efficient than solutions based on ``{% spaceless %}`` tag or middleware minification.

This package is based on following unmaintained packages:

* `Django template minifying loader <https://github.com/SectorLabs/django-template-minifying-loader>`_
* `Django template minified <https://github.com/iRynek/django-template-minifier>`_

How much bandwidth does it save? Check data from real project:

================  ========  =================
Normal HTML       109kB     15kB gzipped
Spaceless HTML    67kB      13kB gzipped
**Saved**         **38 %**  **12 % gzipped**
================  ========  =================


Installation
------------

.. code-block:: bash
 
  pip install django-spaceless-templates

Basic usage
-----------

Modify Your Django project settings's module.

**For production** (note cached loader):

.. code-block:: python

  TEMPLATES = [
    {
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            'loaders': [
                (
                    'django.template.loaders.cached.Loader', [
                        'django_spaceless_templates.loaders.filesystem.Loader',
                        'django_spaceless_templates.loaders.app_directories.Loader',
                    ],
                ),
            ],
        },
    },
  ]

**For development** (each refresh reloads template):

.. code-block:: python

  TEMPLATES = [
    {
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            'loaders': [
                'django_spaceless_templates.loaders.filesystem.Loader',
                'django_spaceless_templates.loaders.app_directories.Loader',
            ],
        },
    },
  ]


Settings
--------

Using modified settings You can:

* turn on stripping only for templates with given extensions

.. code-block:: python

  TEMPLATE_MINIFIER_FILENAME_EXTENSIONS = ('.html', '.htm', )

* turn off stripping for particular directories

.. code-block:: python

  TEMPLATE_MINIFIER_EXCLUDED_DIRS = ('admin/', )

* turn off all stripping

.. code-block:: python

  TEMPLATE_MINIFIER = False # default = True

* run Your own strip_function, which preprocess templates

.. code-block:: python

  TEMPLATE_MINIFIER_STRIP_FUNCTION = 'template_minifier.utils.strip_spaces_in_template'

* **use only in production**

.. code-block:: python

  if DEBUG:
    TEMPLATE_MINIFIER = False

Known issues
------------

* Don't use ``//`` one line comments in your inline javascript ``<script>`` tags. **Use /* */ instead**:

.. code-block:: js

  // comment something - !!it's evil!! and cause the rest of JS code is commented out.
  function name() {
  }

  /* comment something - it's nice and clean <3! */
  function name() {
  }

* Don't use multiline ``{% blockquote %}`` without parameter `trimmed <https://docs.djangoproject.com/en/2.1/topics/i18n/translation/#blocktrans-template-tag>`_.
  Otherwise your blockquote translations won't be translated. Correct usage:

.. code-block:: python

    {% blockquote trimmed %}
        My paragraph...
    {% blockquote %}

* To preserve extra space use ``{{ " " }}``:

.. code-block:: html

    <div>Text {{ " " }} {{ variable }}</div>

Running Tests
-------------

::

    (myenv) $ pip install -e .
    (myenv) $ python ./runtests.py

Check package
-------------

.. code-block:: bash

    python -m build; python -m twine check dist/*
