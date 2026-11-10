from playwright.sync_api import Page

from framework.base.base_page import BasePage
from framework.components.comments.comment_component import CommentComponent
from framework.components.comments.comment_list_component import CommentListComponent

class CommentPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.comment_list_component = CommentListComponent(page)
        self.comment_component = CommentComponent(page)

    def new_comment(self, comment: str):
        self.comment_component.place_comment(comment)

    def add_comment(self):
        self.comment_component.button_comment()
        
    def should_comment(self, comment):
        self.comment_list_component.should_contain_comment(comment)
        
    def not_should_comment(self, comment):
        self.comment_list_component.should_not_contain_comment(comment)
        