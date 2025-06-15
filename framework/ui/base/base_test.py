import pytest

from framework.ui.pages.search_page import SearchPage
from framework.ui.pages.result_search_page import ResultSearchPage
from framework.ui.pages.film_page import FilmPage


class BaseTest:
    search_page: SearchPage
    result_page: ResultSearchPage
    film_page: FilmPage

    @pytest.fixture(autouse=True)
    def setup(self, request, browser):
        request.cls.browser = browser
        request.cls.search_page = SearchPage(browser)
        request.cls.result_page = ResultSearchPage(browser)
        request.cls.film_page = FilmPage(browser)
