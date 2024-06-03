# Задание: напишите программу на Python, которая будет вычислять хэш-значения.

import hashlib

choice = int(input('Для вычисления хэш-значения вы можете ввести слово(нажмите 1) '
                   'или путь к файлу (нажмите 2). Ваш выбор: '))
match choice:
    case 1:
        word_to_encrypt = input('Введите слово для вычисления хэш-значения: ')
        sha256_hash = hashlib.new('sha256')
        data = word_to_encrypt.encode()
        sha256_hash.update(data)
        sha256_hex = sha256_hash.hexdigest()
        print(f'SHA-256: {sha256_hex}')

    case 2:
        file_path = input('Введите путь к файлу для хэширования (без кавычек): ')
        sha256_hash = hashlib.new('sha256')
        with open(file_path, 'rb') as file:
            while True:
                data = file.read()
                if not data:
                    break
                sha256_hash.update(data)

        print(f'SHA-256: {sha256_hash.hexdigest()}')
