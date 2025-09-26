import pytest
from api.api_client import ApiClient
from api.api_user import UserApi
from data.change_data_user import DataForUserChange
from data.user_data import DataForUser


@pytest.fixture
def client():
    return ApiClient()


@pytest.fixture
def user_api(client):
    return UserApi(client)


@pytest.fixture
def created_user(user_api):
    """Создаёт пользователя EXISTING_USER и удаляет его после теста"""
    response = user_api.create_user(DataForUser.EXISTING_USER)
    data = response.json()  # <-- здесь есть 'accessToken'

    yield data  # возвращаем данные сервера

    # удаляем пользователя
    if "accessToken" in data:
        user_api.delete_user(data["accessToken"])


@pytest.fixture
def auth_user_token(user_api: UserApi):
    """Создаёт пользователя для авторизации, возвращает токен и удаляет после теста"""
    response = user_api.create_user(DataForUserChange.AUTH_USER)
    body = response.json()

    # достаёт токен без префикса 'Bearer '
    token = body.get("accessToken")
    if token and token.startswith("Bearer "):
        token = token.split(" ", 1)[1]

    yield token

    # удаляет пользователя после теста
    if token:
        user_api.delete_user(f"Bearer {token}")
