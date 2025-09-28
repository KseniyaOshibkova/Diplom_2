


class DataForOrder:
    # Валидный заказ
    VALID_ORDER = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa6d",
            "61c0c5a71d1f82001bdaaa6f"
        ]
    }

    # Варианты авторизации
    AUTH_VARIANTS = [
        (VALID_ORDER, None, 401, "Authorization required"),
        (VALID_ORDER, "auth_user_token", 200, None)
    ]

    # Варианты ингредиентов
    INGREDIENT_VARIANTS = [
        ({"ingredients": VALID_ORDER["ingredients"]}, "auth_user_token", 200, None),
        ({"ingredients": []}, "auth_user_token", 400, "Ingredient ids must be provided"),
        ({"ingredients": ["invalid_id_1", "invalid_id_2"]}, "auth_user_token", 400, "One or more ids provided are "
                                                                                    "incorrect")
    ]
