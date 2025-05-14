# Sprint_7


# Виртуально окружение

- создание venv если его нет: python -m venv venv # стандартный модуль venv
- активация на macOS: source venv/bin/activate

# Полезные команды

- установка allure = https://allurereport.org/docs/install-for-macos/
- установка последней версии allure - pip install allure-pytest
- после прописать путь по папки bin пример - export PATH=$PATH:/home/user/tools/allure-2.29.0/bin
- pip install -r requirements.txt - установка зависимостей
- pip freeze > requirements.txt - генерация файла с зависимостями
- pytest test/ --alluredir=allure_results - запуск тестов с отчетом allure
- allure serve allure_results - открытие отчета в UI
- pytest test/ - запуст тестов без отчета allure
- allure generate allure_results - генерация отчета для открытия на другом устройстве

# Подключение логирования 
import logging
import http.client
- Включаем debug-логирование для urllib3
http.client.HTTPConnection.debuglevel = 1

- Настраиваем логирование
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

# Тесты

- test_login_couriers - тесты логина курьера
- test_post_couriers - тесты создания курьера
- test_get_orders - тесты получения списка заказов
- test_post_orders - тесты создания заказов

# Описание методов

- couriers_methods - описание методов курьера
- get_orders_methods - описание методов получения заказов
- post_orders_methods - описание метовод создания заказов