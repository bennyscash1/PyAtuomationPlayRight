from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
import unittest

class WeblocatoreFunction():
    DEFAULT_TIMEOUT_IN_SECONDS = 20.0
    def __init__(self, page: Page):
        self.page = page

    def is_element_found(self, selector: str) -> bool:
        try:
            if self.page.is_visible(selector, timeout=self.DEFAULT_TIMEOUT_IN_SECONDS):
                return True
            else:
                print(f"Element '{selector}' found in the DOM but not visible.")
                return False
        except TimeoutError:
            print(f"Element '{selector}' not found within {self.DEFAULT_TIMEOUT_IN_SECONDS } seconds")
            return False


    def wait_for_element_visibility(self, selector):
        element_visible = self.is_element_found(selector)
        element_details = f"Element {selector} search failed within {self.DEFAULT_TIMEOUT_IN_SECONDS } seconds"
        self.assertTrue(element_visible, element_details)

    def click(self, selector: str):
        element_visible = self.is_element_found(selector)
        if element_visible:
            self.page.click(selector)
        else:
            element_details = f"Element {selector} click failed within {self.DEFAULT_TIMEOUT_IN_SECONDS } seconds"
            self.assertTrue(element_visible, element_details)

    def fill_text(self, selector: str, text):
      #  self.page.fill(selector, text)
        element_visible = self.is_element_found(selector)
        if element_visible:
            self.page.fill(selector, text)
        else:
            element_details = f"Element {selector} click failed within {self.DEFAULT_TIMEOUT_IN_SECONDS} seconds"
            self.assertTrue(element_visible, element_details)

    def switch_to_frame(self, frame_selector):
        self.page.frame(frame_selector)

    def is_displayed(self, selector):
        try:
            self.wait_for_element_visibility(selector)
            return self.page.is_visible(selector)
        except PlaywrightTimeoutError:
            return False

    def alert_ok(self):
        alert = self.page.on("dialog", lambda dialog: dialog.accept())

    def get_text_from_at(self, selector, attribute):
        self.wait_for_element_visibility(selector)
        return self.page.get_attribute(selector, attribute)

    # def mark_element(self, selector):
    #     color = "#0000FF"
    #     element_handle = self.page.query_selector(selector)
    #     if element_handle:
    #         self.page.evaluate("element => element.style.border = '3px solid ' + arguments[1]", element_handle, color)

# Example of usage
# driver = webdriver.Chrome()  # Or any other browser you're using
# base_functions = BaseFunctions(driver)
# Remember to replace 'webdriver.Chrome()' with your actual WebDriver initialization.
