from django.conf import settings
from django.template.loaders.app_directories import Loader as AppDirectoriesLoader

from ..utils import get_template_minifier_strip_function


class Loader(AppDirectoriesLoader):

    def get_contents(self, origin):
        content = super().get_contents(origin)

        if getattr(settings, 'TEMPLATE_MINIFIER', True):
            content = get_template_minifier_strip_function()(content)

        return content

