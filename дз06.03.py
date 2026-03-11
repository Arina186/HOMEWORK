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

    elif user_choice == 4:
        from functools import reduce

        rooms = [
            {"name": "Kitchen", "length": 6, "width": 4},
            {"name": "Room 1", "length": 5.5, "width": 4.5},
            {"name": "Room 2", "length": 5, "width": 4},
            {"name": "Room 3", "length": 7, "width": 6.3},
        ]
        separate_square = list(map(lambda x: x["length"] * x["width"], rooms))
        print(f"Площадь каждой комнаты: {separate_square} ")
        print(f"Общая площадь квартиры: ", reduce(lambda x, y: x + y, separate_square))

    elif user_choice == 5:

        try:
            cholesterol = float(input("Enter your level of cholesterol: "))
            sugar = float(input("Enter your level of sugar: "))
            bmi = float(input("Enter your bmi: "))
            systolic_blood_pressure = int(input("Enter your upper blood pressure: "))
            diastolic_blood_pressure = int(input("Enter your diastolic blood pressure: "))
            age = int(input("Enter your age: "))
            smoking = input("Do you smoke? (yes/no): ").lower() == "yes"
            elevated_count = 0  # счетчик количества отклонений по каждому показателю

            if cholesterol >= 5.2: elevated_count += 1
            if sugar >= 5.5: elevated_count += 1
            if bmi < 18.5 or bmi > 24.9: elevated_count += 1
            if systolic_blood_pressure > 130 or diastolic_blood_pressure > 85: elevated_count += 1
            severe_risk = (cholesterol > 6.5 or sugar > 7.0 or bmi > 30.0 or systolic_blood_pressure > 140
                           or diastolic_blood_pressure > 90)
            if bmi < 16 or bmi > 40:
                risk = "Special case: critical!"
            elif elevated_count >= 4 and smoking and age > 60:
                risk = "Critical"
            elif elevated_count >= 3 or severe_risk:
                risk = "High"
            elif 1 <= elevated_count <= 2 or age > 45:
                risk = "Moderate"
            else:
                risk = "Low"

            print(f"Test result: {risk}")

        except ValueError:
            print("Error: Please, enter only numbers! (for float numbers use a point).")
        except Exception as e:
            print(f"Occurred unexpected error: {e}")


