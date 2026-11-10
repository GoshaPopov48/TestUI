from playwright.sync_api import Page

from framework.base.base_page import BasePage

from framework.components.issues.issue_form_component import IssueFormComponent
from framework.components.issues.issue_list_component import IssueListComponent
from framework.components.issues.issue_actions_component import IssueActionsComponent


class IssuesPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.issue_form = IssueFormComponent(page)
        self.issue_list = IssueListComponent(page)
        self.issue_actions = IssueActionsComponent(page)
    
    def new_issue(self):
        self.issue_form.open_form()
        
    def issue_data(self, title: str, description: str):
        self.issue_form.fill_data(title, description)
    
    def create_issue(self):
        self.issue_form.create()        
        

    def select_issue(self, title: str):
        self.issue_list.select_issue(title)

    def delete_issue(self):
        self.issue_actions.delete()

    def should_contain_issue(self, title: str):
        self.issue_list.should_contain_issue(title)

    def should_not_contain_issue(self, title: str):
        self.issue_list.should_not_contain_issue(title)
    
    def submit_button_disabled(self):
        self.issue_form.disabled_button()