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

    def delete_user(self, access_token):
        headers = {"authorization": f"{access_token}"}
        return self.client.delete(Urls.REFRESH_DATA_USERS, headers=headers)

    def patch_user(self, patch_data, token=None):
        headers = {"authorization": token} if token else {}
        return self.client.patch(Urls.REFRESH_DATA_USERS, headers=headers, json=patch_data)
