import allure
import urls
from methods.get_orders_methods import GetOrderMethods



@allure.feature('Проверки ручки получения списка заказов')
class TestGetOrders:

    # В тело ответа возвращается список заказов
    @allure.title('Проверка, что тело ответа возвращает список заказов')
    @allure.description('Получаем список заказов')
    def test_get_orders(self):
        orders = GetOrderMethods()
        status_code, response_text = orders.get_orders(urls.BASE_URL, urls.GET_ORDERS_URL)
        assert "orders" in response_text, (
            f"status_code = {status_code}, response_text = {response_text}"
        )
