from framework.pages.issues_page import IssuesPage
from config.settings import Settings


def test_delete_issue(authenticated_page, issue_ready_to_delete):
    title_issue, project_id = issue_ready_to_delete
    
    page = authenticated_page
    page.goto(f"{Settings.PROJECT_URL}/{project_id}/issues")
    
    issue_page = IssuesPage(page)
    issue_page.select_issue(title_issue)
    issue_page.delete_issue()
    
    issue_page.should_not_contain_issue(title_issue)