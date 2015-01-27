from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar.items import Break
from cms.cms_toolbar import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK
from cms.toolbar_base import CMSToolbar

@toolbar_pool.register
class ChapterToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER, _('Training Portal'))
        position = admin_menu.find_first(Break, identifier=ADMINISTRATION_BREAK)
        menu = admin_menu.get_or_create_menu('add_chapters', _('Chapter'), position=position)
        url = reverse('admin:trainingPortal_chapter_add')
        url2 = reverse('admin:trainingPortal_chapter_changelist')
        menu.add_sideframe_item(_('View Chapters'), url=url2)
        menu.add_sideframe_item(_('Create Chapter'), url=url)
        admin_menu.add_break('chapters-break', position=menu)
		
@toolbar_pool.register
class PageToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER, _('Training Portal'))
        position = admin_menu.find_first(Break, identifier=ADMINISTRATION_BREAK)
        menu = admin_menu.get_or_create_menu('add_page', _('Page'), position=position)
        url = reverse('admin:trainingPortal_page_add')
        url2 = reverse('admin:trainingPortal_page_changelist')
        menu.add_sideframe_item(_('View Pages'), url=url2)
        menu.add_sideframe_item(_('Create Page'), url=url)
        admin_menu.add_break('pages-break', position=menu)