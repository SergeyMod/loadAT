from framework.api_services.data.order import Order

class Payloads:
    create_order = Order(id=1, petId=0, quantity=0, status="placed", complete=True).__dict__