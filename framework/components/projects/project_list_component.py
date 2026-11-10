from playwright.sync_api import Page, expect

from framework.base.base_component import BaseComponent



class ProjectListComponent(BaseComponent):

    def __init__(self, page):
        super().__init__(page)
        
        self.rows = self.page.locator('[data-test="project"]')
        
    def should_contain_project(self, project_name: str):
        project = self.page.locator(
            f'[data-test="project"][data-test-name="{project_name}"]'
        )
        expect(project).to_be_visible()
        
    def not_should_contain_project(self, project_name: str):
            project = self.page.locator(
                f'[data-test="project"][data-test-name="{project_name}"]'
            )
            expect(project).not_to_be_visible()