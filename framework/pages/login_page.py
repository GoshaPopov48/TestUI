from playwright.sync_api import Page, expect

from framework.base.base_page import BasePage
from framework.components.auth.login_component import LoginComponent


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.login_component = LoginComponent(page)

    def auth(self, username: str, password: str):
        self.login_component.login(username, password)
        
    def should_show_auth_error(self):
        expect(
        self.page.get_by_text("Некорректное имя пользователя или пароль.")
        ).to_be_visible()