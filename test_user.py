from unittest import TestCase
from user import *


class TestUser(TestCase):
    def test_set_password(self):
        test_user = User('Test Name', 'Test Login', 'testpassword')
        test_user.set_password('newpassword')

        assert test_user.get_password() == 'newpassword'

    def test_set_login(self):
        test_user = User('Test Name', 'Test Login', 'testpassword')
        test_user.set_login('New Login')

        assert test_user.get_login() == 'New Login'

    def test_generate_random_password(self):
        test_user = User('Test Name', 'Test Login', 'testpassword')
        former_password = test_user.get_password()
        test_user.generate_random_password()

        assert len(test_user.get_password()) == 8
        assert former_password != test_user.get_password()
