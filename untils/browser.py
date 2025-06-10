from selenium import webdriver
from selenium.webdriver.edge.options import Options as OE
from selenium.webdriver.chrome.options import Options as OCH
from selenium.webdriver.firefox.options import Options as OFF

from conf.read_settings import ReadSettings

def get_browser():
    settings = ReadSettings.get_settings()
    match settings['browser'].lower():
        case 'edge':
            options = OE()
            _set_options(options, settings['options'])
            browser = webdriver.Edge(options=options)
        case 'chrome':
            options = OCH()
            _set_options(options, settings['options'])
            browser = webdriver.Chrome(options=options)
        case 'firefox':
            options = OFF()
            _set_options(options, settings['options'])
            browser = webdriver.Firefox(options=options)
        case _:
            raise ValueError(
                f'Браузер {settings['browser']} не распознан, проверте значение')
    browser.set_window_size(*settings['window_size'].split(','))
    return browser


def _set_options(options, dict_options):
    for option, is_on in dict_options.items():
        if is_on.lower() == 'true':
            options.add_argument(option)