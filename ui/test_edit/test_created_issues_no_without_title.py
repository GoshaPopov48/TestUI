from playwright.sync_api import expect
from ui.pages.issues_page import IssuesPage
from conftest import authenticated_page
import pytest
import uuid
import time



def test_created_issues_no_valid_title(authenticated_page,):
    suffix = uuid.uuid4().hex[:9]
    page = authenticated_page
    create_project = IssuesPage(page)
    page.goto("http://localhost:8081/issues/test")
            
    create_project.create_issue()
    create_project.data_for_issues(title=" ", description="Описание")
    button = page.locator('[data-test="submit-button"]')
    if expect(button).to_be_disabled():
        page.screenshot(
                    path=f"screenshots/error_created_issues/NovalidTitle/Test_{suffix}.png"
                )
    print("Кнопка создания задачи заблокирована")
    
    time.sleep(2)