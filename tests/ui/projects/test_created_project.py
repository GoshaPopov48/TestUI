from framework.pages.project_page import ProjectPage
from config.settings import Settings






def  test_created_project(authenticated_page, create_project):
    project_name, _ = create_project
    
    page = authenticated_page
    
    page.goto(f"{Settings.PROJECT_URL}")
    
    project_page = ProjectPage(page)
    
    project_page.should_contain_project(project_name)
    

    
    