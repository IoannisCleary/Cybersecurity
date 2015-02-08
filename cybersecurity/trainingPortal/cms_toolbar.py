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
@toolbar_pool.register
class QuizToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER, _('Training Portal'))
        position = admin_menu.find_first(Break, identifier=ADMINISTRATION_BREAK)
        menu = admin_menu.get_or_create_menu('add_quiz', _('Quiz'), position=position)
        url = reverse('admin:quiz_category_add')
        menu.add_sideframe_item(_('Create Category'), url=url)
        url3 = reverse('admin:quiz_subcategory_add')
        menu.add_sideframe_item(_('Create SubCategory'), url=url3)
        url2 = reverse('admin:quiz_quiz_add')
        url4 = reverse('admin:quiz_quiz_changelist')
        menu.add_sideframe_item(_('Create Quiz'), url=url2)
        menu.add_sideframe_item(_('View Quizzes'), url=url4)
        admin_menu.add_break('quiz-break', position=menu)
@toolbar_pool.register
class QuestionsToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER, _('Training Portal'))
        position = admin_menu.find_first(Break, identifier=ADMINISTRATION_BREAK)
        menu = admin_menu.get_or_create_menu('add_question', _('Questions'), position=position)
        menu.add_sideframe_item(_('Create MultipleChoiceType'), url="/admin/multichoice/mcquestion/add/")
        menu.add_sideframe_item(_('View MultipleChoiceType'), url="/admin/multichoice/mcquestion/")
        menu.add_sideframe_item(_('Create True/FalseType'), url="/admin/true_false/tf_question/add/")
        menu.add_sideframe_item(_('View True/FalseType'), url="/admin/true_false/tf_question/")
        menu.add_sideframe_item(_('Create EssayType'), url="/admin/essay/essay_question/add/")
        menu.add_sideframe_item(_('View EssayType'), url="/admin/essay/essay_question/")
        admin_menu.add_break('question-break', position=menu)