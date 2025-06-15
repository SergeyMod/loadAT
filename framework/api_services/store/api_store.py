import requests
import allure

from framework.api_services.store.payloads import Payloads
from framework.api_services.store.endpoints import Endpoints
from framework.api_services.data.order import Order


class StoreAPI:
    @allure.step('create order')
    def create_order(self):
        response = requests.post(
            url=Endpoints.CREATE_ORDER,
            json=Payloads().create_order
        )
        assert response.status_code == 200, response.json()

    @allure.step('get order')
    def get_order(self, order_id):
        response = requests.get(Endpoints.GET_ORDER_BY_ID(order_id))
        assert response.status_code == 200, response.json()
        Order(**response.json())

    @allure.step('get inventory')
    def get_inventory(self):
        response = requests.get(
            url=Endpoints.GET_STORE_INVENTORY
        )
        assert response.status_code == 200, response.json()

    @allure.step('delete order')
    def dell_order(self, order_id):
        response = requests.delete(Endpoints.DELL_ORDER_BY_ID(order_id))
        assert response.status_code == 200, response.json()
