from django.conf import settings

from .utils import get_template_minifier_strip_function


class TemplateMinifierMixin:

    def get_contents(self, origin):
        content = super().get_contents(origin)

        allowed_extensions = getattr(settings, 'TEMPLATE_MINIFIER_FILENAME_EXTENSIONS', ('.html', '.htm'))
        if not origin.template_name.endswith(allowed_extensions):
            return content

        exclude_dirs = getattr(settings, 'TEMPLATE_MINIFIER_EXCLUDED_DIRS', ('admin/', ))
        if origin.template_name.startswith(exclude_dirs):
            return content

        if getattr(settings, 'TEMPLATE_MINIFIER', True):
            content = get_template_minifier_strip_function()(content)

        return content