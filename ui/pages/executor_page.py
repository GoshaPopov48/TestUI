from playwright.sync_api import Page, expect


class ExecutorPage:
    def __init__(self, page: Page):
        self.page = page
        self.executor = page.locator('[data-test="field"]').filter(has=page.get_by_text("Исполнитель", exact=True)).get_by_role("combobox")
        
        
    
    def enter_exexutor(self):
            self.executor.click()
            expect(self.executor).to_have_attribute("aria-expanded", "true")
            print(self.page.get_by_role("option").all_text_contents())
    
    def change_executor(self, name_executor: str):
        new_executor = self.page.locator('[data-test="list-item-details"]').filter(has_text=name_executor)
        
        new_executor.click()
        
        expect(self.executor).to_contain_text(name_executor)