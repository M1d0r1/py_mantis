from model.project import Project
from selenium.webdriver.support.ui import Select
import datetime
import re

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def navigate_to_manage_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()


    def create(self, project):
        wd = self.app.wd
        wd.find_element_by_xpath("// input[ @ value = 'Create New Project']").click()
        self.fill_form(project)
        wd.find_element_by_xpath("// input[ @ value = 'Add Project']").click()

    def fill_form(self, project):
        wd = self.app.wd
        self.fill_text_field("name", project.name)
        self.fill_list_field("status", project.status)
        self.fill_list_field("view_state", project.view_status)
        self.fill_text_field("description", project.description)

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
        # if self.contact_cache is None:
            wd = self.app.wd
            self.navigate_to_manage_projects_page()
            project_cache = []
            for i in range(0,2):
                project = self.get_data_from_projects_page_by_index(i)
                project_cache.append(project)
            return list(project_cache)


    def get_data_from_projects_page_by_index(self, index):
        wd = self.app.wd
        element = wd.find_element_by_css_selector("tr.row-%s > td" % str(index+1))
        project = Project(name = element.text)
        return project