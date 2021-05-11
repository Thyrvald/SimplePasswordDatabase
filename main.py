import sys

from user import *
from web_page import *
from encrypting import *


def main():
    database_file_name = 'passwords.txt'
    # encrypt_file(database_file_name) # uncomment if the file need to be encrypted first
    decrypt_file(database_file_name)
    page_base = load_data_from_file(database_file_name)
    clear_file(database_file_name)

    while True:
        user_input = input(
            "\nWhat do you want to do? \n-Type 1 to print data\n-Type 2 to modify data\n-Type 3 to "
            "introduce a new user\n-Type exit to exit\n")
        if user_input == 'exit':
            load_data_to_file(database_file_name, page_base)
            encrypt_file(database_file_name)
            break
        elif user_input == "1":
            # data access
            user_input = input("-Type 1 to print all data\n-Type 2 to group data by page type"
                               "\n-Type 3 to print pages just for one type"
                               "\n-Type anything else to go back to main menu\n-Type exit to exit\n")
            if user_input == 'exit':
                load_data_to_file(database_file_name, page_base)
                encrypt_file(database_file_name)
                break
            elif user_input == '1':
                print_all_data(page_base)
            elif user_input == '2':
                group_data_by_page_type(page_base)
            elif user_input == '3':
                print_one_page_group(page_base)
        elif user_input == '2':
            # data modification
            user_input = input("-Type 1 to change user's login\n-Type 2 to change user's password"
                               "\n-Type anything else to go back to main menu\n-Type exit to exit\n")
            if user_input == 'exit':
                load_data_to_file(database_file_name, page_base)
                encrypt_file(database_file_name)
                break
            elif user_input == '1':
                # login change
                change_login_option(page_base)
            elif user_input == '2':
                # password change
                change_password_option(page_base)
        elif user_input == '3':
            # data introduction
            add_user(page_base)
        else:
            print("Enter a correct action code.")


def load_data_from_file(file_name):
    page_base = []
    with open(file_name) as f:
        for l in f:
            line = l.strip('\n').split(',')
            if is_page_in_database(page_base, line[0]):
                for page in page_base:
                    if page.page_name == line[0]:
                        page_index = page_base.index(page)
                if not is_user_in_page(page_base[page_index].users, line[2]):
                    page_base[page_index].users.append(User(line[2], line[3], line[4]))
            else:
                page_base.append(WebPage(line[0], line[1], [User(line[2], line[3], line[4])]))
    return page_base


def load_data_to_file(file_name, page_base):
    content = ''
    for page in page_base:
        for user in page.users:
            content += f"{page.get_page_name()},{page.get_page_type()},{user.get_name()}," \
                       f"{user.get_login()},{user.get_password()}\n"
    with open(file_name, 'w') as f:
        f.write(content)


def is_page_in_database(database, page):
    for data in database:
        if page == data.page_name:
            return True


def is_user_in_page(page, username):
    for user in page:
        if user.get_login() == username:
            return True


def print_user_data(page, user):
    print(f"Page: {page.page_name:25} | User: {user.name:25} | "
          f"User's login: {user.get_login():25} | User's password: {user.get_password():25}")


def print_all_data(page_base):
    for page in page_base:
        for user in page.users:
            print_user_data(page, user)


def get_page_types_from_database(page_base):
    page_types = []
    for page in page_base:
        if page_types is None:
            page_types.append(page.get_page_type())
        else:
            does_type_exist = False
            for page_type in page_types:
                if page_type == page.get_page_type():
                    does_type_exist = True
            if not does_type_exist:
                page_types.append(page.get_page_type())
    return page_types


def group_data_by_page_type(page_base):
    for page_type in get_page_types_from_database(page_base):
        print(f'\nType: {page_type}:\n')
        for page in page_base:
            if page.get_page_type() == page_type:
                for user in page.users:
                    print_user_data(page, user)


def print_one_page_group(page_base):
    print_existing_types(page_base)
    user_input = input('Type one of the listed categories, for which you want to printdata\n')
    does_type_exist = 0
    for page in page_base:
        if user_input == page.get_page_type():
            does_type_exist += 0
            for user in page.users:
                print_user_data(page, user)
    if does_type_exist == 0:
        print("There's no such category ina the database")


def print_existing_types(page_base):
    page_types = []
    for page in page_base:
        is_type_in_list = 0
        for page_type in page_types:
            if page_type == page.get_page_type():
                is_type_in_list += 1
        if is_type_in_list == 0:
            page_types.append(page.get_page_type())
    for page_type in page_types:
        print(page_type)


