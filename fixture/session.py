import time

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        self.app.open_start_page()
        wd = self.app.wd
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        #time.sleep(5)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        self.app.open_start_page()
        self.app.wd.find_element_by_xpath("//a[@onclick='document.logout.submit();']").click()
        # self.app.wd.find_element_by_name("user")

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("logout")) > 0

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def get_logged_user(self):
        return self.app.wd.find_element_by_css_selector("td.login-info-left span").text
