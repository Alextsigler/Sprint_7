import requests
import allure


class CourierMethods:


    """Метод создания курьера"""
    @allure.step('Отправлили запрос за создание курьера')
    def post_couriers(self, base_url, api_url, data):
        response = requests.post(f"{base_url}{api_url}", data=data)
        return response.status_code, response.text

    """Метод логина курьера"""
    @allure.step('Отправили запрос на логин курьера')
    def login_couriers(self, base_url, api_url, data):
        response = requests.post(f"{base_url}{api_url}", data=data)
        return response


    """Метод удаления курьера"""
    @allure.step('Отправили запрос на удаление курьера')
    def delete_couriers(self, base_url, api_url, id_couriers):
        response = requests.delete(f"{base_url}{api_url}/{id_couriers}")
