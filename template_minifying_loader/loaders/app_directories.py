from django.template.loaders.app_directories import Loader as AppDirectoriesLoader
from ..mixins import TemplateMinifierMixin


class Loader(TemplateMinifierMixin, AppDirectoriesLoader):
    pass

