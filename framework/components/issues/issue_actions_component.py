from framework.base.base_component import BaseComponent


class IssueActionsComponent(BaseComponent):

    def __init__(self, page):
        super().__init__(page)

        self.delete_button = self.page.locator(
            '[data-test="delete-item-button"]'
        )

        self.confirm_delete_button = self.page.get_by_role(
            "button",
            name="OK"
        )

    def delete(self):
        self.delete_button.click()
        self.confirm_delete_button.click()