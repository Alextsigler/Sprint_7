from helpers import generate_random_string

"""Данные для Регистрации/Логина курьера"""

login = generate_random_string(10)
password = generate_random_string(10)
firstname = generate_random_string(10)

login_couriers = {
    "login": login,
    "password": password
}

uncurrent_login = {
    "login": f"{login}1",
    "password": password
}

not_field_login = {
    "password": password
}

create_couriers = {
    "login": login,
    "password": password,
    "firstName": firstname
}

data_create_couriers = {
    "login": login,
    "password": password,
    "firstName": firstname
}

data_create_null_field = [
    {
        "login": "",
        "password": password,
        "firstName": firstname
    },
    {
        "login": login,
        "password": "",
        "firstName": firstname
    }
]

data_create_not_field = [
    {
        "password": password,
        "firstName": firstname
    },
    {
        "login": login,
        "firstName": firstname
    }
]


"""Данные для создания заказа"""

data_orders_black_and_grey = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK", "GREY"
    ]
}

data_orders_not_colors = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha"
}

data_orders = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}
