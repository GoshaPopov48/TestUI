from ui.components.comment_component import CommentComponent
from playwright.sync_api import Page


class CommentPage:
    def __init__(self, page: Page):
        self.page = page
        self.commentComponent = CommentComponent(page)
    
    def new_comment(self, comment: str):
        self.commentComponent.place_comment(comment)
    
    def add_comment(self):
        self.commentComponent.button_comment()

