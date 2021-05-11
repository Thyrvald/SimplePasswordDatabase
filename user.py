import random


class User:

    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password

    def get_password(self):
        return self.password

    def get_login(self):
        return self.login

    def get_name(self):
        return self.name

    def set_password(self, new_password):
        self.password = new_password

    def set_login(self, new_login):
        self.login = new_login

    def generate_random_password(self):
        random_password = ''
        for i in range(8):
            ascii_code = random.randint(32, 122)
            while ascii_code == 44:
                ascii_code = random.randint(32, 122)
            random_password += chr(ascii_code)
        self.set_password(random_password)
