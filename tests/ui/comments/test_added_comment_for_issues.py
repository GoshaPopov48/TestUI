from framework.pages.comment_page import CommentPage



def test_added_comment(authenticated_page, add_comment_for_issue):
    page = authenticated_page
    comment, _, _ = add_comment_for_issue
    
    comment_page = CommentPage(page)
    comment_page.add_comment()
    
    comment_page.should_comment(comment)
    
    