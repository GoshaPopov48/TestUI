from playwright.sync_api import Page
from ui.components.component_issues import CreatedIssues




class IssuesPage:
    def __init__(self, page: Page):
        self.page = page
        self.CreatedIssues = CreatedIssues(page)
        
    def choice_issues(self):
        self.CreatedIssues.choice_issue()
            
    def delete_issues(self):
        self.CreatedIssues.delete_issue()
            
    def create_issue(self):
        self.CreatedIssues.create_issue()
            
    def data_for_issues(self, title, description):
        self.CreatedIssues.title_desc_for_issue(title, description)
        
    def button_created_isseus(self):
        self.CreatedIssues.button_issue()