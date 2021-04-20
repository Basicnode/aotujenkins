from web.page.page import WebPage
from selenium.webdriver.common.by import By

class LoginPage(WebPage):
    url = 'http://flash-admin.enilu.cn/#/login?redirect=%2Fdashboard'
    username_loc = (By.NAME, 'username')
    password_loc = (By.NAME, 'password')
    submit_loc = (By.CLASS_NAME, 'el-button')

    @property
    def username(self):
        return self.find_element(*self.username_loc)

    @property
    def password(self):
        return self.find_element(*self.password_loc)

    @property
    def submit(self):
        return self.find_element(*self.submit_loc)

    def login(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.submit.click()
