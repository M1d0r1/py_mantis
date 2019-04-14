from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.soap import SoapHelper
from selenium.webdriver.support.ui import Select


class Application:
    def __init__(self, browser = "firefox", baseurl = "http://localhost/addressbook", username = "user", password = "pass"):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unknown browser %s" % browser)
        self.wd.implicitly_wait(3)
        self.soap = SoapHelper(self)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.baseurl = baseurl
        self.username = username
        self.password = password


    def open_start_page(self):
        wd = self.wd
        if wd.current_url.endswith("/login_page.php") and len(wd.find_element_by_xpath("//input[@value='Login']")) > 0:
            return
        else:
            self.wd.get(self.baseurl)

    def fill_text_field(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_file_field(self, field_name, path):
        wd = self.wd
        if path is not None:
            wd.find_element_by_name(field_name).send_keys(path)

    def fill_date_field(self, day_field, month_field, year_field, date):
        wd = self.wd
        if date is not None:
            Select(wd.find_element_by_name(day_field)).select_by_visible_text(str(date.day))
            Select(wd.find_element_by_name(month_field)).select_by_index(date.month)
            wd.find_element_by_name(year_field).clear()
            wd.find_element_by_name(year_field).send_keys(str(date.year))

    # noinspection PyStatementEffect,PyBroadException
    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
