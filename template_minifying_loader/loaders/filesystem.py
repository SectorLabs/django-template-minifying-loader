from django.conf import settings
from django.template.loaders.filesystem import Loader as FilesystemLoader
from django.template import Template

from ..utils import get_template_minifier_strip_function


class Loader(FilesystemLoader):

    def get_contents(self, origin):
        content = super().get_contents(origin)

        if getattr(settings, 'TEMPLATE_MINIFIER', True):
            content = get_template_minifier_strip_function()(content)

        return content
