
from conftest import authenticated_page
from ui.pages.project_page import ProjectPage
import time
import uuid


def  test_created_project(authenticated_page):
    suffix = uuid.uuid4().hex[:3]
    page = authenticated_page
    
    page.goto("http://localhost:8081/projects")
    project = ProjectPage(page)
    
    project.new_project()
    project.choice_type()
    project.fill_data(
        name = f"Test_{suffix}",
        project_id = suffix)
    project.created_project()
    project.skipping_setting()
    