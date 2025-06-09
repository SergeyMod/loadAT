
HOST = 'https://petstore.swagger.io/v2'

class Endpoints:

    get_store_inventory = f'{HOST}/store/inventory'
    create_order = f'{HOST}/store/order'
    dell_order_by_id = get_order_by_id = lambda self, order_id: f'{HOST}/store/order/{order_id}'
