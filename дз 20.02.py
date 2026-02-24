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
        if len(digits) == len(set(digits)): # set(digits) уберет дубликаты. если длины не равны, значит есть дубликаты
            print("Все числа в списке уникальны")
        else:
            print("В списке есть повторяющиеся элементы")
            counts = {} # создается пустой словарь, чтобы хранить какое число скока раз встретилось
            for dig in digits:
                if dig in counts:
                    counts[dig] += 1 # если число уже встречалось
                else:
                    counts[dig] = 1 # если число встр впервые
            print("Повторяющиеся элементы: ")
            for dig, count in counts.items():
                if count > 1:
                    print(f"Число {dig} встречается {count} раза")
            print(sep="\n")



