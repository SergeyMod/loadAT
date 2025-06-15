import allure

from selenium.webdriver.common.by import By

from framework.ui.base.base_page import BasePage
from framework.ui.pages.enum.links import Links


class FilmPage(BasePage):
    PAGE_URL = str(Links.FILM)

    ELEMENT_INFO_XPATH = '//div[@data-tid="7cda04a5"]'
    TITLE_CSS_SELECTOR = '.styles_title__b1HVo'
    VALUE_CSS_SELECTOR = '.styles_value__g6yP4'

    def __init__(self, browser):
        super().__init__(browser)

    def save_info_film(self, film_name: str):
        with allure.step(f'Parse param film: {film_name}'):
            elements = self.find_clickable_elements(
                self.ELEMENT_INFO_XPATH)
            film_info = {}
            for element in elements:
                title = element.find_element(
                    By.CSS_SELECTOR,
                    self.TITLE_CSS_SELECTOR).text.strip()
                value = element.find_element(
                    By.CSS_SELECTOR,
                    self.VALUE_CSS_SELECTOR).text.strip()
                film_info[title] = value
            allure.attach(
                '\n'.join(
                    f'{key}: {value}' for key, value in film_info.items()),
                name='Основная информация о фильме',
                attachment_type=allure.attachment_type.TEXT
            )
