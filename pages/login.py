from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

    @property
    def main(self):
        return self.driver.find_element(By.TAG_NAME, 'body')

    @property
    def login_mbs_form(self):
        return self.main.find_element(By.CLASS_NAME, 'container')
    
    @property
    def login_mbs_form_test(self):
        return self.main.find_element(By.CLASS_NAME, 'test')

    @property
    def login_mbs_form_elements(self):
        _elements = {
            'login': self.login_mbs_form.find_element(By.ID, "ReportUsers_login"),
            'pass': self.login_mbs_form.find_element(By.ID, "ReportUsers_password"),
            'submit-mbs': self.login_mbs_form.find_element(By.ID, "submit")
        }
        return _elements

    def fill_mbs_login_form_and_submit(self, mail, password):
          try:
            self.login_mbs_form_elements['login'].send_keys(mail)
            self.login_mbs_form_elements['pass'].send_keys(password)
            self.login_mbs_form_elements['submit-mbs'].click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "yw0")))
          except: pass

