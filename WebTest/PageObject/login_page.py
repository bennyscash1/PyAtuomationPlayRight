from playwright.sync_api import Page

from WebTest.PageObject.base_pages import BasePages


class LoginPage(BasePages):

    def __init__(self, page: Page):
        super().__init__(page)
        self.m_user_name_input_field = "//input[@id='username']"
        self.m_password_input_field = "//input[@id='password']"
        self.m_submit_button = "//button[@id='submit']"
        self.m_home_page_logo_by = "//h1[normalize-space()='Logged In Successfully']"

    def open_page(self, navigate_to_logon_screen=True, url=None):
        if navigate_to_logon_screen and url is not None:
            self.page.goto(url)
        return self

    def enter_email(self, email):
        self.fill_text(self.m_user_name_input_field, email)
        return self

    def enter_password(self, password):
        self.fill_text(self.m_password_input_field, password)
        return self

    def click_on_submit_button(self):
        self.click(self.m_submit_button)
        return self

    def is_home_page_displayed(self):
        self.wait_for_element_visibility(self.m_home_page_logo_by)
        return True
