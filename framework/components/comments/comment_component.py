from playwright.sync_api import Page

from framework.base.base_component import BaseComponent


class CommentComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page)
        self.comment = self.page.locator('[data-test="wysiwyg-editor-content"]')

        self.button = self.page.get_by_role(
            "button",
            name="Добавить комментарий"
        )

    def place_comment(self, comment: str):
        self.comment.fill(comment)

    def button_comment(self):
        self.button.click()