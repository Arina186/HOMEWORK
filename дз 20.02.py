is_continue = True
while is_continue:
    print(" 1 - Маша\n"
          " 2 - Фибоначчи\n"
          " 3 - Сумма всех чисел в списке\n"
          " 4 - Уникальность элементов списка\n"
          " 5 - Бинарный поиск\n"
          " 6 - Сдвинутый список\n"
          " 7 - Матрица\n"
          " 8 - Кол-во гласных и согласных в строке\n"
          " 9 - Простое число\n"
          "10 - Совершенное число\n"
          "11 - Число Армстронга\n"
          "12 - Пока число не станет равным 1\n"
          "13 - exit\n")
    user_choice = input("Enter action number: ")
    if user_choice == '1':
        n = input("Сколько стоит телефон (N)? ")
        k = input("Сколько Маша откладывает в день (К)? ")
        if n.isdigit() and k.isdigit():
            n = int(n)
            k = int(k)
            savings = 0
            days = 0
            while savings < n:
                days += 1  # наступил новый день
                # #проверить не воскресенье ли сегодня, каждый 7-й день (7, 14, 21, 28) - это вс
                if days % 7 == 0:
                    # в вс она тратит, не копит=не прибавляем деньги, пропускаем
                    pass
                else:
                    savings += k
            print(f"Маша накопит нужную сумму за {days} дней.")
        else:
            print("Enter only integer numbers!")
        print(sep="\n")

    elif user_choice == '2':
        numbers = input("Сколько чисел Фибоначчи вывести? ")
        if numbers.isdigit():
            numbers = int(numbers)
            a = 1  # Первое число
            b = 1  # Второе число
            count = 0
            print("Последовательность: ", end=" ")
            while count < numbers:
                print(a, end=" ")  # end чтобы числа выводились в одну строку
                a, b = b, a + b
                count += 1
        print(sep="\n")

    elif user_choice == '3':
        number = [3, 5, 12, 6, 25, 4, 9, 17, 76, 1]
        total_sum = sum(number)
        min_value = min(number)
        max_value = max(number)
        print(f"Сумма: {total_sum}")
        print(f"Минимум: {min_value}")
        print(f"Максимум: {max_value}")
        print(sep="\n")
    elif user_choice == '4':
        digits = [4, 5, 56, 34, 3, 1, 2, 5, 4, 67, 98, 66, 33, 44, 33, 4, 1, 90]
        print(f"Список чисел: ", digits)
        if len(digits) == len(set(digits)):  # set(digits) уберет дубликаты. если длины не равны, значит есть дубликаты
            print("Все числа в списке уникальны")
        else:
            print("В списке есть повторяющиеся элементы")
            counts = {}  # создается пустой словарь, чтобы хранить какое число скока раз встретилось
            for dig in digits:
                if dig in counts:
                    counts[dig] += 1  # если число уже встречалось
                else:
                    counts[dig] = 1  # если число встр впервые
            print("Повторяющиеся элементы: ")
            for dig, count in counts.items():
                if count > 1:
                    print(f"Число {dig} встречается {count} раза")
            print(sep="\n")

    elif user_choice == '5':
        numbers = [5, 7, 16, 23, 28, 31, 38, 42, 46, 53, 57, 74, 81, 85, 87]
        print("Список чисел: ", numbers)
        digit = input("Введите число из списка, которое хотели бы отобразить: ")
        if digit.isdigit():
            digit = int(digit)
            left = 0
            right = len(numbers) - 1
            attempts = 0
            mid = 0
            while left <= right and numbers[mid] != digit:
                attempts += 1
                mid = (left + right) // 2
                if numbers[mid] > digit:
                    right = mid - 1
                elif numbers[mid] < digit:
                    left = mid + 1
            if numbers[mid] == digit:
                print(f"Число {digit} найдено за {attempts} попыток")
            else:
                print(f"Число {digit} не найдено в списке")
            print(sep="\n")

    elif user_choice == '6':
        numbers = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
        print("Список чисел: ", numbers)
        digit = input("Введите число из списка, которое хотели бы отобразить: ")
        if digit.isdigit():
            digit = int(digit)
            left = 0
            right = len(numbers) - 1
            mid = 0
            while left <= right and numbers[mid] != digit:
                mid = (left + right) // 2
                if numbers[mid] == digit:
                    continue
                if numbers[left] <= numbers[mid]:  # левая часть отсортирована
                    if numbers[left] <= digit < numbers[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if numbers[mid] < digit <= numbers[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
            if numbers[mid] == digit:
                print(f"Число {digit} найдено на {mid} позиции")
            else:
                print(f"Число {digit} не найдено в списке")
            print(sep="\n")

    elif user_choice == '7':
        from random import randint

        rows_number = int(input("Enter rows number: "))
        columns_number = int(input("Enter columns number: "))
        if rows_number != columns_number:
            print("Только квадратные матрицы!")
        else:
            matrix = []
            for r_num in range(0, rows_number):
                empty_row = []
                matrix.append(empty_row)
                for c_num in range(0, columns_number):
                    elem = randint(0, 100)
                    matrix[r_num].append(elem)
                print(matrix[r_num])
            secondary_sum = 0
            for r_num in range(0, rows_number):
                formula = columns_number - 1 - r_num
                secondary_sum += matrix[r_num][formula]
            print(f"Sum of a secondary diagonal is: {secondary_sum}")
            print(sep="\n")

    elif user_choice == '8':
        string = "спаспачвЕНЁнпгртроыуыу"
        vowels = "аеёиоуыэяАЕЁИОУЫЭЯ"
        consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
        vowels_count = 0
        consonants_count = 0
        for char in string:
            if char in vowels:
                vowels_count += 1
            elif char in consonants:
                consonants_count += 1
        print(f"Количество гласных: {vowels_count}")
        print(f"Количество согласных: {consonants_count}")
        print(sep="\n")

    elif user_choice == '9':
        number = input("Введите число: ")
        if number.isdigit():
            number = int(number)
            if number < 2:
                print("1 не является простым числом!")
            else:
                is_prime = True
                i = 2
                while i * i <= number and is_prime:
                    if number % i == 0:
                        is_prime = False
                    i += 1  # В отличие от цикла for, который сам переходит к следующему числу,
                # цикл while будет работать бесконечно с одним и тем же значением, если мы не будем его менять вручную
                if is_prime:
                    print(f"Число {number} - простое")
                else:
                    print(f"Число {number} - не простое")
                print(sep="\n")

    elif user_choice == '10':
        number = input("Введите предел N: ")
        if number.isdigit():
            number = int(number)
            print(f"Совершенные числа до {number}: ")
            for i in range(1, number + 1):
                summa = 0
                for j in range(1, i):  # проверяет все числа которые меньше текущего i
                    if i % j == 0:  # ищем делители
                        summa += j
                if summa == i:
                    print(f"Число {i} - совершенное")
                else:
                    print("Совершенных чисел нет до указанного предела!")
        print(sep="\n")

    elif user_choice == '11':
        number = input("Введите число N: ")
        if number.isdigit():
            number = int(number)
            power = len(str(number))
            summa = 0
            for digit in str(number):  # str(number) превратит число 153 в '1', '5', '3'
                summa += int(digit) ** power
            if summa == number:
                print(f"Число {number} - число Армстронга")
            else:
                print(f"Число {number} - НЕ число Армстронга")
        print(sep="\n")

    elif user_choice == '12':
        number = input("Введите число: ")
        if number.isdigit():
            number = int(number)
            original_number = number  # чтобы вывести в консоле изначально введенное число, а не преобразованную единицу
            steps = 0
            while number != 1:
                if number % 2 == 0:
                    number //= 2
                    steps += 1
                else:
                    number = number * 3 + 1
                    steps += 1
            print(f"Для числа {original_number} нужно {steps} шагов, чтобы получить 1")

    elif user_choice == '13':
        print("До свидания!")
        is_continue = False
