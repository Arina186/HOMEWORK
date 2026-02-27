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
    if user_choice == 1:
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

    elif user_choice == 2:
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

    elif user_choice == 3:
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

        #  сумма всех элементов и #какую долю(процент) в общей сумме составляет сумма элементов кажд столбцакакую долю(процент) в общей сумме составляет сумма элементов кажд столбца
        def sum_and_proportion_matrix(matrix):
            summa = 0
            rows = len(matrix)
            columns = len(matrix[0])
            for row in matrix:
                for item in row:
                    summa += item

            share = []
            for j in range(columns):
                column_sum = 0
                for i in range(rows):
                    column_sum += matrix[i][j]
                share.append((column_sum/summa)*100)
                #через равно на каждой итерации цикла старое значение будет стираться

            return summa, share


        rows_number = get_int_input("Enter rows number: ")
        columns_number = get_int_input("Enter columns number: ")
        result = generate_random_matrix(rows_number, columns_number)
        print(f" \nВаша матрица:")
        show_matrix(result)
        summ, share = sum_and_proportion_matrix(result)
        print(f"Сумма элементов матрицы: {summ}, доля: {share}")

    elif user_choice == 4:
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


        def multiplication_col_k(matrix, special_column):
            rows = len(matrix)
            columns = len(matrix[0])

            for i in range(rows):
                multiplier = matrix[i][special_column-1]
                for j in range(columns):
                    matrix[i][j] *= multiplier

            return matrix


        rows_number = get_int_input("Enter rows number: ")
        columns_number = get_int_input("Enter columns number: ")
        special_column = get_int_input("Enter any of the columns: ")
        result = generate_random_matrix(rows_number, columns_number)
        print(f" \nВаша матрица:")
        show_matrix(result)
        multip = multiplication_col_k(result,special_column)
        print("Результат перемножения k столбца на все столбцы: ")
        show_matrix(multip)

    elif user_choice == 5:
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


        def addition_row_l(matrix, special_row):
            rows = len(matrix)
            columns = len(matrix[0])
            target_row = matrix[special_row-1]

            new_matrix = []
            for i in range(rows):
                new_row = []
                for j in range(columns):
                    new_row.append(matrix[i][j] + target_row[j])
                new_matrix.append(new_row)

            return new_matrix


        rows_number = get_int_input("Enter rows number: ")
        columns_number = get_int_input("Enter columns number: ")
        special_row = get_int_input("Enter any of the rows: ")
        result = generate_random_matrix(rows_number, columns_number)
        print(f" \nВаша матрица:")
        show_matrix(result)
        new_matrix = addition_row_l(result, special_row)
        print("Результат сложения L строки с каждой строкой: ")
        show_matrix(new_matrix)
