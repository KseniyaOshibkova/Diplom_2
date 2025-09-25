from api.url import Urls


class UserApi:
    def __init__(self, client):
        self.client = client

    def create_user(self, user_data):    #добавить данные для создания пользователя
        """Создание пользователя"""
        return self.client.post(Urls.CREATE_USER, json=user_data)

    def login_user(self, creds):   #данные для логина
        """Логин пользователя в системе"""
        return self.client.post(Urls.LOGIN_USER, json=creds)

    def delete_user(self, user_id):
        """Удаление пользователя из системы"""
        return self.client.delete(f"{Urls.DELETE_USER}/{user_id}")
