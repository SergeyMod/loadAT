import allure

from base.base_page import BasePage
from pages.enum.links import Links


class ResultSearchPage(BasePage):
    PAGE_URL = str(Links.RESULT)

    LINK_FILM_XPATH = '//a[text()="{}"]'

    def __init__(self, browser):
        super().__init__(browser)

    def click_film(self, film_name):
        with allure.step(f'Click film: {film_name}'):
            self.find_clickable_element(
                self.LINK_FILM_XPATH.format(film_name)).click()
