import random
from test_framework.helpers.data_collector import DataCollector
from test_framework.steps.steps import Steps


class TestProject:
    def test_user(self):
        data = DataCollector()
        data.username = f"Tester{random.random()}"
        data.password = "qwerty123"
        data.phone = "+79259216306"

        # Регистрация пользователя
        Steps().user_registration(data)

        # Авторизация пользователя
        Steps().user_auth(data)

        # Регистрация пользователя
        Steps().user_get_info(data)

        # Добавление контакта пользователю
        Steps().user_add_contact(data)

        # Удаление контакта пользователя
        Steps().user_delete_contact(data)

        # Проверка отображения username на HTML-page
        Steps().check_username_on_html_page(data)
