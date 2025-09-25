

class DataForUser:
    """Данные для тестов создания пользователя"""
    UNIQUE_USER_TEMPLATE = {
        "password": "password123",
        "name": "TestUser"
    }

    EXISTING_USER = {
        "email": "exist_user@yandex.ru",
        "password": "password123",
        "name": "ExistUser"
    }

    # Набор невалидных данных (без одного из обязательных полей)
    INVALID_USERS = [
        {"password": "password123", "name": "NoEmail"},  # без email
        {"email": "no_pass@yandex.ru", "name": "NoPassword"},  # без password
        {"email": "no_name@yandex.ru", "password": "password"}  # без name
    ]