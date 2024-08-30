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
from WebTest.Flows.login_flow import LoginFlow
from playwright.sync_api import sync_playwright



class TestLoginWeb(WebDriverFactory):
    def __init__(self):
        super().__init__()
        self.url = GetData.loaded_data[VarData.WebUrl]
        self.web_user_name = GetData.loaded_data[VarData.WebUserName]
        self.web_password = GetData.loaded_data[VarData.WebPassword]
    
 
    @pytest.mark.webtest    
    def test_login_web(self):
        login_flow = LoginFlow(self.page)
       
        login_flow.open_page(True, url=self.url)
        login_flow.do_valid_login(self.web_user_name, self.web_password)

        assert login_flow.is_home_page_open()
       

@pytest.mark.webtest
def test_login():
        run_test = TestLoginWeb()
        run_test.test_login_web()
        pass

