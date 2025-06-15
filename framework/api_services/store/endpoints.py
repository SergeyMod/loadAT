from enum import Enum

HOST = 'https://petstore.swagger.io/v2'

class Endpoints(str, Enum):
    GET_STORE_INVENTORY = f'{HOST}/store/inventory'
    CREATE_ORDER = f'{HOST}/store/order'

    @staticmethod
    def GET_ORDER_BY_ID(order_id: int) -> str:
        return f'{HOST}/store/order/{order_id}'

    @staticmethod
    def DELL_ORDER_BY_ID(order_id: int) -> str:
        return f'{HOST}/store/order/{order_id}'

    def __str__(self):
        return self.value

