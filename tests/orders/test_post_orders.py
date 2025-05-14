import allure
import pytest
import data
import urls
from methods.post_orders_methods import PostOrdersMethods


@allure.feature('Проверки ручки создания заказа')
class TestOrders:

    # Можно указать один из цветов - BLACK или GREY
    @allure.title('Проверка, что можно указать один из цветов - BLACK или GREY')
    @allure.description('Создаем заказ с указанием одного из цветов')
    @pytest.mark.parametrize('colors', ["BLACK", "GREY"])
    def test_create_orders_with_one_colors(self, colors):
        data1 = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                colors
            ]
        }
        orders = PostOrdersMethods()
        status_code, response_text = orders.post_orders(
            urls.BASE_URL, urls.CREATE_ORDERS_URL, data1
        )
        assert status_code == 201 and response_text, (
            f"status_code = {status_code}, response_text = {response_text}"
        )

    # Можно указать оба цвета
    @allure.title('Проверка, что можно указать оба цвета')
    @allure.description('Создаем заказ с указаним двух цветов')
    def test_create_orders_with_two_colors(self):
        orders = PostOrdersMethods()
        status_code, response_text = orders.post_orders(
            urls.BASE_URL, urls.CREATE_ORDERS_URL, data.data_orders_black_and_grey
        )
        assert status_code == 201 and response_text, (
            f"status_code = {status_code}, response_text = {response_text}"
        )


    # Можно совсем не указывать значения
    @allure.title('Проверка, что можно совсем не указывать значения')
    @allure.description('Создаем заказ без указания цвета')
    def test_create_orders_not_colors(self):
        orders = PostOrdersMethods()
        status_code, response_text = orders.post_orders(
            urls.BASE_URL, urls.CREATE_ORDERS_URL, data.data_orders_not_colors
        )
        assert status_code == 201 and response_text, (
            f"status_code = {status_code}, response_text = {response_text}"
        )


    # Тело ответа содержит track
    @allure.title('Проверка, что тело ответа содержит track')
    @allure.description('Создаем заказ')
    def test_create_orders_with_two_colors(self):
        orders = PostOrdersMethods()
        status_code, response_text = orders.post_orders(
            urls.BASE_URL, urls.CREATE_ORDERS_URL, data.data_orders
        )
        assert "track" in response_text, (
            f"status_code = {status_code}, response_text = {response_text}"
        )