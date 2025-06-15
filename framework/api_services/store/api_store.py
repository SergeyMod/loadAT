import requests
import allure

from framework.api_services.store.payloads import Payloads
from framework.api_services.store.endpoints import Endpoints
from framework.api_services.data.order import Order


class StoreAPI:
    def __init__(self, base_url):
        self.endpoints = Endpoints(base_url)

    @allure.step('create order')
    def create_order(self):
        response = requests.post(
            url=self.endpoints.create_order,
            json=Payloads().create_order
        )
        assert response.status_code == 200, response.json()

    @allure.step('get order')
    def get_order(self, order_id):
        response = requests.get(self.endpoints.get_order_by_id(order_id))
        assert response.status_code == 200, response.json()
        Order(**response.json())

    @allure.step('get inventory')
    def get_inventory(self):
        response = requests.get(
            url=self.endpoints.get_store_inventory
        )
        assert response.status_code == 200, response.json()

    @allure.step('delete order')
    def dell_order(self, order_id):
        response = requests.delete(self.endpoints.dell_order_by_id(order_id))
        assert response.status_code == 200, response.json()
