import allure
from selenium.webdriver.support.ui import Select

from base.base_page import BasePage
from pages.enum.links import Links


class SearchPage(BasePage):
    PAGE_URL = str(Links.SEARCH)

    FILM_NAME_FIELD_XPATH = '//input[@id="find_film"]'
    COUNTRY_FIELD_XPATH = '//select[@id="country"]'
    GENRE_FIELD_XPATH = '//select[@id="m_act[genre]"]'
    GENRE_CHECKBOX_XPATH = '//input[@id="m_act[genre_and]"]'
    BUTTON_SEARCH_XPATH = '//input[@value="поиск"]'

    def __init__(self, browser):
        super().__init__(browser)

    def set_film_name(self, film_name: str):
        with allure.step(f'Set film name: {film_name}'):
            element = self.find_clickable_element(self.FILM_NAME_FIELD_XPATH)
            element.send_keys(film_name)

    def select_element_select(self, id_: str, value: str):
        element = self.find_clickable_element(id_)
        Select(element).select_by_visible_text(value)

    def set_country(self, country: str):
        with allure.step(f'Set country: {country}'):
            self.select_element_select(self.COUNTRY_FIELD_XPATH, country)

    def set_genre(self, genre: str):
        with allure.step(f'Set genre: {genre} and checkbox click'):
            self.select_element_select(self.GENRE_FIELD_XPATH, genre)
            self.find_clickable_element(self.GENRE_CHECKBOX_XPATH).click()

    @allure.step('Click button search')
    def search(self):
        self.find_clickable_element(self.BUTTON_SEARCH_XPATH).click()
