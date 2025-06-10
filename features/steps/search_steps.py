from behave import when, given, then

from features.pages_ import Pages
from tests.param.read_param import ReadParam

@given('Даны название фильма страна и жанир')
def set_param(context):
    param = ReadParam.get_param()[0]
    context.file_name, context.country, context.genre = param

@when('Открывается страница поиска фильма')
def open_(context):
    Pages.search_page.open()

@when('Заполняется поле название фильма')
def set_film_name(context):
    Pages.search_page.set_film_name(context.file_name)

@when('Заполняется поле страна')
def set_country(context):
    Pages.search_page.set_country(context.country)

@when('Заполняется поле жанр и ставится галочка в checkbox')
def set_genre(context):
    Pages.search_page.set_genre(context.genre)

@when('Нажимается кнопка поиска фильма')
def search(context):
    Pages.search_page.search()

@when('Нажимается название фильма')
def click_film(context):
    Pages.result_page.click_film(context.file_name)

@then('URL страницы соответствует странице фильма')
def check_url(context):
    Pages.film_page.is_open()