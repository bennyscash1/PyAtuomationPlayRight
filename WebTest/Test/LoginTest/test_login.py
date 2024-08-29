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
from playwright.sync_api import Page
from WebTest.WebInfra.web_driver_factory import WebDriverFactory
from WebTest.PageObject.login_page import LoginPage

from playwright.sync_api import sync_playwright



class TestLoginWeb:

    def fatch_data(self):
        self.url = GetData.loaded_data[VarData.WebUrl]
        self.web_user_name = GetData.loaded_data[VarData.WebUserName]
        self.web_password = GetData.loaded_data[VarData.WebPassword]
    
    #@classmethod
    def setup_driver(cls):
        cls.driver = WebDriverFactory()
        
    def test_login_web(self):
        self.login_page = LoginPage(self)
       
        self.login_page.enter_email(self.web_user_name)  # Uncomment if defined in LoginPage
        self.login_page.enter_password(self.web_password)
        self.login_page.click_on_submit_button()

        # Add assertions here to validate login success

@pytest.mark.webtest
def test_login():
        run_test = TestLoginWeb(Page)
        run_test.setup_driver()
        run_test.test_login_web()
        pass

