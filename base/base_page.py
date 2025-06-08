from itertools import dropwhile

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10, poll_frequency=1)

    def open(self):
        with allure.step(f'Open {self.PAGE_URL} page'):
            self.browser.get(self.PAGE_URL)

    def is_open(self):
        with allure.step(f'Page {self.PAGE_URL} is opened'):
            self.wait.until(EC.url_contains(self.PAGE_URL))

    def find_clickable_element(self, xpath):
        return self.wait.until(EC.element_to_be_clickable(("xpath", xpath)))

    def find_clickable_elements(self, xpath):
        return self.wait.until(
            EC.presence_of_all_elements_located(("xpath", xpath)))

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.browser.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )
