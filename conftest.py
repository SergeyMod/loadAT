import pytest

from untils.browser import get_browser


@pytest.fixture(autouse=True)
def browser(request):
    browser = get_browser()
    request.cls.browser = browser
    yield browser
    browser.quit()


