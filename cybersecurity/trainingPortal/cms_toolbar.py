from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar


@toolbar_pool.register
class PortalToolbar(CMSToolbar):
    def populate(self):
        if self.is_current_app:
            menu = self.toolbar.get_or_create_menu('Trainingportal', _('Training Portal'))
            url = reverse('index')