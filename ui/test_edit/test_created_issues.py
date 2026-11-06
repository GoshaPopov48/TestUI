
from ui.pages.issues_page import IssuesPage
from conftest import authenticated_page
import uuid
import time

def test_created_project(authenticated_page):
    suffix = uuid.uuid4().hex[:9]
    page = authenticated_page
    create_project = IssuesPage(page)
    page.goto("http://localhost:8081/issues/test")
    
    create_project.create_issue()
    create_project.data_for_issues(
        title=suffix,
        description=suffix
    )
    
    create_project.button_created_isseus()
    time.sleep(3)