from behave import when, then, given

from framework.api_services.store.api_store import StoreAPI

store_api = StoreAPI()

@then('Получить на запрос инвентарья статус код 200')
def get_inventory(context):
    store_api.get_inventory()

@then('Получить на запрос создания ордера код 200')
def test_set_order(context):
    store_api.create_order()

@then('Получить на запрос получения ордера код 200')
def test_get_order(context):
    store_api.create_order()
    store_api.get_order(1)

@then('Получить на запрос удаления ордера код 200')
def test_dell_order(context):
    store_api.create_order()
    store_api.dell_order(1)