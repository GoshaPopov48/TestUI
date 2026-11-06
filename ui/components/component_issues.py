from playwright.sync_api import Page




class CreatedIssues:
    def __init__(self, page: Page):
        self.page = page
        
        self.created_issues = page.locator('[data-test="ring-button-set"]')        
        
        self.title_issues = page.get_by_placeholder("Введите Заголовок")        
        
        self.description_issues = page.locator('[data-test="wysiwyg-editor-content"]')   
        
        self.create_button_issues = page.locator('[data-test="submit-button"]')
        
        self.delete_button = page.locator('[data-test="delete-item-button"]')
                
        self.conf_del_button = page.get_by_role("button", name="OK")
        
        self.row_for_issue = page.locator(
                    'tr[data-test="ring-table-row test-13"]'
                )
                
        self.checkbox = self.row_for_issue.locator(
                    '[data-test="ring-checkbox"] input'
                    )
        
    def choice_issue(self):
        self.checkbox.check()
            
    def delete_issue(self):
        self.delete_button.click()
        self.conf_del_button.click()
            
    def create_issue(self):
        self.created_issues.click()
            
    def title_desc_for_issue(self, title: str, description: str):
        self.title_issues.fill(title)
        self.description_issues.fill(description)
        
    def button_issue(self):
        self.create_button_issues.click()