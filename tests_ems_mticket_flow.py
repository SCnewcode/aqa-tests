from time import sleep, time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from pages.login import LoginPage
from pages.main import Main
from pages.mbs_page_test import MBSPage

from tests_ems_mticket_testcase import EmsMticketTestCase


class EmsFlow(EmsMticketTestCase):
    _USER = None

    def ordered_tests_runner(self):
          self.test_update_user_data()
          self.test_events_page()
          self.test_add_event()
          self.test_add_hall()
          self.test_add_date()
          self.test_mbs_check_html()

    def test_update_user_data(self):
       
       def given_url_of_widget_page(ctx):
           ctx.url = self._URL
           self.driver.get(ctx.url)

       def it_should_open_login_form(ctx):
           self.assertTrue(LoginPage(self.driver).login_mbs_form.is_displayed())

       def given_user_mail(ctx):
            ctx.user_name = self.USER_NANE
            ctx.user_pass = self.USER_PASS

       def when_fill_login_form_and_submit_with_otp_code(ctx):
            login_page = LoginPage(self.driver)
            login_page.fill_mbs_login_form_and_submit(ctx.user_name, ctx.user_pass)


    def test_events_page(self):
            def it_should_open_events_page(ctx):
                 Main(self.driver).open_events_page()
                 self.assertTrue(Main(self.driver).present_button.is_displayed())

                 Main(self.driver).open_events_create_page()
                 self.assertTrue(Main(self.driver).present_create_event_page.is_displayed())  
                 
    def test_add_event(self):
           def it_should_add_events(ctx):
               ctx.event_name_new = self.EVENT_NANE

           def when_code(ctx):

               Main(self.driver).events_result(ctx.event_name_new)
               Main(self.driver).click_on_event()

    def test_add_hall(self):
           def it_should_add_hall(ctx):
               ctx.hall_name_new = self.HALL_NANE
               Main(self.driver).events_hall(ctx.hall_name_new)
               Main(self.driver).click_on_hall()


    def test_add_date(self):
           def it_should_add_date(ctx):              
               Main(self.driver).date_events_page()
               Main(self.driver).date_click_self()
               Main(self.driver).no_limit_scan()
               Main(self.driver).update_event_tab()
               Main(self.driver).price_edit_start()
               Main(self.driver).price_container()
               Main(self.driver).apply_template()  
               Main(self.driver).price_container_apply()
               Main(self.driver).apply_template_and_save()
               Main(self.driver).price_edit_update_start()
               Main(self.driver).go_on_sale_click()
               Main(self.driver).confirm_go_to_sale_event()

    def test_mbs_check_html(self):

          def it_should_to_put_event_name(ctx):
            mbs_page = MBSPage(self.driver)
            mbs_page.open_directories_page()
            mbs_page.open_agents_page()
            mbs_page.open_organizers_page()
            mbs_page.open_order_page()
            mbs_page.open_customers_page()
