import pytest
from api.api_client import ApiClient
from api.api_order import OrderApi
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
def order_api():
    client = ApiClient()
    return OrderApi(client)

@pytest.fixture
def created_existing_user(user_api):
    """Создаёт пользователя EXISTING_USER и удаляет его после теста"""
    user_data = DataForUser.EXISTING_USER
    response = user_api.create_user(user_data)
    body = response.json()

    # Возвращает данные пользователя
    yield user_data

    # Удаляет пользователя
    if "accessToken" in body:
        user_api.delete_user(body["accessToken"])

@pytest.fixture
def auth_user_token(user_api: UserApi):
    """Создаёт пользователя AUTH_USER для авторизации, возвращает токен и удаляет после теста"""
    response = user_api.create_user(DataForUserChange.AUTH_USER)
    body = response.json()

    # достаёт токен
    token = body.get("accessToken")

    yield token

    # удаляет пользователя после теста
    if token:
        user_api.delete_user(token)
