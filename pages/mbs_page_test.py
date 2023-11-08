import random
import requests
import urllib.request
from time import sleep
import time
import os

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class MBSPage(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def main(self):
        return self.driver.find_element(By.TAG_NAME, "body")

    @property
    def header_bar(self):
        return self.main.find_element(By.ID, "yw0")

    @property
    def first_reservation(self):
        return self.header_bar.find_element(
            By.CSS_SELECTOR, "[href='/firstBook/index']"
        )

    def open_first_reservation_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.first_reservation)
        ).click()
        sleep(1)


    @property
    def directories_path(self):
        return self.header_bar.find_element(
            By.CSS_SELECTOR, "[href='/provider/shows']"
        )


    def open_directories_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.directories_path)
        ).click()
        sleep(1)


    def open_agents_page(self):
        WebDriverWait(self.driver, 10).until(
          EC.element_to_be_clickable(self.driver.find_element( By.XPATH, "/html/body/div[3]/div/div/div[1]/a[1]" ))).click()
        sleep(1)
        WebDriverWait(self.driver, 10).until(
          EC.element_to_be_clickable(self.driver.find_element( By.XPATH, "/html/body/div[3]/div/div/a[1]" ))).click()
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element( By.CSS_SELECTOR, "[name='DistributeAgents[type]']"))).send_keys('distribute_agents_type')
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element( By.CSS_SELECTOR, "[name='DistributeAgents[name]']"))).send_keys('distribute_agents_name')
        sleep(1)   
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element( By.CSS_SELECTOR, "[name='DistributeAgents[fio]']"))).send_keys('distribute_agents_fio')
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element( By.CSS_SELECTOR, "[name='DistributeAgents[okpo]']"))).send_keys('1122334455')  
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element( By.CSS_SELECTOR, "[name='DistributeAgents[contract]']"))).send_keys('distribute_agents_contract')  
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element( By.CSS_SELECTOR, "[name='DistributeAgents[agentId]']"))).send_keys('903443412344')  
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element( By.XPATH, "//form[contains(@id,'agent-form')]/div[2]/input"  ))).click()
        sleep(1)
        search_distribute_agents_result = self.driver.find_element(
           By.XPATH, "/html/body/div[3]/div/div/table/tbody/tr[1]/td[2]"  
        )
        if search_distribute_agents_result.text == "distribute_agents_name":
            test_delete_agent_result = self.driver.find_element(
               By.XPATH, "/html/body/div[3]/div/div/table/tbody/tr[1]/td[4]/a[2]/i"  
            )
            test_delete_agent_result.click()
            WebDriverWait(self.driver, 10).until(
              EC.presence_of_element_located((By.ID, "agentPopup")))
            WebDriverWait(self.driver, 10).until(
              EC.element_to_be_clickable(self.driver.find_element( By.XPATH, "//div[contains(@id,'agentPopup')]/form/div[2]/input[2]" ))).click()
            print("search and delete works")
            sleep(1)
        else:
            raise Exception(
                "filter failed"
            )       
        sleep(1)
        search_distribute_agents_after_delete = self.driver.find_element(
           By.XPATH, "/html/body/div[3]/div/div/table/tbody/tr[1]/td[2]"  
        )
        if search_distribute_agents_after_delete.text != "distribute_agents_name":
            print("delete agent works")
        else:
            raise Exception(
                "delete new agent not working"
            )
        sleep(1)


    def open_organizers_page(self):
        WebDriverWait(self.driver, 10).until(
          EC.element_to_be_clickable(self.driver.find_element( By.XPATH, "/html/body/div[3]/div/div/div[1]/a[2]" ))).click()
        sleep(1)
        WebDriverWait(self.driver, 10).until(
          EC.element_to_be_clickable(self.driver.find_element( By.XPATH, "/html/body/div[3]/div/div/a[1]" ))).click()
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element( By.CSS_SELECTOR, "[name='ProviderOrganizers[name]']"))).send_keys('organizers_name_test')
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element( By.CSS_SELECTOR, "[name='ProviderOrganizers[fio]']"))).send_keys('organizers_name_fio_test')
        sleep(1)   
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element( By.CSS_SELECTOR, "[name='ProviderOrganizers[okpo]']"))).send_keys('9899797979')
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element( By.CSS_SELECTOR, "[name='ProviderOrganizers[contract]']"))).send_keys('organizers_contract')  
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element( By.XPATH, "//form[contains(@id,'org-form')]/div[2]/input"  ))).click()
        sleep(1)
        search_organizers_result = self.driver.find_element(
           By.XPATH, "/html/body/div[3]/div/div/table/tbody/tr[1]/td[2]"  
        )
        if search_organizers_result.text == "organizers_name_test":
            test_delete_organizers_result = self.driver.find_element(
               By.XPATH, "/html/body/div[3]/div/div/table/tbody/tr[1]/td[5]/a[2]/i"  
            )
            test_delete_organizers_result.click()
            WebDriverWait(self.driver, 10).until(
              EC.presence_of_element_located((By.ID, "orgPopup")))
            WebDriverWait(self.driver, 10).until(
              EC.element_to_be_clickable(self.driver.find_element( By.XPATH, "//div[contains(@id,'orgPopup')]/form/div[2]/input[2]" ))).click()
            print("search and delete new organizer works")
            sleep(1)
        else:
            raise Exception(
                "search and delete new organizer failed"
            )       
        sleep(1)
        search_organizers_after_delete = self.driver.find_element(
           By.XPATH, "/html/body/div[3]/div/div/table/tbody/tr[1]/td[2]"  
        )
        if search_organizers_after_delete.text != "organizers_name_test":
            print("delete organizer works")
        else:
            raise Exception(
                "delete new organizer not working"
            )
        sleep(1)


    def open_order_page(self):
        WebDriverWait(self.driver, 10).until(
          EC.element_to_be_clickable(self.driver.find_element(  By.CSS_SELECTOR, "[href='/orders/index']" ))).click()
        sleep(1)
        WebDriverWait(self.driver, 10).until(
          EC.element_to_be_clickable(self.driver.find_element( By.ID, "cashierType" ))).click()
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element( By.XPATH, "//select[contains(@id,'cashierType')]/option[1]"  ))).click()
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element( By.XPATH, "//table[contains(@id,'ordersTable')]/tbody/tr[1]/td[1]/a"  ))).click()
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located((By.ID, "modalOrderInfo")))
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element( By.XPATH, "//div[contains(@id,'modalOrderInfo')]/div[3]/button"  ))).click()
        sleep(1)

    def open_customers_page(self):
        WebDriverWait(self.driver, 10).until(
          EC.element_to_be_clickable(self.driver.find_element(  By.CSS_SELECTOR, "[href='/clients/index']" ))).click()
        sleep(1)
        WebDriverWait(self.driver, 10).until(
          EC.element_to_be_clickable(self.driver.find_element( By.ID, "Orders_eventId_chosen" ))).click()
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element( By.XPATH, "//div[contains(@id,'Orders_eventId_chosen')]/div/div/input"))).send_keys('2systemAgent')
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element( By.XPATH, "//div[contains(@id,'Orders_eventId_chosen')]/div/ul/li[1]"))).click()
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element( By.CSS_SELECTOR, "[name='yt0']"))).click()
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element( By.XPATH, "//div[contains(@id,'yw1')]/table/tbody/tr[1]/td[4]/a"))).click()
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located((By.ID, "modalClientInfo")))
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element( By.XPATH, "//div[contains(@id,'clientOrdersTable_filter')]/label/input"))).send_keys('2systemAgent')
        sleep(1)
        search_customers_result_input = self.driver.find_element(
           By.XPATH, "//table[contains(@id,'clientOrdersTable')]/tbody/tr[1]/td[4]"  
        )
        sleep(1)
        if search_customers_result_input.text == "2systemAgent":
            print("all customers filters works correct")
        else:
            raise Exception(
                "customers filters failed"
            )
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.driver.find_element( By.XPATH, "//div[contains(@id,'modalClientInfo')]/div[3]/button"))).click()
        sleep(1)

