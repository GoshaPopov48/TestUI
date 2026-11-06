from playwright.sync_api import Page
from ui.components.component_project import CreateProjectComponents


class ProjectPage:
    def __init__(self, page: Page):
        self.page = page
        self.CreateProjectComponents = CreateProjectComponents(page)
    
    def new_project(self):
        self.CreateProjectComponents.open_new_project()
        
    def choice_type(self):
        self.CreateProjectComponents.select_template()
    
    def fill_data(self, name: str, project_id: str):
        self.CreateProjectComponents.fill_project_data(name, project_id)
    
    def created_project(self):
        self.CreateProjectComponents.created_project()
    
    def skipping_setting(self):
        self.CreateProjectComponents.skip_setting()
        