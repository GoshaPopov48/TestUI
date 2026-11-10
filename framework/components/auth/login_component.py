from framework.base.base_component import BaseComponent


class LoginComponent(BaseComponent):

    def __init__(self, page):
        super().__init__(page)

        self.username = self.page.locator(
            '[data-test="username-field"]'
        )

        self.password = self.page.locator(
            '[data-test="password-field"]'
        )

        self.remember_me_checkbox = self.page.locator(
            '[data-test="ring-checkbox"]'
        )

        self.login_button = self.page.locator(
            '[data-test="login-button"]'
        )

    def fill_username(self, username: str):
        self.username.fill(username)

    def fill_password(self, password: str):
        self.password.fill(password)

    def remember_me(self):
        self.remember_me_checkbox.check()

    def click_login(self):
        self.login_button.click()

    def login(self, username: str, password: str):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()