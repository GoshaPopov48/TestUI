
from ui.pages.issues_page import IssuesPage
from conftest import authenticated_page
import time


def test_delete_project(authenticated_page):
    page =  authenticated_page
    page.goto("http://localhost:8081/issues/test")
    
    issues_page = IssuesPage(page)
    
    issues_page.choice_issues()
    issues_page.delete_issues()
    