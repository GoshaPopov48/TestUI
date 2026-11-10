from playwright.sync_api import expect
from framework.base.base_component import BaseComponent



class CommentListComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)
        
        self.comment = self.page.locator(
            '[data-test="comment-content"]'
        )
        
    def should_contain_comment(self, comment: str):
        expect(
            self.comment.filter(has_text=comment)
        ).to_be_visible()
        
    def should_not_contain_comment(self, comment: str):
        expect(
            self.comments.filter(has_text=comment)
        ).not_to_be_visible()
