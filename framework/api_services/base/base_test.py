from framework.api_services.store.api_store import StoreAPI


class BaseTest:

    def setup_method(self):
        self.api_store = StoreAPI()
