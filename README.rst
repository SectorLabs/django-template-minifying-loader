django-template-minifying-loader
================================

Django application, providing simple template loader. It reduces HTML output in templates by stripping out whitespace characters between HTML and django template tags. This is an update of `django-template-minifier <https://github.com/iRynek/django-template-minifier>`_ that works with django 1.10.

Things to note:

* It **does not** make any fancy compression, to do that use `GZip Middleware <https://docs.djangoproject.com/en/dev/ref/middleware/#module-django.middleware.gzip>`_.

* To compress CSS and JS use `django-compressor <https://github.com/jezdez/django_compressor>`_.


Installation
------------

* via `virtualenv <http://www.virtualenv.org/en/latest/#what-it-does>`_ - yup we highly recommend it!

.. code-block:: bash
 
  pip install django-template-minifying-loader

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
                        'template_minifying_loader.loaders.filesystem.Loader',
                        'template_minifying_loader.loaders.app_directories.Loader',
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
                'template_minifying_loader.loaders.filesystem.Loader',
                'template_minifying_loader.loaders.app_directories.Loader',
            ],
        },
    },
  ]

Be happy having less spaces and new lines in Your templates!


Advanced usage:
---------------

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

Known issues:
-------------
* Don't use // one line comments in Your inline javascript &lt;script&gt; or .js templates. In some cases, if You are using lot of {% if %} there, it can comment out }; or }, for example:

.. code-block:: js

  // comment something - !!it's evil!!
  {% if %}
  function name(){
  }
  {% endif %}

**Use /* */ instead**

.. code-block:: js

  /* comment something - it's nice and clean <3! */
  {% if %}
  function name(){
  }
  {% endif %}

Or just set TEMPLATE_MINIFIER_TEMPLATE_TAGS = False


To do:
------
* {% new_line %} template_tag
