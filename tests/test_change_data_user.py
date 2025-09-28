import pytest
import allure
from data.change_data_user import DataForUserChange

@allure.feature("Изменение данных пользователя")
class TestChangeDataUser:

    @allure.title("Изменение имени и email авторизованным пользователем")
    @allure.description("Проверяем, что авторизованный пользователь может изменить имя и email")
    @pytest.mark.parametrize("update_data, expected_field", [
        (DataForUserChange.UPDATE_NAME, "name"),
        (DataForUserChange.UPDATE_EMAIL, "email")
    ])
    def test_change_user_name_or_email(self, user_api, auth_user_token, update_data, expected_field):
        token = auth_user_token

        with allure.step(f"Отправляем PATCH запрос с данными: {update_data}"):
            response = user_api.patch_user(update_data, token=token)
            body = response.json()

        with allure.step("Проверяем успешный ответ и обновлённое поле"):
            assert response.status_code == 200
            assert body["success"] is True
            assert body["user"][expected_field] == update_data[expected_field]



    @allure.title("Изменение пароля авторизованным пользователем")
    @allure.description("Проверяем, что авторизованный пользователь может изменить пароль (только статус код)")
    def test_change_user_password(self, user_api, auth_user_token):
        token = auth_user_token
        update_data = DataForUserChange.UPDATE_PASSWORD

        with allure.step(f"Отправляем PATCH запрос с новым паролем"):
            response = user_api.patch_user(update_data, token=token)

        with allure.step("Проверяем успешный ответ"):
            assert response.status_code == 200



    @allure.title("Попытка изменить данные без авторизации")
    @allure.description("Проверяем, что неавторизованный пользователь не может изменить данные")
    @pytest.mark.parametrize("update_data", [
        DataForUserChange.UPDATE_NAME,
        DataForUserChange.UPDATE_EMAIL,
        DataForUserChange.UPDATE_PASSWORD
    ])
    def test_change_user_unauthorized(self, user_api, update_data):
        with allure.step(f"Отправляем PATCH запрос без токена с данными: {update_data}"):
            response = user_api.patch_user(update_data)
            body = response.json()

        with allure.step("Проверяем код ошибки и сообщение"):
            assert response.status_code == 401
            assert body["success"] is False
            assert body["message"] == "You should be authorised"
