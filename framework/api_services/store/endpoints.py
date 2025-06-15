from enum import Enum

# HOST = 'https://petstore.swagger.io/v2'

class Endpoints(str):
    def __init__(self, base_url):
        self.HOST = base_url

    @property
    def get_store_inventory(self):
        return f'{self.HOST}/store/inventory'

    @property
    def create_order(self):
        return f'{self.HOST}/store/order'

    def get_order_by_id(self, order_id: int) -> str:
        return f'{self.HOST}/store/order/{order_id}'

    def dell_order_by_id(self, order_id: int) -> str:
        return f'{self.HOST}/store/order/{order_id}'


