import re

from django.conf import settings
from django.utils.module_loading import import_string


def strip_spaces_in_template(template_source):
    """
    Default function used to preprocess templates.

    To use Your own stripping function do not change this function, use
    **settings.TEMPLATE_MINIFIER_STRIP_FUNCTION property**!
    """

    # remove comments
    template_source = re.sub(r'{#.*#}', '', template_source)

    # strip whitespace between html tags
    template_source = re.sub(r'>\s+<', '><', template_source, flags=re.MULTILINE)

    # strip whitespace around django variables
    template_source = re.sub(r'>\s+{{', '>{{', template_source, flags=re.MULTILINE)
    template_source = re.sub(r'}}\s+<', '}}<', template_source, flags=re.MULTILINE)

    # strip whitespace around django and html tags
    template_source = re.sub(r'>\s+{%', '>{%', template_source, flags=re.MULTILINE)
    template_source = re.sub(r'%}\s+<', '%}<', template_source, flags=re.MULTILINE)

    # strip whitespace between django tags
    template_source = re.sub(r'%}\s+{%', '%}{%', template_source, flags=re.MULTILINE)

    # strip whitespace between django tags and variables
    template_source = re.sub(r'%}\s+{{', '%}{{', template_source, flags=re.MULTILINE)
    template_source = re.sub(r'}}\s+{%', '}}{%', template_source, flags=re.MULTILINE)

    # condense any white space
    template_source = re.sub(r'\s{2,}', ' ', template_source, flags=re.MULTILINE)

    # strip leading and trailing html
    template_source = template_source.strip()

    return template_source


def get_template_minifier_strip_function():
    """
    Getting proper template strip function, taking into consideration
    TEMPLATE_MINIFIER_STRIP_FUNCTION setting.
    """
    if getattr(settings, 'TEMPLATE_MINIFIER_STRIP_FUNCTION', False):
        fce = import_string(settings.TEMPLATE_MINIFIER_STRIP_FUNCTION)
        return fce
    else:
        return strip_spaces_in_template
