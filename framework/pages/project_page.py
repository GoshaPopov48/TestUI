from playwright.sync_api import Page

from framework.base.base_page import BasePage
from framework.components.projects.project_component import ProjectComponent
from framework.components.projects.project_list_component import ProjectListComponent
from framework.components.projects.project_actions_component import ProjectActionsComponent


class ProjectPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.project_list = ProjectListComponent(page)
        self.project_component = ProjectComponent(page)
        self.project_actions = ProjectActionsComponent(page)

    def new_project(self):
        self.project_component.open_new_project()

    def choice_type(self):
        self.project_component.select_template()

    def fill_data(self, name: str, project_id: str):
        self.project_component.fill_project_data(name, project_id)

    def create_project(self):
        self.project_component.create_project()

    def skipping_setting(self):
        self.project_component.skip_setting()
        
    def should_contain_project(self, project_name):
        self.project_list.should_contain_project(project_name)
        
    def should_not_contain_project(self, project_name):
            self.project_list.not_should_contain_project(project_name)
            
    def open_span(self, project_name):
        self.project_actions.action_menu(project_name)
    
    def choose_delete(self):
        self.project_actions.action_deleted()
        
    def fii_input(self, project: str):
        self.project_actions.project_label(project)
        
    def btn_click(self):
        self.project_actions.button_deleted()
        