from framework.pages.project_page import ProjectPage
from config.settings import Settings


def test_delete_project(authenticated_page, delete_project):
    
    page = authenticated_page
    
    project_page = ProjectPage(page)
    project_page.btn_click()
    project_page.should_not_contain_project(delete_project)