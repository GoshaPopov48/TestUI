from framework.pages.issues_page import IssuesPage
from config.settings import Settings



def test_created_issues(authenticated_page, create_issue_cleanup):
    issue_title, project_id = create_issue_cleanup
    
    page = authenticated_page
    
    page.goto(f"{Settings.PROJECT_URL}/{project_id}/issues")
    
    issue_page = IssuesPage(page)
    
    issue_page.should_contain_issue(issue_title)