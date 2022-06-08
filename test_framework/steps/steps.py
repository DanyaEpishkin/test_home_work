from selenium import webdriver
from selenium.webdriver.common.by import By
from test_framework.requests.requests import Requests
import chromedriver_autoinstaller


class Steps:
    def __init__(self):
        self.requests = Requests()

    def user_registration(self, data):
        response = self.requests.post_registration(data.username, data.password)
        assert response.status_code == 201, 'Некорректный статус код'
        assert response.json()['success'] is True, 'No success'
        assert response.json()['result']['user']['login'] == data.username, \
            f'Username не соответствует исходному: {data.username}'

        return response.json()

    def user_auth(self, data):
        response = self.requests.post_auth(data.username, data.password)
        assert response.status_code == 200, 'Некорректный статус код'
        assert response.json()['success'] is True, 'No success'
        assert response.json()['result']['user']['login'] == data.username, \
            f'Username не соответствует исходному: {data.username}'
        data.ssid = response.json()['result']['ssid']
        return response.json()

    def user_get_info(self, data):
        response = self.requests.get_user(data.ssid)
        assert response.status_code == 200, 'Некорректный статус код'
        assert response.json()['success'] is True, 'No success'
        assert response.json()['result']['user']['login'] == data.username, \
            f'Username не соответствует исходному: {data.username}'
        return response.json()

    def user_add_contact(self, data):
        response = self.requests.post_user_contact(data.ssid, data.phone)
        assert response.status_code == 200, 'Некорректный статус код'
        assert response.json()['success'] is True, 'No success'
        data.id_number = response.json()['result']['user']['contacts'][0]['id']
        return response.json()

    def user_delete_contact(self, data):
        response = self.requests.delete_user_contact(data.ssid, data.id_number)
        assert response.status_code == 200, 'Некорректный статус код'
        assert response.json()['success'] is True, 'No success'
        return response.json()

    def check_username_on_html_page(self, data):
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()
        driver.get(f"http://localhost:8080/session/{data.ssid}")
        expected_username = driver.find_element(By.CLASS_NAME, 'username').text
        assert data.username == expected_username, f'Имя пользователя username={data.username} не совпадает c ' \
                                                   f'полученным с HTML-page = {expected_username}'
