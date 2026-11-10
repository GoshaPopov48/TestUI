import pytest
from config.settings import Settings
from framework.pages.login_page import LoginPage
from utils.screenshots import take_screen



@pytest.mark.parametrize(
    "username, password, expect_result",
    [ 
    ("goshass", "admin", "error"),
    ("jfsd sdf sd", "admin", "error"),
    ("1234124fds", "admin", "error"),
    ]
)
def test_no_valid_login_auth(page, username, password, expect_result):
    page.goto(Settings.LOGIN_URL)
    
    login_page = LoginPage(page)
    
    login_page.auth(username, password)
    
    if expect_result == "error":
        
        login_page.should_show_auth_error()
        
    take_screen(page, "AuthErrorName")