import data
import urls
from methods.courier_methods import CourierMethods
import allure


@allure.feature('Проверки авторизации пользователя')
class TestLoginCouriers:


    # Курьер может авторизоваться
    @allure.title('Проверка авторизации курьера')
    @allure.description('Создаем курьера, логини курьера с корректными данными, проверяем, удаляем')
    def test_login_couriers(self):
        couriers = CourierMethods()
        couriers.post_couriers(
            urls.BASE_URL, urls.CREATE_COURIERS_URL, data.create_couriers
        )
        response = couriers.login_couriers(
            urls.BASE_URL, urls.LOGIN_COURIERS_URL, data.login_couriers
        )
        id_couriers = response.json()['id']
        assert response.status_code == 200 and response.text, (
            f"status_code = {response.status_code}, response_text = {response.text}"
        )
        couriers.delete_couriers(urls.BASE_URL, urls.DELETE_COURIERS_URL, id_couriers)


    # Для авторизации нужно передать все обязательные поля
    @allure.title('Проверка. что для авторизации нужно передать все обязательные поля')
    @allure.description('Создаем курьера, логиним курьера с корректными данными, проверям, удаляем')
    def test_login_with_null_field(self):
        couriers = CourierMethods()
        couriers.post_couriers(
            urls.BASE_URL, urls.CREATE_COURIERS_URL, data.create_couriers
        )
        response = couriers.login_couriers(
            urls.BASE_URL, urls.LOGIN_COURIERS_URL, data.login_couriers
        )
        id_couriers = response.json()['id']
        assert response.status_code == 200 and response.text, (
            f"status_code = {response.status_code}, response_text = {response.text}"
        )
        couriers.delete_couriers(urls.BASE_URL, urls.DELETE_COURIERS_URL, id_couriers)


    # Система вернет ошибку, если неправильно указать логин или пароль
    @allure.title('Проверка, что система вернет ошибку, если неправильно указать логин или пароль')
    @allure.description('Создаем курьера, логини с некорректными данными, проверяем, удаляем')
    def test_with_uncurrent_login(self):
        couriers = CourierMethods()
        couriers.post_couriers(
            urls.BASE_URL, urls.CREATE_COURIERS_URL, data.create_couriers
        )
        response = couriers.login_couriers(
            urls.BASE_URL, urls.LOGIN_COURIERS_URL, data.uncurrent_login
        )
        assert response.status_code == 404 and response.text, (
            f"status_code = {response.status_code}, response_text = {response.text}"
        )
        response = couriers.login_couriers(
            urls.BASE_URL, urls.LOGIN_COURIERS_URL, data.login_couriers
        )
        id_couriers = response.json()['id']
        couriers.delete_couriers(urls.BASE_URL, urls.DELETE_COURIERS_URL, id_couriers)


    # Если какого-то поля нет, запрос возвращает ошибку
    @allure.title('Проверка, что если какого-то поля нет, запрос возвращает ошибку')
    @allure.description('Создаем курьера, логиним с некорректными данными, проверяем, удаляем')
    def test_login_with_not_field(self):
        couriers = CourierMethods()
        couriers.post_couriers(
            urls.BASE_URL, urls.CREATE_COURIERS_URL, data.create_couriers
        )
        response = couriers.login_couriers(
            urls.BASE_URL, urls.LOGIN_COURIERS_URL, data.not_field_login
        )
        assert response.status_code == 400 and response.text, (
            f"status_code = {response.status_code}, response_text = {response.text}"
        )
        response = couriers.login_couriers(
            urls.BASE_URL, urls.LOGIN_COURIERS_URL, data.login_couriers
        )
        id_couriers = response.json()['id']
        couriers.delete_couriers(urls.BASE_URL, urls.DELETE_COURIERS_URL, id_couriers)


    # Если авторизоваться под несуществующим пользователем, запрос вернет ошибку
    @allure.title('Провера, что если авторизоваться под несуществующим пользователем, запрос вернет ошибку')
    @allure.description('Логиним курьера с некорректными данными')
    def test_login_doesnt_exist_couriers(self, generate_data_login_couriers):
        couriers = CourierMethods()
        response = couriers.login_couriers(
            urls.BASE_URL, urls.LOGIN_COURIERS_URL, generate_data_login_couriers
        )
        assert response.status_code == 404 and response.text, (
            f"status_code = {response.status_code}, response_text = {response.text}"
        )


    # Успешный запрос возвращает id
    @allure.title('Проверка, что успешный запрос возвращает ID')
    @allure.description('Создаем курьера, логиним с корректными данными, проверяем, удаляем')
    def test_login_couriers_and_return_id(self):
        couriers = CourierMethods()
        couriers.post_couriers(
            urls.BASE_URL, urls.CREATE_COURIERS_URL, data.create_couriers
        )
        response = couriers.login_couriers(
            urls.BASE_URL, urls.LOGIN_COURIERS_URL, data.login_couriers
        )
        id_couriers = response.json()['id']
        assert "id" in response.text and response.status_code, (
            f"status_code = {response.status_code}, response_text = {response.text}"
        )
        couriers.delete_couriers(urls.BASE_URL, urls.DELETE_COURIERS_URL, id_couriers)
