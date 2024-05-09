from faker import Faker
from models.user_model import UserModel
import random


fake = Faker()

class DataGenerator:
    @staticmethod
    def generate_user(valid=True):
        user = UserModel(
            id =random.randint(0, 9999),
            username=fake.user_name(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email() if valid else "invalid-email",
            password=fake.password(),
            phone=fake.phone_number(),
            user_status=fake.random_int(min=0, max=1)
        )
        return user
