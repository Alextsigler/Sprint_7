import allure
import pytest
import data
import urls
from methods.courier_methods import CourierMethods


@allure.feature('Проверки на создание курьера')
class TestPostCouriers:

    # Курьера можно создать
    @allure.title('Проверка, что курьера можно создать')
    @allure.description('Создаем курьера с корректными данными')
    def test_post_couriers(self, generate_data_create_couriers):
        couriers = CourierMethods()
        status_code, response_text = couriers.post_couriers(
            urls.BASE_URL, urls.CREATE_COURIERS_URL, generate_data_create_couriers
        )
        assert status_code == 201 and response_text, (
            f"status_code = {status_code}, response_text = {response_text}"
        )

    # Нельзя создать двух одинаковых курьеров
    @allure.title('Проверка, что нельзя создать двух одинаковых курьеров')
    @allure.description('Создаем двух курьеров с одинаковыми данными')
    def test_create_dublicate_two_couriers(self):
        couriers = CourierMethods()
        couriers.post_couriers(urls.BASE_URL, urls.CREATE_COURIERS_URL, data.data_create_couriers)
        status_code, response_text = couriers.post_couriers(
            urls.BASE_URL, urls.CREATE_COURIERS_URL, data.data_create_couriers
        )
        assert status_code == 409 and response_text, (
            f"status_code = {status_code}, response_text = {response_text}"
        )

    # Чтобы создать курьера. нужно передать в ручку все обязательные поля
    @allure.title('Проверка, чтобы создать курьера нужно передать все обязательные поля')
    @allure.description('Создаем курьера без логина или пароля')
    @pytest.mark.parametrize('data_field',
                             [
                                 data.data_create_null_field[0],
                                 data.data_create_null_field[1]
                             ]
                             )
    def test_create_null_requaments_field(self, data_field):
        couriers = CourierMethods()
        status_code, response_text = couriers.post_couriers(
            urls.BASE_URL, urls.CREATE_COURIERS_URL, data_field
        )
        assert status_code == 400 and response_text, (
            f"status_code = {status_code}, response_text = {response_text}"
        )

    # Запрос возвращает правильный код ответа
    @allure.title('Проверка, что запрос возвращает правильный код ответа')
    @allure.description('Создаем курьера с корректными данными')
    def test_post_couriers_return_current_status_code(self, generate_data_create_couriers):
        couriers = CourierMethods()
        status_code, response_text = couriers.post_couriers(
            urls.BASE_URL, urls.CREATE_COURIERS_URL, generate_data_create_couriers
        )
        assert status_code == 201, (
            f"status_code = {status_code}, response_text = {response_text}"
        )

    # Успешный запрос возвращает {"ok": true};
    @allure.title('Проверка, что запрос возвращает правильное тело ответа')
    @allure.description('Создаем курьера с корректными данными')
    def test_post_couriers_return_current_response_text(self, generate_data_create_couriers):
        couriers = CourierMethods()
        status_code, response_text = couriers.post_couriers(
            urls.BASE_URL, urls.CREATE_COURIERS_URL, generate_data_create_couriers
        )
        assert response_text == '{"ok":true}', (
            f"status_code = {status_code}, response_text = {response_text}"
        )

    # Если одного из полей нет, запрос возвращает ошибку
    @allure.title('Проверка, что если одного из полей нет, запрос возвращает ошибку')
    @allure.description('Создаем курьера без логина или пароля')
    @pytest.mark.parametrize('data_field',
                             [
                                 data.data_create_not_field[0],
                                 data.data_create_not_field[1]
                             ]
                             )
    def test_create_not_full_requaments_field(self, data_field):
        couriers = CourierMethods()
        status_code, response_text = couriers.post_couriers(
            urls.BASE_URL, urls.CREATE_COURIERS_URL, data_field
        )
        assert status_code == 400 and response_text, (
            f"status_code = {status_code}, response_text = {response_text}"
        )


    # Если создать пользователя с логином, который уже есть, возвращается ошибка
    @allure.title('Проверка, что если создать пользователя с логином, который уже есть, вовращается ошибка')
    @allure.description('Создаем курьера с данными которые уже есть')
    def test_create_dublicate_login_couriers(self):
        couriers = CourierMethods()
        couriers.post_couriers(urls.BASE_URL, urls.CREATE_COURIERS_URL, data.data_create_couriers)
        status_code, response_text = couriers.post_couriers(
            urls.BASE_URL, urls.CREATE_COURIERS_URL, data.data_create_couriers
        )
        assert status_code == 409 and response_text, (
            f"status_code = {status_code}, response_text = {response_text}"
        )
