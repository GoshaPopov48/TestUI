from playwright.sync_api import expect
from framework.base.base_component import BaseComponent


class IssueListComponent(BaseComponent):

    def __init__(self, page):
        super().__init__(page)

        self.rows = self.page.locator(
            'tr[data-test^="ring-table-row"]'
        )

    def get_issue(self, title: str):
        return self.rows.filter(has_text=title)

    def select_issue(self, title: str):
        issue = self.get_issue(title)

        expect(issue).to_be_visible()

        checkbox = issue.locator(
            '[data-test="ring-checkbox"] input'
        )

        checkbox.check()

    def should_contain_issue(self, title: str):
        expect(
            self.get_issue(title)
        ).to_be_visible()

    def should_not_contain_issue(self, title: str):
        expect(
            self.get_issue(title)
        ).not_to_be_visible()