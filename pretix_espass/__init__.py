from django.apps import AppConfig
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from pretix.base.plugins import PluginType


class EspassApp(AppConfig):
    name = 'pretix_espass'
    verbose_name = "esPass tickets"

    class PretixPluginMeta:
        type = PluginType.ADMINFEATURE
        name = "esPass Tickets"
        author = _("ligi")
        version = '1.0.0'
        description = "Provides esPass ticket download support"
        visible = True
        version = '0.0'

    def ready(self):
        from . import signals  # NOQA

    @cached_property
    def compatibility_warnings(self):
        errs = []
        try:
            from PIL import Image  # NOQA
        except ImportError:
            errs.append("Pillow is not installed on this system, which is required for converting and scaling images.")
        return errs


default_app_config = 'pretix_espass.EspassApp'
