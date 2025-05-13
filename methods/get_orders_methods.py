import allure
import requests


class GetOrderMethods:
    """Метод получения заказов"""

    @allure.step('Запрос на получение списка заков')
    def get_orders(self, base_url, api_url):
        response = requests.get(f"{base_url}{api_url}")
        return response.status_code, response.text
