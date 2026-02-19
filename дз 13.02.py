# 1 - логин и пароль
# 2 - треугольник
# 3 - проверка на високосность года
# 4 - шахматы
# 5 - шахматы 2
# 6 - точка в какой четверти коорд плоскости
# 7 - календарь
# 8 - римские цифры в арабские
# 9 - анализ мед обследования
# 10 - калькулятор
print("Our tasks:\n"
      "1 - login and password\n"
      "2 - triangle\n"
      "3 - leap year\n"
      "4 - chess\n"
      "5 - chess 2\n"
      "6 - coordinate plane\n"
      "7 - calendar\n"
      "8 - roman numerals\n"
      "9 - medical check-up"
      "10 - calculator")
chosen_task = input("Choose task number: ")

if chosen_task == "1":
    login = input("Enter your login: ")
    password = input("Enter your password: ")
    special_symbols = "!@#$%^&*()_+="
    password_set = set(password)
    digits = "0123456789"
    digits_set = set(digits)
    # isdisjoint = только для работы с множествами (set), смысл: "не имеют общих элементов"
    # isalnum строка содержит тока буквы и цифры без спецсимволов
    # password.lower() != password.upper() если пароль в нижнем регистре не равен паролю в нижнем, то там точно есть буквы
    if (len(password) >= 8 and password != login and not password_set.isdisjoint(digits_set) and password.lower() != password.upper()
            and password.isupper() != password and password.islower() != password and not password.isalnum()):
        print("Password is approved!")
    else:
        print("Password must contain letters, digits, a special symbol and at least 8 characters!")