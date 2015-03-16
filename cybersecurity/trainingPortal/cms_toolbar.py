from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar.items import Break
from cms.cms_toolbar import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK
from cms.toolbar_base import CMSToolbar

@toolbar_pool.register
class ProfileToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER, _('Training Portal'))
        position = admin_menu.find_first(Break, identifier=ADMINISTRATION_BREAK)
        menu = admin_menu.get_or_create_menu('add_profile', _('Profiles'), position=position)
        url2 = reverse('admin:trainingPortal_profile_changelist')
        url = reverse('admin:trainingPortal_profile_add')
        menu.add_sideframe_item(_('View Profiles'), url=url2)
        menu.add_sideframe_item(_('Create Profile'), url=url)
@toolbar_pool.register
class DjangoFilerToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER, _('Training Portal'))
        position = admin_menu.find_first(Break, identifier=ADMINISTRATION_BREAK)
        menu = admin_menu.get_or_create_menu('add_file', _('Files'), position=position)
        menu.add_sideframe_item(_('Upload/View Files'), url="/admin/filer/folder/")
        admin_menu.add_break('file-break', position=menu)
@toolbar_pool.register
class AnnouncementToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER, _('Training Portal'))
        position = admin_menu.find_first(Break, identifier=ADMINISTRATION_BREAK)
        menu = admin_menu.get_or_create_menu('add_announcement', _('Announcements'), position=position)
        menu.add_sideframe_item(_('View Announcements'), url="/admin/trainingPortal/announcement/")
        menu.add_sideframe_item(_('Create Announcement'), url="/admin/trainingPortal/announcement/add")
        admin_menu.add_break('file-announcement', position=menu)
@toolbar_pool.register
class IndexeElementToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER, _('Training Portal'))
        position = admin_menu.find_first(Break, identifier=ADMINISTRATION_BREAK)
        menu = admin_menu.get_or_create_menu('add_indexelement', _('Index Element'), position=position)
        menu.add_sideframe_item(_('View Index Elements'), url="/admin/trainingPortal/indexelement/")
        menu.add_sideframe_item(_('Create Index Element'), url="/admin/trainingPortal/indexelement/add")
        admin_menu.add_break('file-indexelement', position=menu)
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
class SectionToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER, _('Training Portal'))
        position = admin_menu.find_first(Break, identifier=ADMINISTRATION_BREAK)
        menu = admin_menu.get_or_create_menu('add_page', _('Section'), position=position)
        url = reverse('admin:trainingPortal_page_add')
        url2 = reverse('admin:trainingPortal_page_changelist')
        menu.add_sideframe_item(_('View Sections'), url=url2)
        menu.add_sideframe_item(_('Create Section'), url=url)
@toolbar_pool.register
class ExerciseToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER, _('Training Portal'))
        position = admin_menu.find_first(Break, identifier=ADMINISTRATION_BREAK)
        menu = admin_menu.get_or_create_menu('add_exercise', _('Exercise'), position=position)
        url = reverse('admin:trainingPortal_exercise_add')
        url2 = reverse('admin:trainingPortal_exercise_changelist')
        menu.add_sideframe_item(_('View Exercises'), url=url2)
        menu.add_sideframe_item(_('Create Exercise'), url=url)
        menu.add_sideframe_item(_('View Section Exercises'), url="/admin/trainingPortal/pageexercise/")
        menu.add_sideframe_item(_('Add to Section'), url="/admin/trainingPortal/pageexercise/add/")
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
        menu.add_sideframe_item(_('View Progress'), url="/admin/quiz/progress/")
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
@toolbar_pool.register
class ForumToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER, _('Training Portal'))
        position = admin_menu.find_first(Break, identifier=ADMINISTRATION_BREAK)
        menu = admin_menu.get_or_create_menu('add_forum', _('Forum'), position=position)
        menu.add_sideframe_item(_('Create Forum'), url="/admin/pybb/forum/add/")
        menu.add_sideframe_item(_('View Forums'), url="/admin/pybb/forum/")
        menu.add_sideframe_item(_('Create Topic'), url="/admin/pybb/topic/add/")
        menu.add_sideframe_item(_('View Topics'), url="/admin/pybb/topic/")
        admin_menu.add_break('forum-break', position=menu)
@toolbar_pool.register
class TestingMoeToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(ADMIN_MENU_IDENTIFIER, _('Training Portal'))
        position = admin_menu.find_first(Break, identifier=ADMINISTRATION_BREAK)
        menu = admin_menu.get_or_create_menu('testing_mode', _('Testing Mode'), position=position)
        menu.add_sideframe_item(_('Enable/Disable'), url="/admin/trainingPortal/mode/1/")
        admin_menu.add_break('testing-break', position=menu)