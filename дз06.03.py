is_continue = True
while is_continue:
    print(" 1 - map числа в строку\n"
          " 2 - filter > 0\n"
          " 3 - filter палиндром\n"
          " 4 - декоратор\n"
          " 5 - площадь квартиры\n"
          " 6 - имт\n"
          " 7 - калькулятор\n"
          " 8 - фильтр фото\n"
          " 9 - exit\n")


    def get_int_input(prompt):
        while True:
            try:
                int_num = int(input(prompt))
                return int_num
            except ValueError:
                print("Введите целое число!")


    user_choice = get_int_input("Enter action number: ")
    if user_choice == 1:
        sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(list(map(str, sequence)))

    elif user_choice == 2:
        sequence_two = [-10, -6, 7, 4, 2, -4, 7, 1, -15, -18, 17, 62]
        print(list(filter(lambda x: x > 0, sequence_two)))

    elif user_choice == 3:
        def is_palindrome(word):
            s = word.lower().replace(" ", "")
            return s == s[::-1]

    word = ["abccba", "hsdhee", "level", "fjkroeolel", "radar", "fjfkkk", "civic", "madam", "hffhfhfh"]
    print(list(filter(is_palindrome, word)))
