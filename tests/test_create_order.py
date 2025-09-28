import pytest
import allure
from api.api_order import OrderApi
from data.order_data import DataForOrder

@allure.feature("Создание заказа")
class TestCreateOrder:
    @pytest.mark.parametrize(
        "order_data, token_key, expected_status, expected_message",
        DataForOrder.AUTH_VARIANTS + DataForOrder.INGREDIENT_VARIANTS)
    @allure.title("Создание заказа с разными сценариями")
    @allure.description("Каждый сценарий описан в параметрах: авторизация и ингредиенты")
    def test_create_order(
            self, order_api: OrderApi, auth_user_token, order_data, token_key, expected_status, expected_message):
        # Подставляем токен из параметров
        token = auth_user_token if token_key == "auth_user_token" else None

        with allure.step("Отправляем запрос на создание заказа с парамерами"):
            response = order_api.create_order(order_data, token=token)
            body = response.json()

        with allure.step("Проверяем статус-код и ответ сервера"):
            assert response.status_code == expected_status
            if expected_message:
                assert body["message"] == expected_message
