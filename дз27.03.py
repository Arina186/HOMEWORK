def get_int_input(prompt):
    while True:
        try:
            int_num = int(input(prompt))
            return int_num
        except ValueError:
            print("Введите целое число!")


def filter_text(file_path, levels):
    if isinstance(levels, str):
        levels = [levels]
    target_prefixes = [f"[{lvl.strip().upper()}]" for lvl in levels]
    current_block = []
    is_target_level = False
    with open(file_path, "r") as file:
        for line in file:
            stripped_line = line.strip()

            if stripped_line.startswith("["):
                if is_target_level and current_block:
                    yield current_block

                current_block = []
                is_target_level = False
                for p in target_prefixes:
                    if stripped_line.startswith(p):
                        is_target_level = True
                        break

            if is_target_level and stripped_line:
                current_block.append(stripped_line)
        if is_target_level and current_block:
            yield current_block


def group_repeating(data):
    if not data:
        return
    current_basket = [data[0]]
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            current_basket.append(data[i])
        else:
            yield current_basket
            current_basket = [data[i]]
    yield current_basket


is_continue = True
while is_continue:
    print(" 1 - error\n"
          " 2 - group repeating\n"
          " 3 - exit\n")

    user_choice = get_int_input("Enter action number: ")
    if user_choice == 1:
        level_input = input("Введите уровень или уровни через пробел (например: INFO ERROR): ")
        selected_levels = level_input.replace(",", " ").split()

        if not selected_levels:
            print("Вы ничего не ввели!")
            continue
        filter_generator = filter_text("inform27.03.txt", selected_levels)
        found_anything = False
        for item in filter_generator:
            found_anything = True
            print("\n".join(item))

        if not found_anything:
            print(f"Записей с уровнями {selected_levels} не обнаружено.")

    elif user_choice == 2:
        numbers = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 7, 7]
        for basket in group_repeating(numbers):
            print(f"\n Группировка списка {basket}")

    elif user_choice == 3:
        print("Выход из программы...")
        is_continue = False
    else:
        print("Нет такого пункта меню!")
