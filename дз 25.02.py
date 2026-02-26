is_continue = True
while is_continue:
    print(" 1 - Генерация матрицы\n"
          " 2 - min и max в матрице\n"
          " 3 - Сумма всех элементов в матрице\n"
          " 4 - Умножение элементов с K столбцом\n"
          " 5 - Сумма элементов строки матрицы\n"
          " 6 - Поиск числа Н в столбцах матрицы\n"
          " 7 - Матрица из 0 и 1 + добавление столбца\n"
          " 8 - exit\n")


    def get_int_input(prompt):
        while True:
            try:
                int_num = int(input(prompt))
                return int_num
            except ValueError:
                print("Введите целое число!")


    user_choice = get_int_input("Enter action number: ")
    if user_choice == '1':
        from random import randint


        def generate_random_matrix(rows_count, columns_count):
            matrix = []
            for row in range(0, rows_count):
                matrix.append([])
                for col in range(0, columns_count):
                    matrix[row].append(randint(0, 50))

            return matrix


        def show_matrix(matrix):
            for row in matrix:
                print(row)

            return matrix

        rows_number = get_int_input("Enter rows number: ")
        columns_number = get_int_input("Enter columns number: ")
        result = generate_random_matrix(rows_number, columns_number)
        print(f" \nВаша матрица:")
        show_matrix(result)

    user_choice = get_int_input("Enter action number: ")
    elif user_choice == '2':
        from random import randint


        def generate_random_matrix(rows_count, columns_count):
            matrix = []
            for row in range(0, rows_count):
                matrix.append([])
                for col in range(0, columns_count):
                    matrix[row].append(randint(0, 50))

            return matrix


        def show_matrix(matrix):
            for row in matrix:
                print(row)

            return matrix


        def min_value_matrix(matrix):
            # берем первый элемент 1 строки матрицы как начальный минимум
            minimum = matrix[0][0]
            min_row_index, min_col_index = 0, 0  #для отображения индекса найденного минимума
            for r_ind, row in enumerate(matrix):  #enumerate возвращает индекс и само значение
                for c_ind, item in enumerate(row):
                    if item<minimum:
                        minimum = item
                        min_row_index = r_ind
                        min_col_index = c_ind

            return minimum, (min_row_index, min_col_index)     # взяв в скобки мы сгруппировали неск значений в кортеж
# если не возьмем, то придется ниже брать 3 переменные (min_value, r_index, c_index)вместо 2-х (min_value, min_index)

        def max_value_matrix(matrix):
            maximum = matrix[0][0]
            max_row_index, max_col_index = 0, 0
            for r_ind, row in enumerate(matrix):
                for c_ind, item in enumerate(row):
                    if item>maximum:
                        maximum = item
                        max_row_index = r_ind
                        max_col_index = c_ind

            return maximum, (max_row_index, max_col_index)


        rows_number = get_int_input("Enter rows number: ")
        columns_number = get_int_input("Enter columns number: ")
        result = generate_random_matrix(rows_number, columns_number)
        print(f" \nВаша матрица:")
        show_matrix(result)
        min_value, min_index = min_value_matrix(result)
        max_value, max_index = max_value_matrix(result)
        print(f"Минимальное значение матрицы: {min_value}, индекс: {min_index}")
        print(f"Максимальное значение матрицы: {max_value}, индекс: {max_index}")
