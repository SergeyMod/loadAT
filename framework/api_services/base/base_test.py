import pytest

from framework.api_services.store.api_store import StoreAPI


class BaseTest:
    api_store: StoreAPI

    @pytest.fixture(autouse=True)
    def setup_method(self, base_url):
        self.api_store = StoreAPI(base_url)
