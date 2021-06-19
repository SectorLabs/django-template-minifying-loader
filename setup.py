from setuptools import find_packages, setup

import django_spaceless_templates

readme = open('README.rst').read()
requirements = open('requirements.txt').readlines()

setup(
    name='django-spaceless-templates',
    version=django_spaceless_templates.__version__,
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Simple Django template loader that minifies html output.',
    long_description=readme,
    long_description_content_type='text/x-rst',
    url='https://github.com/martinsvoboda/django-spaceless-templates',
    author='Martin Svoboda',
    author_email='martin.svoboda@gmail.com',
    keywords=['django', 'template', 'minification', 'html', 'minifier'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=requirements,
)
