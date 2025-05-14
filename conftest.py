import pytest
import urls
from helpers import generate_random_string
from methods.courier_methods import CourierMethods


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

"""Фикстура копирует тело из фиксуты регистрации и удаляет поле firstName"""
@pytest.fixture
def generate_data_login_couriers(generate_data_create_couriers):
    data = generate_data_create_couriers.copy()
    data.pop('firstName', None)
    return data


"""Фикстура создания объекта курьера и удаления после его создания"""
@pytest.fixture
def couriers(generate_data_create_couriers, generate_data_login_couriers):
    couriers = CourierMethods()
    yield couriers
    response = couriers.login_couriers(urls.BASE_URL, urls.LOGIN_COURIERS_URL, generate_data_login_couriers)
    id_couriers = response.json()['id']
    couriers.delete_couriers(urls.BASE_URL, urls.DELETE_COURIERS_URL, id_couriers)