def change_user_password(user_input, password_policy, user):
    if user.get_login() == user_input:
        user_input = input(f'-Type 1 if you want to generate random password consistent with the following '
                           f' policy:\n{password_policy}\n-Type 2,  '
                           'if you want to change password  manually\n')
        if user_input == '1':
            user.generate_random_password()
        elif user_input == '2':
            user_input = input(f"Enter new password consistent with the following policy:{password_policy}")
            input_message = 'Enter password consistent with the given policy\n'
            user_input = is_password_long_enough(check_if_coma_was_typed(user_input, input_message),
                                                 input_message)
            user.set_password(user_input)
        print('Password successfully changed\n')


def change_password_option(page_base):
    user_input = input('Type for which page do you want to change password\n')
    password_policy = "\n-Password has to be at least 8 characters long\n-Password cannot include a coma!" \
                      "\n-Password can include the following characters:\n'A-B', 'a-b', '0-9', ' ', '.', '/', '!', '#', '$', " \
                      "'%', '&', '*', '(', ')', '-', '+', '\"', '@', '^', '<', '>', '=', ':', ';', " \
                      "'?', '`', '[', ']', '_'\n"
    if is_page_in_database(page_base, user_input):
        for page in page_base:
            if page.get_page_name() == user_input:
                user_input = input('Enter for which user do you want to change password\n')
                if is_user_in_page(page.users, user_input):
                    for user in page.users:
                        change_user_password(user_input, password_policy, user)
                else:
                    print('No such user in the database')
    else:
        print('No such page in the database')


def change_user_login(user_input, user):
    if user.get_login() == user_input:
        user_input = input('-Type new login (remember, it cannot include a coma!)\n')
        user_input = check_if_coma_was_typed(user_input, 'Type login without a coma!\n')
        user.set_login(user_input)
        print('Login successfully changed')


def change_login_option(page_base):
    user_input = input('Type for which page do you want to change login\n')
    if is_page_in_database(page_base, user_input):
        for page in page_base:
            if page.get_page_name() == user_input:
                user_input = input('Enter for which user do you want to change login\n')
                if is_user_in_page(page.users, user_input):
                    for user in page.users:
                        change_user_login(user_input, user)
                else:
                    print('No such user in the database')
    else:
        print('No such page in the database')


def add_user(page_base):
    user_input = input('Type for which page you want to introduce a new user\n')
    if is_page_in_database(page_base, user_input):
        for page in page_base:
            if page.get_page_name() == user_input:
                append_user(page.users)
    else:
        new_page_name = user_input
        user_input = input('No such page in the database\n-Type 1 to to introduce a new one\n-Type anything else '
                           'to go back to main menu\n')
        if user_input == '1':
            new_page_users = []
            append_user(new_page_users)
            new_page_type = input('Enter new page type\n')
            page_base.append(WebPage(new_page_name, new_page_type, new_page_users))


def append_user(users):
    new_user_login = input("Enter new user's login\n")
    if is_user_in_page(users, new_user_login):
        print('User already exists')
    else:
        new_user_login = check_if_coma_was_typed(new_user_login, 'Enter login bez coma!\n')
        new_user = input('Jak nazywa się użytkownik\n')
        new_user = check_if_coma_was_typed(new_user, 'Nie wprowadzaj coma!\n')
        new_user_password = input("Enter a password for a new user consistent with a following policy:\n"
                                  "-Password has to be at least 8 characters long\n-Password cannot include "
                                  "a coma!\n-Password can include the following characters:\n"
                                  "'A-B', 'a-b', '0-9', ' ', '.', '/', '!', '#', '$', '%', '&', '*', "
                                  "'(', ')', '-', '+', '\"', '@', '^', '<', '>', '=', ':', ';' '?', '`', "
                                  "'[', ']', '_'\n")
        input_message = 'Enter password consistent with the given policy\n'
        new_user_password = is_password_long_enough(check_if_coma_was_typed(new_user_password, input_message),
                                                    input_message)
        users.append(User(new_user, new_user_login, new_user_password))


def check_if_coma_was_typed(user_input, input_message):
    while True:
        was_coma_typed = 0
        for letter in user_input:
            if letter == ',':
                was_coma_typed += 1
                user_input = input(input_message)
            else:
                was_coma_typed += 0
        if was_coma_typed == 0:
            return user_input


def is_password_long_enough(user_input, input_message):
    while True:
        if len(user_input) < 8:
            user_input = input(input_message)
            user_input = check_if_coma_was_typed(user_input, input_message)
        else:
            user_input = user_input
            return user_input


if __name__ == "__main__":
    sys.exit(main())
