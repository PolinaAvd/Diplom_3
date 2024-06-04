import random

class UserFactory:
    @staticmethod
    def create_user_with_random_param():

        return {
            "email": f'{random.randint(0, 1000000)}@mail.ru',
            "password": f'{random.randint(0, 100000000)}',
            "name": 'Dianaaa'

        }



password_random = f'Pass{random.randint(100, 999)}'
email_random = f"polina_avdohina_k7_{random.randint(100, 99999)}@gmail.com"
