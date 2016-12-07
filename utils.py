import re

from django.conf import settings


def strip_spaces_in_template(template_source):
    """
    Default function used to preprocess templates.

    Use settings.TEMPLATE_MINIFIER_HTML_TAGS or
    settings.TEMPLATE_MINIFIER_TEMPLATE_TAGS to change
    its behaviour.

    To use Your own stripping function do not change this function, use
    **settings.TEMPLATE_MINIFIER_STRIP_FUNCTION property**!
    """
    if (getattr(settings, 'TEMPLATE_MINIFIER_HTML_TAGS', True)):
        template_source = re.sub(r'>\s+<', '><', template_source)

    if (getattr(settings, 'TEMPLATE_MINIFIER_TEMPLATE_TAGS', True)):
        template_source = re.sub(r'\s+{ ?%', ' {%', template_source)
        template_source = re.sub(r'% ?}\s+', '%} ', template_source)

    return template_source


def get_template_minifier_strip_function():
    """
    Getting proper template strip function, taking into consideration
    TEMPLATE_MINIFIER_STRIP_FUNCTION setting.
    """
    if getattr(settings, 'TEMPLATE_MINIFIER_STRIP_FUNCTION', False):
        return settings.TEMPLATE_MINIFIER_STRIP_FUNCTION
    else:
        return strip_spaces_in_template
