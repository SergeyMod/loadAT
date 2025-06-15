import pytest

from framework.api_services.store.api_store import StoreAPI

def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://petstore.swagger.io/v2", help="Base API URL")

@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")