from playwright.sync_api import sync_playwright, expect, Page



class CreateProjectComponents:
    def __init__(self, page: Page):
        self.page = page
        
        self.new_project = page.get_by_role(
            "link", name="Новый проект"
        )

        self.template = page.get_by_role(
            "button",
            name="Управление задачами Упрощенный проект для повседневного управления задачами"
        )

        self.use_template = page.get_by_role(
            "button", name="Использовать шаблон"
        )

        self.project_name = page.get_by_placeholder(
            "Введите имя проекта"
        )

        self.project_id = page.locator(
            '[data-test="project-id"]'
        )

        self.create_button = page.get_by_role(
            "button", name="Создать проект"
        )

        self.skip_setup = page.get_by_role(
            "button", name="Пропустить настройку и перейти к проекту"
        )
        
        
        
    
    def open_new_project(self):
        self.new_project.click()
    
    def select_template(self):
        expect(self.template).to_be_visible()
        self.template.click()
        self.use_template.click()
    
    def fill_project_data(self, name: str, project_id: str):
        self.project_name.fill(name)
        self.project_id.fill(project_id)
    
    def created_project(self):
        self.create_button.click()
    
    def skip_setting(self):
        expect(self.skip_setup).to_be_visible()
        self.skip_setup.click()
        
    
    