import datetime
import random

from unitspec import SpecTestCase
import requests
import json
import boto3
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class EmsMticketTestCase(SpecTestCase):

    USER_NANE = "newobs"
    USER_PASS =  "orzxnu"
    EVENT_NANE = "Test_Scan"
    HALL_NANE = "Hall_name"


    TEST_NANE = "2systemAgent"

    _URL = None
    USER_MAIL = None
    MAIL_SERVICE_TOKEN = None
    MAIL_BOX_NAME = None

    def get_ssm_param(self, param_id):
        client = boto3.client('ssm', region_name='eu-west-1')
        key = client.get_parameter(
            Name=param_id,
            WithDecryption=True
        )['Parameter']['Value']
        return key

    v_name = "widget-sales-flow{}.mp4".format(datetime.datetime.now()).replace(" ", "-")
    # print(v_name)
    capabilities = {
        "browserName": "chrome",
        # "browserVersion": "97.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False,
            # "screenResolution": "1920x1080",
            "timeout": 45,
            # "videoName": v_name,
            "name": "widget_sales-flow-{}".format(datetime.datetime.now()),
            "enableLog": True
        }
    }

    # driver = webdriver.Remote(
    #    command_executor="http://143.244.181.69:4444/wd/hub",
    #    desired_capabilities=capabilities)
    
    # driver = webdriver.Chrome('C:\chromedriver.exe')
 
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    def tearDown(self):
       self.driver.quit()

    def mark_build(self, is_passed=True):
        self.driver.add_cookie({'name': 'zaleniumTestPassed',
                                'value': str(is_passed).lower()})
        self.driver.quit()


    def runTest(self):
        self.ordered_tests_runner()

    def ordered_tests_runner(self):
        pass

    def get_login_data(self):
        names = "newobs"
        last_n = "orzxnu"
        return {"mail": names,
                "password": last_n}

