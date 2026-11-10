from playwright.sync_api import expect

from config.settings import Settings
from framework.pages.login_page import LoginPage


def test_auth(page):
    
    page.goto(Settings.LOGIN_URL)
    
    login_page = LoginPage(page)
    
    login_page.auth(Settings.UI_USERNAME, Settings.UI_PASSWORD)
    
    expect(page).to_have_url(
        f"{Settings.BASE_URL}/dashboard")