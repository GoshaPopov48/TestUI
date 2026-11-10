from framework.base.base_component import BaseComponent
from playwright.sync_api import Page, expect






class ProjectActionsComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)
        
        self.project_actions_menu = page.locator(
            '[data-test="project-menu"]'
            )
        
        self.action_delete = page.locator(
            '[data-test="ring-list-item-label"][title="Удалить"]'
            )
        
        self.project_name_input = self.page.locator(
            '[data-test~="ring-dialog"] [data-test="ring-input"] input'
            )
        
        self.button_delete = self.page.get_by_role(
            "button", name="Удалить проект"
            )
        
        
    def action_menu(self, project_name):
        project = self.page.locator(
            f'[data-test="project"][data-test-name="{project_name}"]'
        )
        project.locator('[data-test="project-menu"]').click()
    
    def action_deleted(self):
        self.action_delete.click()
    
    def project_label(self, project):
        self.project_name_input.fill(project)
    
    def button_deleted(self):
        self.button_delete.click()
