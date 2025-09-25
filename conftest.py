import pytest
from api.api_client import ApiClient
from api.api_user import UserApi
from data.user_data import DataForUser


@pytest.fixture
def client():
    return ApiClient()


@pytest.fixture
def user_api(client):
    return UserApi(client)


@pytest.fixture
def created_user(user_api):
    """Создаёт пользователя и удаляет его после теста"""
    response = user_api.create_user(DataForUser.EXISTING_USER)
    data = response.json()

    yield data

    if "accessToken" in data:
        token = data["accessToken"]
        user_api.delete_user(token)
