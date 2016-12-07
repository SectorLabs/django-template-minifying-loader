from django.conf import settings
from django.template.loaders.app_directories import Loader as AppDirectoriesLoader
from django.template import Template

from ..utils import get_template_minifier_strip_function


class Loader(AppDirectoriesLoader):

    def get_template(self, template_name, template_dirs=None, skip=None):
        template = super().get_template(template_name, template_dirs)

        template_source = template.source
        if getattr(settings, 'TEMPLATE_MINIFIER', True):
            template_source = get_template_minifier_strip_function()(template.source)

        return Template(
            template_source,
            template.origin,
            template.name,
            template.engine
        )
