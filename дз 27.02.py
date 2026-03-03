from wsgiref.util import shift_path_info

is_continue = True
while is_continue:
    print(" 1 - Рекурсия. Бинарный поиск\n"
          " 2 - Перевод из 10-ной системы счисления в 2-ную\n"
          " 3 - Простое ли число\n"
          " 4 - НОД\n"
          " 5 - Шифр Цезаря\n"
          " 6 - Шифр Виженера\n"
          " 7 - Сжатие строки\n"
          " 8 - Спам - фильтр\n"
          " 9 - Имитация «Генетического алгоритма»\n"
          "10 - Транслитератор\n"
          "11 - Поиск «Пиков» в списке\n"
          "12 - exit\n")


    def get_int_input(prompt):
        while True:
            try:
                int_num = int(input(prompt))
                return int_num
            except ValueError:
                print("Введите целое число!")


    user_choice = get_int_input("Enter action number: ")
    if user_choice == 1:
        def binary_search(numbers, left, right, goal):
            if left > right:
                return -1
            # принято возвращать -1, если функция должна вернуть индекс, но не смогла найти
            mid = (left + right) // 2
            if numbers[mid] == goal:
                return mid  # возвращает индекс, а если было бы return numbers[mid] - вернуло бы само значение из списка
            elif numbers[mid] > goal:
                return binary_search(numbers, left, mid - 1, goal)
            else:
                return binary_search(numbers, mid + 1, right, goal)


        numbers = [1, 5, 7, 16, 23, 28, 31, 38, 42]
        print("List of numbers: ", numbers)
        goal = get_int_input("Enter the number from the list to be depicted: ")
        result = binary_search(numbers, 0, len(numbers) - 1, goal)  # задаются лев и правая границы
        if result != -1:
            print(f"Element {goal} has an index: {result}")
        else:
            print("Element is not found. Try again!")

    elif user_choice == 2:
        def from_decimal_to_binary(number):
            binary_number = ""
            while number > 0:
                binary_number += str(number % 2)
                number //= 2
            return binary_number


        number = get_int_input("Enter a decimal number: ")
        result = from_decimal_to_binary(number)
        print(f"Your number {number} from decimal to binary system: {result}")

    elif user_choice == 3:
        import math


        def prime_number(num):
            if num <= 1:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            limit = int(math.sqrt(num)) + 1
            for i in range(3, limit, 2):  # означает: «начни с 3, иди до лимита с шагом 2».
                # То есть мы проверяем делители: 3, 5, 7, 9, 11...
                # четные не проверяем, потому что в самом начале функции мы уже проверили число на четность
                if num % i == 0:
                    return False
            return True


        num = get_int_input("Enter a number: ")
        if prime_number(num):
            print(f"Number {num} is a prime number!")
        else:
            print(f"Number {num} is not a prime number.")

    elif user_choice == 4:
        def gcd(number_one, number_two):
            while number_two:
                number_one, number_two = number_two, number_one % number_two
            return number_one
            #  a = 15, b = 10.


        # Проверяем while b (10 — это не ноль, заходим в цикл).
        # Считаем остаток: 15 % 10 = 5.
        # переменные меняются: a становится равным b (10), а b становится равным остатку (5).
        # Проверяем while b (5 — это не ноль).
        # Считаем остаток: 10 % 5 = 0 и т д

        number_one = get_int_input("Enter the first number: ")
        number_two = get_int_input("Enter the second number: ")
        result = gcd(number_one, number_two)
        print(f"GCD of your numbers is: {result}")

    elif user_choice == 5:
        shift = 4


        def caesar_encyption(message, shift):
            encrypted_message = ""
            for char in message:
                if char.isalpha():
                    start = ord("A") if char.isupper() else ord("a")
                    # Сдвигаем внутри диапазона 26 букв алфавита
                    shifted_char = chr((ord(char) - start + shift) % 26 + start)
                    encrypted_message += shifted_char
                else:
                    encrypted_message += char  # Символы и пробелы оставляем как есть
            return encrypted_message


        def decrypt_message(message, shift):
            return caesar_encyption(message, -shift)


        decision = get_int_input("What do you want to do? - (1 - encrypt, 2 - decrypt):  ")
        message = input("Enter your message: ")
        if decision == 1:
            print(f" Encrypted message with a step = 4: {caesar_encyption(message, shift)}")
        elif decision == 2:
            print(f" Decrypted message with a step = 4: {decrypt_message(message, shift)}")
        else:
            print(f"Invalid input. Try again!")

    elif user_choice == 6:
        letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


        def vigenere_encryption(text, key):
            result = ""
            key_index = 0  # какую букву ключа мы сейчас используем
            for char in text.lower():
                if char in letters:
                    char_index = letters.find(char)  # Находим индекс (с 0) буквы текста в алфавите
                    current_key_char = key[key_index % len(key)].lower()
                    # Находим индекс буквы ключа, % len(key) заставляет ключ повторяться по кругу
                    shift = letters.find(current_key_char)
                    new_index = (char_index + shift) % len(letters)
                    result += letters[new_index]
                    key_index += 1
                else:
                    result += char
            return result


        def decrypt(text, key):
            result = ""
            key_index = 0
            for char in text.lower():
                if char in letters:
                    char_index = letters.find(char)
                    current_key_char = key[key_index % len(key)].lower()
                    shift = letters.find(current_key_char)
                    new_index = (char_index - shift) % len(letters)
                    result += letters[new_index]
                    key_index += 1
                else:
                    result += char
            return result


        print("--- Программа: Шифр Виженера ---")
        text = input("Enter your message: ")
        decision = get_int_input("What do you want to do? - (1 - encrypt, 2 - decrypt):  ")
        key_word = input("Enter your key word: ")
        if decision == 1:
            print(f"Encrypted message : {vigenere_encryption(text, key_word)}")
        elif decision == 2:
            print(f"Decrypted message : {decrypt(text, key_word)}")
        else:
            print(f"Invalid input. Try again!")

    elif user_choice == 7:
        def contract_text(text):
            if not text:
                return ""
            result = ""
            count = 1
            for i in range(1, len(text)):
                if text[i] == text[i - 1]:
                    count += 1  # символ такой же, как прошлый
                else:
                    result += text[i - 1] + str(count)  # символ изменился - записываем прошлый и его число
                    count = 1  # сброс счетчика для след символа
            result += text[-1] + str(count)  # для последнего символа
            return result


        text = input("Enter your message: ")
        res = contract_text(text)
        print(f" Your initial text: {text}. \n Contracted text: {res} ")

    elif user_choice == 8:
        import string

        def is_spam(text):
            bad_words = ["sale", "free", "discount", "win", "winner", "only today", "last chance"]
            words = text.split()
            bad_count = 0
            has_caps = False

            punctuation = string.punctuation

            for word in words:
                clean_word = word.strip(punctuation)  # очищаем слово от знаков по краям
                if not clean_word:
                    continue

                if clean_word.isupper() and len(clean_word) > 1:
                    has_caps = True

                if clean_word.lower() in bad_words:
                    bad_count += 1
            return bad_count > 3 or has_caps


        text = input("Enter your email message: ")
        result = is_spam(text)
        if result:
            print(f"This is spam!")
        else:
            print(f"This message is clean!")
