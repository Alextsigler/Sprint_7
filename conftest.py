import pytest
from helpers import generate_random_string


"""Фикстура для создания уникальных данных регистрации курьера"""


@pytest.fixture
def generate_data_create_couriers():
    login = generate_random_string(10)
    password = generate_random_string(10)
    firstname = generate_random_string(10)

    data = {
        "login": login,
        "password": password,
        "firstName": firstname
    }

    return data


"""Фикстура для создания уникальных данных логина курьера"""


@pytest.fixture
def generate_data_login_couriers():
    login = generate_random_string(10)
    password = generate_random_string(10)

    data = {
        "login": login,
        "password": password,
    }

    return data

