from playwright.sync_api import expect
from framework.pages.issues_page import IssuesPage
from config.settings import Settings
from test_data.factories import generate_issue_description
from utils.screenshots import take_screen

def test_created_issues_no_valid_title(authenticated_page, create_issue_cleanup):
    title_issue, project_id = create_issue_cleanup
    page = authenticated_page
    page.goto(f"{Settings.PROJECT_URL}/{project_id}/issues")
    
    description = generate_issue_description("This description for task")
    issue_page = IssuesPage(page)
    
    issue_page.new_issue()
    issue_page.issue_data("", description)
    
    issue_page.submit_button_disabled()
    take_screen(page, "ErrorNameIssues")