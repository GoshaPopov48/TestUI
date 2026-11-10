from playwright.sync_api import Page, expect

from framework.base.base_component import BaseComponent


class ProjectComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page)

        self.new_project = self.page.get_by_role(
            "link",
            name="Новый проект"
        )

        self.template = self.page.get_by_role(
            "button",
            name="Управление задачами Упрощенный проект для повседневного управления задачами"
        )

        self.use_template = self.page.get_by_role(
            "button",
            name="Использовать шаблон"
        )

        self.project_name = self.page.get_by_placeholder(
            "Введите имя проекта"
        )

        self.project_id = self.page.locator(
            '[data-test="project-id"]'
        )

        self.create_button = self.page.get_by_role(
            "button",
            name="Создать проект"
        )

        self.skip_setup = self.page.get_by_role(
            "button",
            name="Пропустить настройку и перейти к проекту"
        )
        
        self.row_settings = self.page.locator(
            '[data-test="ring-dropdown"]'
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

    def create_project(self):
        self.create_button.click()

    def skip_setting(self):
        expect(self.skip_setup).to_be_visible()
        self.skip_setup.click()
        
    def delete(self):
        self.row_settings().click()
        