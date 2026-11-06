
from playwright.sync_api import Page





class CommentComponent:
    def __init__(self, page: Page):
        self.page = page
        self.comment = page.locator('[data-test="wysiwyg-editor-content"]')
        self.button = page.get_by_role("button", name="Добавить комментарий")

    def place_comment(self, comment: str):
        self.comment.fill(comment)
        
    def button_comment(self):
        self.button.click()
    