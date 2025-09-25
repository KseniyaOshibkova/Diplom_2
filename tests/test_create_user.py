import pytest
import allure
from data.user_data import DataForUser
from helpers import random_email


@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    @allure.description("Проверяем, что пользователь с уникальным email успешно создаётся")
    def test_create_unique_user(self, user_api):
        # Генерация уникального email + подставляем статичные поля
        unique_user = DataForUser.UNIQUE_USER_TEMPLATE.copy()
        unique_user["email"] = random_email()

        with allure.step("Отправляем запрос на создание пользователя"):
            response = user_api.create_user(unique_user)

        with allure.step("Проверяем успешный ответ и данные пользователя"):
            body = response.json()
            assert response.status_code == 200
            assert body["success"] is True
            assert body["user"]["email"] == unique_user["email"]

        with allure.step("Удаляем созданного пользователя"):
            if "accessToken" in body:
                user_api.delete_user(body["accessToken"])

    @allure.title("Создание пользователя с уже зарегистрированным email")
    @allure.description("Проверяем, что сервер возвращает ошибку при попытке создать дубликат")
    def test_create_existing_user(self, user_api, created_user):
        # Пользователь уже создан фикстурой
        with allure.step("Создаем пользователя с уже зарегистрированным email"):
            response = user_api.create_user(DataForUser.EXISTING_USER)
            body = response.json()
        with allure.step("Проверяем код ошибки и сообщение"):
            assert response.status_code == 403
            assert body["success"] is False
            assert body["message"] == "User already exists"


    @pytest.mark.parametrize("user_data", DataForUser.INVALID_USERS)
    @allure.title("Создание пользователя без обязательного поля")
    @allure.description("Проверяем, что сервер возвращает ошибку, если отсутствует email, password или name")
    def test_create_user_missing_field(self, user_api, user_data):
        with allure.step(f"Создаем пользователя с данными: {user_data}"):
            response = user_api.create_user(user_data)

        with allure.step("Проверяем код ошибки и сообщение"):
            body = response.json()
            assert response.status_code == 403
            assert body["success"] is False
            assert body["message"] == "Email, password and name are required fields"
