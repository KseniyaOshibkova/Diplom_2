from api.url import Urls

class OrderApi:
    def __init__(self, client):
        self.client = client

    def create_order(self, data, token=None):
        """Создать заказ. Если token указан, отправляет его в заголовке Authorization"""
        headers = {"Authorization": token} if token else {}
        return self.client.post(Urls.CREATE_ORDER_USER, json=data, headers=headers)

    def get_order_user(self, params=None, token=None):
        """Получить список заказов конкретного пользователя. Можно передать token для авторизации"""
        headers = {"Authorization": token} if token else {}
        return self.client.get(Urls.GET_ORDER_USER, params=params, headers=headers)

