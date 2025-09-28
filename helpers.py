import random
import string


def random_email(domain="yandex.ru"):
    """Генерация уникального email"""
    return "test_" + "".join(random.choices(string.ascii_lowercase, k=8)) + f"@{domain}"
