from playwright.sync_api import Page
from ui.components.component_login import ComponentLogin




class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.ComponentLogin = ComponentLogin(page)
        
    def auth(self, username: str, password: str):
        self.ComponentLogin.login(username, password)