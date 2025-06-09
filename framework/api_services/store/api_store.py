import requests
import jsonschema
import allure

from framework.api_services.store.payloads import Payloads
from framework.api_services.store.endpoints import Endpoints


class StoreAPI:
    def __init__(self):
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.\
            json_schema = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "petId": {"type": "integer"},
                "quantity": {"type": "integer"},
                "shipDate": {"type": "string", "format": "date-time"},
                "status": {"type": "string"},
                "complete": {"type": "boolean"}
            },
            "required": ["id", "petId", "quantity", "shipDate", "status",
                         "complete"]
        }

    @allure.step('create order')
    def create_order(self):
        response = requests.post(
            url=self.endpoints.create_order,
            json=self.payloads.create_order
        )
        assert response.status_code == 200, response.json()

    @allure.step('get order')
    def get_order(self, order_id):
        response = requests.get(self.endpoints.get_order_by_id(order_id))
        assert response.status_code == 200, response.json()
        jsonschema.validate(response.json(), self.json_schema)

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
