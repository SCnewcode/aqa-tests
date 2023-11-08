import random
from time import sleep
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Main(object):

    def __init__(self, driver):
        self.driver = driver

    @property
    def main(self):
        return self.driver.find_element(By.TAG_NAME, 'body')
    
    @property
    def header_bar(self):
        return self.main.find_element(By.ID, 'yw0')
    
    @property
    def evants_bar(self):
        return self.main.find_element(By.CLASS_NAME, 'btn-group.pull-left')
    
    @property
    def present_button(self):
        return self.main.find_element(By.ID, "massAddEvents")
    
    @property
    def present_create_event_page(self):
        return self.main.find_element(By.ID, "eventTabs")

    @property
    def events_page(self):
      return  self.header_bar.find_element(By.CSS_SELECTOR, "[href='/provider/events']") 
  

    def open_events_page(self):
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.events_page)).click()
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located((By.ID, "massAddEvents")))
        sleep(2)

    @property
    def events_create_page(self):
      return  self.main.find_element(By.CSS_SELECTOR, "[href='/provider/eventCreate']") 
    
    def open_events_create_page(self):
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.events_create_page)).click()
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located((By.ID, "eventTabs")))
        sleep(2)


    @property
    def add_event(self):
       return {"parent_element": self.main.find_element(By.ID, "ProviderEvents_showId_chosen") ,
                "type_name_event": self.main.find_element(By.CSS_SELECTOR, "input[class='chosen-search-input']"),

              }
            

    
    def events_result(self, event_name):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.add_event["parent_element"])).click()
        sleep(1)
        self.add_event['type_name_event'].send_keys(event_name)
        sleep(1)

    @property
    def click_on_new_event(self):
       dropdown_event_element = self.main.find_element(By.XPATH, "//div[contains(@class,'chosen-drop')]")
       return {
                 "find_element_new": dropdown_event_element,
                 "find_element_in_list": dropdown_event_element.find_element(By.TAG_NAME, 'ul'),
                 "click_on_list_elements": dropdown_event_element.find_element(By.TAG_NAME, 'li')


              }
    
    def click_on_event(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.click_on_new_event.get("find_element_new")))
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.click_on_new_event.get("find_element_in_list")))
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.click_on_new_event.get("click_on_list_elements"))).click()
        sleep(2)
    
    @property
    def add_hall_on_input(self):
       return {"parent_element_hall": self.main.find_element(By.ID, "hallId_chosen") ,
                "type_name_hall": self.main.find_element(By.XPATH, "//div[contains(@id,'hallId_chosen')]/div/div/input"),
              }
            

    
    def events_hall(self, hall_name):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.add_hall_on_input["parent_element_hall"])).click()
        sleep(1)
        self.add_hall_on_input['type_name_hall'].send_keys(hall_name)
        sleep(1)


    @property
    def click_on_new_hall(self):
       dropdown_hall_element = self.main.find_element(By.XPATH, "//div[contains(@id,'hallId_chosen')]/div")
       return {
                 "find_element_hall": dropdown_hall_element,
                 "find_element_in_hall": dropdown_hall_element.find_element(By.TAG_NAME, 'ul'),
                 "click_on_list_hall": dropdown_hall_element.find_element(By.TAG_NAME, 'li')
              }
       
    def click_on_hall(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.click_on_new_hall.get("find_element_hall")))
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.click_on_new_hall.get("find_element_in_hall")))
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.click_on_new_hall.get("click_on_list_hall"))).click()
        sleep(1)


    @property
    def date_event_page(self):
        return self.main.find_element(By.ID, "eventDate")

    def date_events_page(self):
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.date_event_page)).click()
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located((By.ID, "ui-datepicker-div")))
        sleep(1)

    @property
    def date_click(self):
        return self.main.find_element(By.CLASS_NAME, "ui-datepicker-today")

    def date_click_self(self):
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.date_click)).click()
        sleep(1)


    def no_limit_scan(self):
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.main.find_element(By.ID, "ProviderEvents_isUnlimitedScan"))).click()
        sleep(1)


    @property
    def update_form_id(self):
        return self.main.find_element(By.ID, "eventForm")

    def update_event_tab(self):
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.main.find_element(By.CSS_SELECTOR, "input[type='submit']"))).click()
        WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located((By.ID, "tabs-prices")))
        sleep(2)


        
    @property
    def price_add_edit_start(self):
        return self.main.find_element(By.ID, "tabs-prices")

    def price_edit_start(self):
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.main.find_element(By.XPATH, "//div[contains(@id,'tabs-prices')]/a[1]"))).click()
        sleep(1)


    @property
    def new_page_test(self):
        return self.driver.find_element(By.ID, 'eventPricesSidebar')

    def price_container(self):
        windows = self.driver.window_handles
        print("opened windows length: ", len(windows))
        self.driver.switch_to.window(windows[1])
        sleep(1)
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.new_page_test.find_element(By.XPATH, "//div[contains(@id,'eventPricesSidebar')]/div/ul/li[2]/a"))).click()
        sleep(1)


    def apply_template(self):
         WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.new_page_test.find_element(By.ID, 'applyTemplate'))).click()
         sleep(1)

        
    def price_container_apply(self):

        obj = self.driver.switch_to.alert
        message=obj.text
        print ("Alert shows following message: "+ message )
        obj.accept()
        sleep(1)
        obj.accept()
        sleep(1)

    @property
    def save_and_apply(self):
        return self.driver.find_element(By.ID, 'placesSidebar')
    
    def apply_template_and_save(self):
         WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.save_and_apply.find_element(By.XPATH, "//div[contains(@id,'placesSidebar')]/div[1]/button[2]"))).click()
         sleep(2)

    @property
    def price_update_in_tab(self):
         return self.main.find_element(By.ID, "tabs-prices")
    
    def price_edit_update_start(self):

        windows = self.driver.window_handles
        print("opened windows length: ", len(windows))
        self.driver.switch_to.window(windows[0])

        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.main.find_element(By.XPATH, "//div[contains(@id,'tabs-prices')]/a[2]"))).click()
        sleep(1)  


    def go_on_sale_click(self):
        WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable(self.main.find_element(By.ID, 'statusPublish'))).click()
        sleep(2)  

    def confirm_go_to_sale_event(self):
        obj = self.driver.switch_to.alert
        message=obj.text
        print ("Alert shows following message: "+ message )
        obj.accept()
        sleep(2)


