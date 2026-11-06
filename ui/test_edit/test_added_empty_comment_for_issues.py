from ui.pages.comment_pages import CommentPage
from conftest import authenticated_page
import uuid
import time


def test_added_empty_comment(authenticated_page):
    page = authenticated_page
    created_comment = CommentPage(page)
    
    page.goto("http://localhost:8081/issue/test-1/Zagolovok")
    
    created_comment.new_comment("Это новый комментарий в данной задачи")
    created_comment.add_comment()

    time.sleep(2)
