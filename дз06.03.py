is_continue = True
while is_continue:
    print(" 1 - map числа в строку\n"
          " 2 - filter > 0\n"
          " 3 - filter палиндром\n"
          " 4 - площадь квартиры\n"
          " 5 - имт\n"
          " 6 - калькулятор\n"
          " 7 - фильтр фото\n"
          " 8 - exit\n")


    def get_int_input(prompt):
        while True:
            try:
                int_num = int(input(prompt))
                return int_num
            except ValueError:
                print("Введите целое число!")


    import time


    def repeat(n):
        def timer_decorator(func):
            def wrapper(*args, **kwargs):
                start_time = time.time()  # засекаем общее начало отсчета
                for sth in range(n):
                    func(*args, **kwargs)  # вызываем ф-цию n раз
                end_time = time.time()  # время конца
                average_time = (end_time - start_time) / n

                print(f"Среднее время выполнения функции {func.__name__} за {n} запусков: {average_time} сек ")
                return average_time

            return wrapper

        return timer_decorator


    user_choice = get_int_input("Enter action number: ")
    if user_choice == 1:
        sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(list(map(str, sequence)))

    elif user_choice == 2:
        @repeat(5)
        def some_task():
           sequence_two = [-10, -6, 7, 4, 2, -4, 7, 1, -15, -18, 17, 62]
           print(list(filter(lambda x: x > 0, sequence_two)))

        some_task()

    elif user_choice == 3:
        def is_palindrome(word):
            s = word.lower().replace(" ", "")
            return s == s[::-1]

        word = ["abccba", "hsdhee", "level", "fjkroeolel", "radar", "fjfkkk", "civic", "madam", "hffhfhfh"]
        print(list(filter(is_palindrome, word)))


