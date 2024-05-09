import requests

class ApiService:
    BASE_URL = "https://petstore.swagger.io/v2"

    def __init__(self):
        self.session = requests.Session()

    def create_user(self, user_data):
        url = f"{self.BASE_URL}/user"
        response = self.session.post(url, json=user_data)
        return response

    def get_user(self, username):
        url = f"{self.BASE_URL}/user/{username}"
        response = self.session.get(url)
        return response

    def update_user(self, username, user_data):
        url = f"{self.BASE_URL}/user/{username}"
        response = self.session.put(url, json=user_data)
        return response

    def delete_user(self, username):
        url = f"{self.BASE_URL}/user/{username}"
        response = self.session.delete(url)
        return response

        
    def login(self, email, password):
        url = f"{self.BASE_URL}/user/login"
        params = {
            "email": email,
            "password": password
        }
        response = self.session.get(url, params=params)
        return response