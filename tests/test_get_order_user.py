import allure


@allure.feature("Получение заказов пользователя")
class TestGetUserOrders:
    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_user_orders_authorized(self, order_api, auth_user_token):
        token = auth_user_token

        with allure.step("Отправляем запрос на получение заказов авторизованного пользователя"):
            response = order_api.get_order_user(token=token)
            body = response.json()

        with allure.step("Проверяем, что статус ответа 200"):
            assert response.status_code == 200

        with allure.step("Проверяем, что в теле ответа есть ключ 'orders'"):
            assert "orders" in body
            assert isinstance(body["orders"], list)

        with allure.step("Проверяем, что ключ 'success' равен True"):
            assert body["success"] is True


    @allure.title("Получение заказов неавторизованного пользователя")
    def test_get_user_orders_unauthorized(self, order_api):
        with allure.step("Отправляем запрос на получение заказов без токена"):
            response = order_api.get_order_user(token=None)
            body = response.json()

        with allure.step("Проверяем, что статус ответа 401"):
            assert response.status_code == 401

        with allure.step("Проверяем, что success=False и вернулось сообщение об ошибке"):
            assert body["success"] is False
            assert body["message"] == "You should be authorised"
