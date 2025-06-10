import pytest
import allure

from base.base_test import BaseTest
from tests.param.read_param import ReadParam

PARAM = ReadParam.get_param()


@allure.feature('Kinopoisk tests search')
class TestKinopoiskSearchFilm(BaseTest):

    @allure.title('Search film')
    @pytest.mark.parametrize('param', PARAM)
    @pytest.mark.smoke
    def test_kinopoisk_search_film(self, param):
        film_name, country, genre = param
        self.search_page.open()
        self.search_page.make_screenshot('open_search_page')
        self.search_page.set_film_name(film_name)
        self.search_page.make_screenshot('set_film_name')
        self.search_page.set_country(country)
        self.search_page.make_screenshot('set_country')
        self.search_page.set_genre(genre)
        self.search_page.make_screenshot('set_genre')
        self.search_page.search()
        self.result_page.make_screenshot('click_search')
        self.result_page.is_open()
        self.result_page.click_film(film_name)
        self.film_page.make_screenshot('click_film')
        self.film_page.is_open()
        self.film_page.save_info_film(film_name)
