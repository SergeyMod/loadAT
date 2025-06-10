from pages.search_page import SearchPage
from pages.result_search_page import ResultSearchPage
from pages.film_page import FilmPage
from untils.browser import get_browser


class Pages:
    browser = get_browser()

    search_page = SearchPage(browser)
    result_page = ResultSearchPage(browser)
    film_page = FilmPage(browser)