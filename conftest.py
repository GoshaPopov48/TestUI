import pytest
import os
import uuid
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, expect
from ui.pages.login_page import LoginPage

load_dotenv()

# Фикстура для авторизации теста UI
@pytest.fixture
def authenticated_page():
    with sync_playwright() as pl:
        browser = pl.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            page.goto("http://localhost:8081/hub/auth/login")

            login_page = LoginPage(page)
            login_page.auth(
                os.getenv("UI_USERNAME"),
                os.getenv("UI_PASSWORD")
            )

            expect(page).to_have_url(
                "http://localhost:8081/dashboard",
                timeout=15000
            )

            yield page

        finally:
            browser.close()