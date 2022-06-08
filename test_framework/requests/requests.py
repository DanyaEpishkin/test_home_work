import requests
import webbrowser


class Requests:
    def post_registration(self, username, password):
        json = {"user": {"login": username, "password": password}}
        return requests.post(url=f'http://localhost:8080/api/v1/user/registration', json=json)

    def post_auth(self, username, password):
        json = {"user": {"login": username, "password": password}}
        return requests.post(url=f'http://localhost:8080/api/v1/user/login', json=json)

    def get_user(self, ssid):
        return requests.get(url=f'http://localhost:8080/api/v1/user', headers={'ssid': ssid})

    def post_user_contact(self, ssid, phone):
        json = {
            "contact": {
                "type": "phone",
                "content": phone
            }
        }
        return requests.post(url=f'http://localhost:8080/api/v1/user/contact', headers={"ssid": ssid}, json=json)

    def delete_user_contact(self, ssid, id_number):
        return requests.delete(url=f'http://localhost:8080/api/v1/user/contact/{id_number}', headers={'ssid': ssid})

    def get_html_page(self, ssid):
        return webbrowser.open_new(url=f'http://localhost:8080/session/{ssid}')
