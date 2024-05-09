class UserModel:
    def __init__(self, id:int, username: str, first_name: str, last_name: str, email: str, password: str, phone: int, user_status=0):
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone
        self.user_status = user_status

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
            "password": self.password,
            "phone": self.phone,
            "userStatus": self.user_status
        }
