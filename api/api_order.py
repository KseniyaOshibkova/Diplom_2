


class OrderApi:
    def __init__(self, client):
        self.client = client

    def create_order(self, data):
        """Создать заказ"""
        return self.client.post(Urls.CREATE_ORDER_USER, json=data)

    def get_order_user(self, params=None):
        """Получить список заказов конкретного пользователя"""
        return self.client.get(Urls.GET_ORDER_USER, params=params)
