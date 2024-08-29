from WebTest.PageObject.login_page import LoginPage
from playwright.sync_api import sync_playwright
import pytest
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))

# Add the root directory to the Python path
sys.path.append(root_dir)

import GetData
from GetData import VarData
from WebTest.WebInfra.web_driver_factory import WebDriverFactory




class TestLoginWeb():   
    @classmethod
    def setup_driver(cls):
        cls.driver = WebDriverFactory()
    def setup_method(self):
        self.url = GetData.loaded_data[VarData.WebUrl]
        self.web_user_name = GetData.loaded_data[VarData.WebUserName]
        self.web_password = GetData.loaded_data[VarData.WebPassword]

    #@pytest.mark.webtest
    def test_login_web(self):
        login_flow = LoginPage(self.page)
        login_flow.open_page(True, url=self.url)
       # login_flow.enter_email(self.web_user_name)
        login_flow.enter_password(self.web_password)
        login_flow.click_on_submit_button(self)

        # is_home_page_open = login_flow.is_home_page_open()

        # assert is_home_page_open, "Home page was open, Home page failed to open"

    # def teardown_method(self):
    #     self.driver.quit()
@pytest.mark.webtest
def test_login():
    run_test = TestLoginWeb()
    run_test.setup_driver()
    run_test.setup_method()
    run_test.test_login_web()
    pass

