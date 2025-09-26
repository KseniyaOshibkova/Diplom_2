import pytest
import allure
from data.login_data import DataForLoginUser


@allure.feature("Логин пользователя")
class TestLoginUser:

    @allure.title("Успешный логин под существующим пользователем")
    @allure.description("Проверяем, что пользователь может залогиниться с корректными email и паролем")
    def test_login_valid_user(self, user_api, created_user):
        user_data = created_user

        with allure.step("Отправляем запрос на логин с валидными данными"):
            response = user_api.login_user({
                "email": user_data["email"],
                "password": user_data["password"]})
            body = response.json()

        with allure.step("Проверяем успешный код и наличие токенов"):
            assert response.status_code == 200
            assert body["success"] is True
            assert "accessToken" in body
            assert "refreshToken" in body
            assert body["user"]["email"] == user_data["email"]


    @pytest.mark.parametrize("invalid_creds", DataForLoginUser.INVALID_LOGINS)
    @allure.title("Логин с неверными данными")
    @allure.description("Проверяем, что сервер возвращает ошибку при неправильном логине или пароле")
    def test_login_invalid_user(self, user_api, invalid_creds):
        with allure.step(f"Отправляем запрос на логин с данными: {invalid_creds}"):
            response = user_api.login_user(invalid_creds)
            body = response.json()

        with allure.step("Проверяем код ошибки и сообщение"):
            assert response.status_code == 401
            assert body["success"] is False
            assert body["message"] == "email or password are incorrect"
