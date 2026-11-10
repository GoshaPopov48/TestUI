import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, expect
from framework.pages.project_page import ProjectPage
from framework.pages.issues_page import IssuesPage
from framework.pages.login_page import LoginPage
from framework.pages.comment_page import CommentPage
from config.settings import Settings
from test_data.factories import (
    generate_project_name,
    generate_project_id_name,
    generate_issue_title,
    generate_issue_description,
    generate_comment
)



load_dotenv()

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as pl:
        yield pl

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(
        headless=False
    )
    
    yield browser
    
    browser.close()
    
@pytest.fixture
def context(browser):
    context = browser.new_context()
    
    yield context
    
    context.close()
    
@pytest.fixture
def page(context):
    page = context.new_page()
    
    yield page
    
@pytest.fixture
def authenticated_page(page):
    page.goto(Settings.LOGIN_URL)
    
    login_page = LoginPage(page)
    
    login_page.auth(
        Settings.UI_USERNAME,
        Settings.UI_PASSWORD
    )
    
    expect(page).to_have_url(
        Settings.DASHBOARD_URL,
        timeout=15000
    )
    
    return page

@pytest.fixture
def create_project(authenticated_page):
    project_name = generate_project_name("TestProject")
    project_id = generate_project_id_name("TP")
    
    page = authenticated_page
    page.goto(Settings.PROJECT_URL)
        
    project_page = ProjectPage(page)
    
    project_page.new_project()
    project_page.choice_type()
    project_page.fill_data(project_name, project_id)
    project_page.create_project()
    project_page.skipping_setting()
    
    yield project_name, project_id
    page.goto(f"{Settings.PROJECT_URL}")
        
    project_page = ProjectPage(page)
    project_page.open_span(project_name)
    project_page.choose_delete()
    project_page.fii_input(project_name)
    project_page.btn_click()

# Для тестирования удаления задачи
@pytest.fixture
def create_issue(authenticated_page, create_project):
    issue_title = generate_issue_title("TestIssue")
    issue_description = generate_issue_description("Desc test")
    
    page = authenticated_page
    _ , project_id = create_project
    
    page.goto(f"{Settings.PROJECT_URL}/{project_id}/issues")
    
    issue_page = IssuesPage(page)
    issue_page.new_issue()
    issue_page.issue_data(issue_title, issue_description)
    issue_page.create_issue()

    return issue_title, issue_description, project_id
    
    
    

# Для тестирования создания задачи 
@pytest.fixture
def create_issue_cleanup(authenticated_page, create_issue):
    page = authenticated_page
    title_issue, _, project_id = create_issue
    
    page.goto(f"{Settings.PROJECT_URL}/{project_id}/issues")
    
    return title_issue, project_id

@pytest.fixture
def issue_ready_to_delete(authenticated_page, create_issue):
    page = authenticated_page
    title_issue, _ , project_id = create_issue
    
    page.goto(f"{Settings.PROJECT_URL}/{project_id}/issues")

    return title_issue, project_id

@pytest.fixture
def add_comment_for_issue(authenticated_page, create_issue):
    page = authenticated_page
    title_issue, _ , project_id = create_issue
    issue_id = f"{project_id}-1"
    page.goto(f"{Settings.PROJECT_URL}/{project_id}/issues/{issue_id}")
    
    comment_page = CommentPage(page)
    comment = generate_comment("Comment")
    
    comment_page.new_comment(comment)
    
    return comment, project_id, title_issue


@pytest.fixture
def delete_project(authenticated_page):
    project_name = generate_project_name("TestProject")
    project_id = generate_project_id_name("TP")

    page = authenticated_page
    page.goto(Settings.PROJECT_URL)

    project_page = ProjectPage(page)
    project_page.new_project()
    project_page.choice_type()
    project_page.fill_data(project_name, project_id)
    project_page.create_project()
    project_page.skipping_setting()

    page.goto(f"{Settings.PROJECT_URL}")
    
    project_page.open_span(project_name)
    project_page.choose_delete()
    project_page.fii_input(project_name)
    
    return project_name
