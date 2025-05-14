import allure
import requests


class PostOrdersMethods:

    """Метод создания заказа"""

    @allure.step('Запрос на создание заказа')
    def post_orders(self, base_url, api_url, data):
        response = requests.post(f"{base_url}{api_url}", json=data)
        return response.status_code, response.text
