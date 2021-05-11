from unittest import TestCase
from main import *
from encrypting import *


class TestEncrypt(TestCase):
    def test_encrypting_and_decrypting(self):
        test_string = encrypt('helloworld')
        test_string = decrypt(test_string)

        assert test_string == 'helloworld'

    def test_create_string_with_code_word(self):
        test_string = create_string_with_code_word('teststringtocreateanother')

        assert test_string == 'vigenerevigenerevigenerev'

    def test_encrypt_file(self):
        with open('test_file.txt', 'w') as f:
            f.write('Test string to encrypt\nTest string 2 to encrypt')
        encrypt_file('test_file.txt')

        with open('test_file.txt', 'r+') as f:
            assert f.read() == f"{encrypt('Test string to encrypt')}\n{encrypt('Test string 2 to encrypt')}\n"

    def test_decrypt_file(self):
        with open('test_file.txt', 'w') as f:
            f.write('Test string to encrypt\nTest string 2 to encrypt')
        encrypt_file('test_file.txt')
        decrypt_file('test_file.txt')

        with open('test_file.txt', 'r+') as f:
            assert f.read() == 'Test string to encrypt\nTest string 2 to encrypt\n'

    def test_is_user_in_page(self):
        user = User('test', 'test', 'test')
        page = WebPage('test', 'test', [user])

        assert is_user_in_page(page.users, input('Enter a user "test"\n')) == True