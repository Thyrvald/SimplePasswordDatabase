def encrypt(string_to_encrypt):
    encrypted_string = ''
    encrypting_table = create_encrypting_table()
    string_with_code_word = create_string_with_code_word(string_to_encrypt)
    for i in range(len(string_to_encrypt)):
        for encrypted_alphabet in encrypting_table:
            if encrypted_alphabet[0] == string_to_encrypt[i]:
                for letter in encrypting_table[0]:
                    if letter == string_with_code_word[i]:
                        letter_index = encrypting_table[0].index(letter)
                        encrypted_string += encrypted_alphabet[letter_index]

    return encrypted_string


def decrypt(string_to_decrypt):
    decrypted_string = ''
    encrypting_table = create_encrypting_table()
    string_with_code_word = create_string_with_code_word(string_to_decrypt)
    for i in range(len(string_to_decrypt)):
        for encrypted_alphabet in encrypting_table:
            if encrypted_alphabet[0] == string_with_code_word[i]:
                for letter in encrypted_alphabet:
                    if letter == string_to_decrypt[i]:
                        letter_index = encrypted_alphabet.index(letter)
                        decrypted_string += encrypting_table[0][letter_index]
    return decrypted_string


def encrypt_file(file_name):
    with open(file_name, 'r+') as f:
        content = ''
        for l in f:
            line = l.strip('\n')
            content += encrypt(line) + '\n'
    with open(file_name, 'w') as f:
        f.write(content)


def decrypt_file(file_name):
    with open(file_name) as f:
        content = ''
        for l in f:
            line = l.strip('\n')
            content += decrypt(line) + '\n'
    with open(file_name, 'w') as f:
        f.write(content)


def clear_file(file_name):
    with open(file_name, 'w') as f:
        f.write('')


def create_string_with_code_word(string_to_encrypt):
    code_word = 'vigenere'
    string_with_code_word = ''
    while len(string_with_code_word) < len(string_to_encrypt):
        string_with_code_word += code_word
    if len(string_with_code_word) > len(string_to_encrypt):
        string_with_code_word = string_with_code_word[:len(string_to_encrypt)]
    return string_with_code_word


def create_encrypting_table():
    list_of_alphabets = []
    for i in range(0, 91):
        alphabet = []
        for j in range(0, 91):
            if j + i + 32 < 123:
                alphabet.append(chr(j + i + 32))
            else:
                alphabet.append(chr(j + i - 59))
        list_of_alphabets.append(alphabet)
    return list_of_alphabets
