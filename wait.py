import contextlib

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, TimeoutException, \
    WebDriverException
import selenium.webdriver.support.ui as ui
import time


class WaitLocatorTypes(object):
    """
    Set of supported locator strategies.
    """
    ID = By.ID
    CLASS_NAME = By.CLASS_NAME
    PARTIAL_LINK_TEXT = By.PARTIAL_LINK_TEXT
    CSS_SELECTOR = By.CSS_SELECTOR
    NAME = By.NAME
    XPATH = By.XPATH
    TAG_NAME = By.TAG_NAME


class Wait(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait_time = 10
        self.WebDriverWait = WebDriverWait(self.driver, self.wait_time)

    def wait_element(self, locator_type, locator_value, timeout):
        try:
            ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((locator_type,
                                                                                           locator_value)))
            return True
        except TimeoutException:
            return False

    def wait_until_presence_of_element_located(self, locator_type, locator_value):
        try:
            self.WebDriverWait.until(EC.presence_of_element_located((locator_type, locator_value)))
        except WebDriverException:
            return False

    def element_to_be_clickable(self, locator_type, locator_value):
        try:
            self.WebDriverWait.until(EC.element_to_be_clickable((locator_type, locator_value)))
        except WebDriverException as exception:
                    # print exception
                    return False