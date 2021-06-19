from django.template.loaders.filesystem import Loader as FilesystemLoader
from ..mixins import TemplateMinifierMixin


class Loader(TemplateMinifierMixin, FilesystemLoader):
    pass