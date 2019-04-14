from model.project import Project
from selenium.webdriver.support.ui import Select


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    project_cache = None

    def navigate_to_manage_projects_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/manage_proj_page.php") and len(
                wd.find_elements_by_xpath("// input[ @ value = 'Create New Project']")) > 0:
            return
        else:
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        wd = self.app.wd
        wd.find_element_by_xpath("// input[ @ value = 'Create New Project']").click()
        self.fill_form(project)
        wd.find_element_by_xpath("// input[ @ value = 'Add Project']").click()
        self.project_cache = None

    def fill_form(self, project):
        wd = self.app.wd
        self.fill_text_field("name", project.name)
        self.fill_list_field("status", project.status)
        self.fill_list_field("view_state", project.view_status)
        self.fill_text_field("description", project.description)
        if not (wd.find_element_by_name("inherit_global").is_selected() == project.inherit):
            wd.find_element_by_name("inherit_global").click()

    def fill_text_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_list_field(self, field_name, text):
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def get_project_list(self):
        if self.project_cache is None:
            self.navigate_to_manage_projects_page()
            project_cache = []
            for i in range(0, self.count()):
                project = self.get_data_from_projects_page_by_index(i)
                project_cache.append(project)
        # noinspection PyUnboundLocalVariable
        return list(project_cache)

    def count(self):
        wd = self.app.wd
        self.navigate_to_manage_projects_page()
        c = len(wd.find_elements_by_css_selector("table.width100 > tbody > tr.row-1")) + len(
            wd.find_elements_by_css_selector("table.width100 > tbody > tr.row-2"))
        return c

    def get_data_from_projects_page_by_index(self, index):
        wd = self.app.wd
        if index % 2 == 0:
            element = wd.find_elements_by_css_selector("table.width100 > tbody > tr.row-1")[index // 2]
        if index % 2 == 1:
            element = wd.find_elements_by_css_selector("table.width100 > tbody > tr.row-2")[index // 2]
        # noinspection PyUnboundLocalVariable
        name = element.find_elements_by_css_selector("td")[0].text
        project = Project(name=name)
        return project

    def delete_by_name(self, name):
        wd = self.app.wd
        wd.find_element_by_link_text(name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None
