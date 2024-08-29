import os
import subprocess
from playwright.sync_api import sync_playwright, Playwright, Browser

class WebDriverFactory:
    def __init__(self, browser_type='chrome'):
        playwright = sync_playwright().start()
        self.browser = playwright.chromium.launch(headless=False)  # Change to True for headless mode
        self.page = self.browser.new_page()
        self.page.set_viewport_size({"width": 1920, "height": 1080})
        

    def create_webdriver(self, browser_type):
        with sync_playwright() as playwright:
            if browser_type.lower() == 'chrome' or browser_type.lower() == 'chromium':
                return playwright.chromium.launch(headless=False)
            elif browser_type.lower() == 'firefox':
                return playwright.firefox.launch(headless=False)
            elif browser_type.lower() == 'webkit':
                return playwright.webkit.launch(headless=False)
            else:
                return playwright.chromium.launch(headless=False)

    def get_page(self):
        return self.page

    def close_browser(self):
        self.browser.close()

