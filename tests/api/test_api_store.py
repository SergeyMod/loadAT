import pytest
import allure

from framework.api_services.base.base_test import BaseTest

@pytest.mark.positive
@pytest.mark.api
@allure.feature('Проверка API swagger')
class TestAPIStore(BaseTest):

    @allure.story('получить инвентарь')
    def test_get_inventory(self):
        self.api_store.get_inventory()

    @allure.story('Создать ордер')
    def test_set_order(self):
        self.api_store.create_order()

    @allure.story('Получить ордер')
    def test_get_order(self):
        self.api_store.create_order()
        self.api_store.get_order(1)

    @allure.story('Удалить ордер')
    def test_dell_order(self):
        self.api_store.create_order()
        self.api_store.dell_order(1)