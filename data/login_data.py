


class DataForLoginUser:
    VALID_LOGIN = {
        "email": "test_user@yandex.ru",
        "password": "password123"
    }

    INVALID_LOGINS = [
        {
            "email": "wrong_user@yandex.ru",
            "password": "password123"
        },
        {
            "email": "test_user@yandex.ru",
            "password": "wrongpassword"
        }
    ]