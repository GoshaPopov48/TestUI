from playwright.sync_api import Page


class ComponentLogin:
    def __init__(self, page: Page):
        self.page = page
        
        self.username = page.locator('[data-test="username-field"]')
        
        self.password = page.locator('[data-test="password-field"]')
        
        self.remember_me_checkbox = page.locator('[data-test="ring-checkbox"]')
        
        self.login_button = page.locator('[data-test="login-button"]')

    def fill_username(self, username):
        self.username.fill(username)
    
    def fill_password(self, password):
        self.password.fill(password)
        
    def remember_me(self):
        self.remember_me.check()
        
    def click_login(self):
        self.login_button.click()
        
    def login(self, username: str, password: str):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()