import pytest
from playwright.sync_api import expect
from conftest import authenticated_page
import time
from ui.pages.executor_page import ExecutorPage

@pytest.mark.parametrize(
    "executor", [
        "Георгий Попов",
        "Тестер тестер"
    ]
)
def test_changed_executor(authenticated_page, executor):
    page = authenticated_page
    page.goto("http://localhost:8081/projects/DEMO/issues/DEMO-2/Pervye-shagi-polzovatelya")
    
    issue = ExecutorPage(page)
    
    issue.enter_exexutor()
    issue.change_executor(executor)
    
    page.reload()
    
    issue = ExecutorPage(page)
    
    expect(issue.executor).to_contain_text(executor)
    time.sleep(3)
    
