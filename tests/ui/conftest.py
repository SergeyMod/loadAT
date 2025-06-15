from selenium import webdriver
from selenium.webdriver.edge.options import Options as OE
from selenium.webdriver.chrome.options import Options as OCH
from selenium.webdriver.firefox.options import Options as OFF
import pytest

from framework.ui.conf.read_settings import ReadSettings


@pytest.fixture(autouse=True)
def browser(request):
    settings = ReadSettings.get_settings()
    match settings['browser'].lower():
        case 'edge':
            options = OE()
            set_options(options, settings['options'])
            browser = webdriver.Edge(options=options)
        case 'chrome':
            options = OCH()
            set_options(options, settings['options'])
            browser = webdriver.Chrome(options=options)
        case 'firefox':
            options = OFF()
            set_options(options, settings['options'])
            browser = webdriver.Firefox(options=options)
        case _:
            raise ValueError(
                f'Браузер {settings["browser"]} не распознан, проверте значение')
    browser.set_window_size(*settings['window_size'].split(','))
    request.cls.browser = browser
    yield browser
    browser.quit()


def set_options(options, dict_options):
    for option, is_on in dict_options.items():
        if is_on.lower() == 'true':
            options.add_argument(option)