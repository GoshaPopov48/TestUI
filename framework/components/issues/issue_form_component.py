from playwright.sync_api import expect
from framework.base.base_component import BaseComponent



class IssueFormComponent(BaseComponent):
    
    def __init__(self, page):
        super().__init__(page)
        
        self.open_button = self.page.locator('[data-test="ring-button-set"]')
        
        self.title = self.page.get_by_placeholder("Введите Заголовок")
        
        self.description = self.page.locator('[data-test="wysiwyg-editor-content"]')
        
        self.submit_button = self.page.locator('[data-test="submit-button"]')
        
        
    def open_form(self):
        self.open_button.click()
    
    def fill_data(self, title: str, description: str):
        self.title.fill(title)
        self.description.fill(description)
        
    
    def create(self):
        self.submit_button.click()

    def should_be_open(self):
        expect(self.title).to_be_visible()
        
    def disabled_button(self):
        expect(self.submit_button).to_be_disabled()