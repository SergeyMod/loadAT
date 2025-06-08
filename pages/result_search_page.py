import allure

from base.base_page import BasePage
from pages.links import Links


class ResultSearchPage(BasePage):
    PAGE_URL = Links.RESULT

    LINK_FILM = '//a[text()="{}"]'

    def __init__(self, browser):
        super().__init__(browser)

    def click_film(self, film_name):
        with allure.step(f'Click film: {film_name}'):
            self.find_clickable_element(
                self.LINK_FILM.format(film_name)).click()
