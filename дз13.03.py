# task 1
import os, platform

print(f"Operational system: {platform.system()} {os.name}")  # имя операционной системы
print(f"Current working directory: {os.getcwd()}")  # путь до текущей папки

current_files = os.listdir()

extensions = set()
for file in current_files:
    if file.count(".") == 1:
        file_parts = file.split(".")
        if file_parts[0] != "" and file_parts[1] != "":
            extensions.add(file_parts[1].lower())

print(extensions)
# сгруппировать файлы в папку
for ext in extensions:
    if ext != "py":
        new_folder_name = f"{ext}s"
        if not os.path.exists(new_folder_name):
            os.mkdir(new_folder_name)
        count = 0  # сколько файлов в папке
        total_size = 0  # для размера в гб
        for file in current_files:
            if file.count(".") == 1:
                file_parts = file.split(".")
                if file_parts[0] != "" and file_parts[1] != "" and file_parts[1] == ext:
                    file_path = os.path.join(os.getcwd(), file)
                    total_size += os.path.getsize(file_path)
                    count += 1
                    replaced_file_path = os.path.join(os.getcwd(), new_folder_name, file)  # file - новое имя файла
                    os.replace(file, replaced_file_path)
        if count > 0:
            size_file = total_size / 1024 ** 3
            print(f"В папке с {ext} файлами перемещено {count} файлов, их суммарный размер - {size_file:.10f} ГБ")
        # .5f где 5-кол-во знаков после запятой f — тип данных fixed-point (число с фиксированной точкой)
        else:
            print(f"Для расширения {ext} файлов не найдено (возможно, уже перемещены)")

target_file = "dhjddj.txt"
new_file = "poetry.txt"

if "." in target_file:
    ext = target_file.split(".")[-1]
    folder_of_file = f"{ext}s"
    old_path = os.path.join(os.getcwd(), folder_of_file, target_file)
    new_path = os.path.join(os.getcwd(), folder_of_file, new_file)
    # Проверяем наличие и переименовываем
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"File {target_file} was renamed to {new_file}")
    else:
        print(f"File {target_file} was not found in {folder_of_file}")

# task 3

input_path = os.path.join("txts", "text.txt")
output_path = os.path.join("txts", "output.txt")
try:
    with open(input_path, "r", encoding="utf-8") as file, open(output_path, "w", encoding="utf-8") as output:
        for line in file:
            word_count = line.lower().split()
            if not word_count:  # Если строка пустая — пропускаем
                continue
            counts = {}
            for word in word_count:
                clean_word = word.strip(".,!?;:-")
                if clean_word in counts:
                    counts[clean_word] += 1  # Если слово уже записано, мы просто увеличиваем число рядом с ним на +1.
                else:
                    counts[
                        clean_word] = 1  # Если слова еще нет, мы записываем его в книжку и ставим цифру 1, так как мы увидели его в первый раз.

            max_word = ""
            max_count = 0
            for word in counts:
                if counts[word] > max_count:
                    max_count = counts[word]
                    max_word = word
            output.write(f"{max_word} {counts[max_word]}\n")

except Exception as e:
    print(f"Error: {e}")

# task 4
input_path = os.path.join("txts", "forbidden_words.txt")
try:
    with open(input_path, "r", encoding="utf-8") as file:
        forbidden_words = file.read().lower().split()
    file_name = input("Enter the filename(another_text.txt): ")
    target = os.path.join("txts", file_name)
    with open(target, "r", encoding="utf-8") as file:
        text = file.read()

    for word in forbidden_words:
        word_len = len(word)
        stars = "*" * word_len
        # ищем где заменить в версии "нижнего регистра",
        # но замену делаем в оригинальном тексте
        index = text.lower().find(word)
        while index != -1:
            # Склеиваем текст: до найденного слова + звезды + после слова
            text = text[:index] + stars + text[index + word_len:]
            index = text.lower().find(word, index + word_len)
    print(f"Result: {text}")
except FileNotFoundError:
    print("File was not found")
except Exception as e:
    print(f"Error: {e}")

# task 5
input_path = os.path.join("txts", "student_grades.txt")
try:
    with open(input_path, "r", encoding="utf-8") as file:
        for line in file:
            data = line.split()
            if len(data) == 3 and data[2] < "3":
                print(f"Student {data[0]} {data[1]} got {data[2]}")
except Exception as e:
    print(f"Error: {e}")

# task 6
input_path = os.path.join("txts", "another_text.txt")
result = 0
current_num = ""
try:
    with (open(input_path, "r", encoding="utf-8") as file):
        text = file.read()
        for char in text:
            if char.isdigit():
                current_num += char
            else:
                if current_num:
                    result += int(current_num)  # Как только попадается НЕ цифра, превращаем накопленную строку в число
                    # и добавляем его в общую сумму
                    current_num = ""  # очищаем буфер, чтобы следующее число не приклеилось к предыдущему
        if current_num:  # Проверка, если файл заканчивается числом
            result += int(current_num)

        print(f"Total sum: {result}")
except Exception as e:
    print(f"Error: {e}")

# task 7
import string


def caesar_encyption(text, shift):
    encrypted_message = ""
    for char in text:
        if char.isalpha():
            is_russian = "а" <= char.lower() <= "я" or char.lower() == 'ё'
            if is_russian:
                alphabet_size = 33
                ru_alphabet = "абвгждеёзийклмнопрстуфхцчшщъыьэюя"
                if char.isupper():
                    ru_alphabet = ru_alphabet.upper()
                indx = ru_alphabet.find(char)
                encrypted_message += ru_alphabet[(indx + shift) % 33]
            else:
                alphabet_size = 26
                start = ord("A") if char.isupper() else ord("a")
                shifted_char = chr((ord(char) - start + shift) % alphabet_size + start)
                encrypted_message += shifted_char
        else:
            encrypted_message += char  # Символы и пробелы оставляем как есть
    return encrypted_message


if not os.path.exists("txts"):
    os.makedirs("txts")

input_path = os.path.join("txts", "for_caesar.txt")
output_path = os.path.join("txts", "final_caesar.txt")
try:
    with (open(input_path, "r", encoding="utf-8") as file):
        lines = file.readlines()
    with (open(output_path, "w", encoding="utf-8")) as file:
        for index, line in enumerate(lines, start=1):
            encrypted_line = caesar_encyption(line, index)  # Шаг шифра равен номеру строки (index)
            file.write(encrypted_line)
    print("Шифрование завершено успешно!")
except FileNotFoundError:
    print(f"Ошибка: Файл {input_path} не найден.")
except Exception as e:
    print(f"Error: {e}")

# task 8
import json
import csv
import os
from datetime import datetime


def get_int_input(prompt):
    while True:
        try:
            int_num = int(input(prompt))
            return int_num
        except ValueError:
            print("Enter only integer numbers!")


def get_letter_input(prompt):
    while True:
        name = input(prompt).strip()
        # Убираем пробелы для проверки
        if name.replace(" ", "").isalpha() and len(name) > 0:
            return name
        else:
            print("Error! Name must contain only letters and cannot be empty")


# from datetime import datetime
def get_birthday_input(prompt):
    while True:
        date_str = input(prompt).strip()
        try:
            # Пытаемся превратить строку в реальную дату по шаблону
            datetime.strptime(date_str, "%d.%m.%Y")
            return date_str
        except ValueError:
            print("Error: Use format: 11.08.2001 and enter a valid date!")


def get_height_input(prompt):
    while True:
        try:
            hei = int(input(prompt))
            if 50 <= hei <= 250:
                return hei
            else:
                print("Height must be between 50cm and 250cm!")
        except ValueError:
            print("Enter only integer numbers!")


def get_weight_input(prompt):
    while True:
        try:
            # Разрешаем вводить и точку, и запятую
            raw_val = input(prompt).replace(',', '.')
            val = float(raw_val)
            if 35.0 <= val <= 200.0:
                return val
            else:
                print("Weight must be between 35kg and 200kg!")
        except ValueError:
            print("Enter only numbers!")


# task 1 преобразование в формат CSV

def json_to_csv(input_path, output_path):
    with open(input_path, "r") as json_file:
        data = json.load(json_file)
    # Проверяем, что данные — это список объектов
    if not isinstance(data, list) or len(data) == 0:
        print("Error: JSON must contain a list of objects.")
        return
    # делаем список языков программирования в строку
    for item in data:
        if "languages" in item and isinstance(item["languages"], list):
            item["languages"] = ", ".join(item["languages"])
            # получаем заголовки
    head = data[0].keys()
    # записываем в cvs
    with open(output_path, "w", encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=head)
        writer.writeheader()
        writer.writerows(data)


# task 2 сохранение данных в CSV-файл

def save_file_csv(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        # Превращаем списки (например, languages) в строки через запятую
        for row in data:
            for k, v in row.items():
                if isinstance(v, list):
                    row[k] = ', '.join(map(str, v))
        with open(output_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


# task 3 добавление информации о новом сотруднике в JSON-файл

def add_new_employee_to_json(input_path):
    if os.path.exists(input_path):
        with open(input_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    print("--- New employee's information ---")
    name = get_letter_input("Enter employee's name and surname: ")
    birthday = get_birthday_input("Enter employee's birthday(for example: 11.08.2001): ")
    height = get_height_input("Enter employee's height(cm): ")
    weight = get_weight_input("Enter employee's weight(kg): ")
    car = get_letter_input("Does employee have a car? y/n: ")
    have_car = True if car == "y" else False
    languages = input("Enter employee's languages with commas: ")
    languages = languages.split(",")
    new_employee = {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": have_car,
        "languages": languages
    }
    data.append(new_employee)
    with open(input_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Employee {name} is successfully added to the file!")


# ensure_ascii=False отвечает за то, как в JSON-файле будут выглядеть русские буквы,
# записывает символы как есть

# task 4 добавление информации о новом сотруднике в CSV-файл

def add_new_employee_to_csv(input_path):
    print("--- New employee's information ---")
    name = get_letter_input("Enter employee's name and surname: ")
    birthday = get_birthday_input("Enter employee's birthday(for example: 11.08.2001): ")
    height = get_height_input("Enter employee's height(cm): ")
    weight = get_weight_input("Enter employee's weight(kg): ")
    car = get_letter_input("Does employee have a car? y/n: ")
    have_car = True if car == "y" else False
    languages = input("Enter employee's languages with commas: ")
    new_employee_row = [name, birthday, height, weight, have_car, languages]
    try:
        with open(input_path, "a", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(new_employee_row)
        print(f"Employee {name} is successfully added to the file!")
    except IOError as e:
        print(f"Error: could not write to file. {e}")


# 5 - вывод информации о сотруднике по имени json

def find_employee_in_json(input_path):
    search_name = input("Enter the name and surname of the employee to search for: ").strip().lower()

    if os.path.exists(input_path):
        try:
            with open(input_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                # Проверка, что в файле список
                if not isinstance(data, list):
                    print("Ошибка: Формат JSON должен быть списком объектов.")
                    return
                found_employee = None
                for employee in data:
                    # Используем .get(), чтобы код не "падал", если поля 'name' нет
                    if employee.get('name', '').lower() == search_name:
                        name_in_file = str(employee.get('name', '')).strip().lower()
                        if name_in_file == search_name:
                            found_employee = employee
                            break

                if found_employee:
                    print("Employee found:")
                    print(f"Name: {found_employee.get('name')}")
                    print(f"Birthday: {found_employee.get('birthday')}")
                    print(f"Height: {found_employee.get('height')} cm")
                    print(f"Weight: {found_employee.get('weight')} kg")
                    print(f"Has a car: {'Yes' if found_employee.get('car') else 'No'}")
                    langs = found_employee.get('languages', [])
                    print(f"Languages: {', '.join(langs) if langs else 'None'}")

                else:
                    print(f"Employee with name '{search_name}' was not found.")

        except json.JSONDecodeError:
            print("Error: The JSON file is corrupted or empty.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Error: The file does not exist.")


# task 6 - вывод информации о сотруднике по имени csv

def find_employee_in_csv(input_path):
    search_name = input("Enter the name and surname of the employee to search for: ").strip().lower()
    found = False
    try:
        with open(input_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            head = next(reader, None)
            for row in reader:
                if row and row[0].lower() == search_name:
                    print("Employee found:")
                    print(f"Name: {row[0]}")
                    print(f"Birthday: {row[1]}")
                    print(f"Height: {row[2]} cm")
                    print(f"Weight: {row[3]} kg")
                    print(f"Has a car: {row[4]}")
                    print(f"Languages: {row[5]}")
                    found = True
                    break

        if not found:
            print(f"Employee with name '{search_name}' was not found.")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# task 7 - фильтр по языку json

def filter_employees_language_json(input_path):
    search_lang = input("Enter the programming language to filter by: ").strip().lower()
    found = False

    if os.path.exists(input_path):
        try:
            with open(input_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            for employee in data:
                # Проверяем, есть ли поле languages и не пустое ли оно
                if "languages" in employee and isinstance(employee['languages'], list):
                    lower_lang = [lang.strip().lower() for lang in employee['languages']]
                    if search_lang in lower_lang:
                        print(f"  {employee['name']} (Birthday: {employee['birthday']})")
                        found = True
                # не ставим break, потому что нужно найти всех подходящих сотрудников,
                # а не только первого встречного

            if not found:
                print(f"Employee with language '{search_lang}' was not found.")

        except json.JSONDecodeError:
            print("Error: The JSON file is corrupted or empty.")
    else:
        print("Error: The file does not exist.")


# task 8 - фильтр по языку csv

def filter_employees_language_csv(input_path):
    search_lang = input("Enter the programming language to filter by: ").strip().lower()
    found = False
    try:
        with open(input_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            head = next(reader, None)
            for row in reader:
                # languages индекс столбца 5, а сам столбец 6 по счету
                if len(row) > 5:
                    lower_lang = [lang.strip().lower() for lang in row[5].split(",")]
                    if search_lang in lower_lang:
                        print(f"  {row[0]} (Birthday: {row[1]})")
                        found = True

            if not found:
                print(f"Employee with language '{search_lang}' was not found.")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# task 9 - фильтр по году json

def filter_year_json(input_path):
    try:
        search_year = int(input("Enter the year to filter by: ").strip())
    except ValueError:
        return print("Error: The year must be an integer.")

    if os.path.exists(input_path):
        try:
            with open(input_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            heights = []
            for employee in data:
                birthday_year = int(employee["birthday"].split(".")[-1])
                if birthday_year < search_year:
                    heights.append(employee["height"])
                    print(f"{employee['name']}, {employee['birthday']} matches the filter")
            if heights:
                average_height = sum(heights) / len(heights)
                print(f"Average height among suitable employees: {average_height} ")
            else:
                print("There is no employees born before the search year")

        except (json.JSONDecodeError, ValueError, KeyError) as e:
            print("Error: {e}")
    else:
        print("Error: The file does not exist.")


# task 10 - фильтр по году csv

def filter_year_csv(input_path):
    try:
        search_year = int(input("Enter the year to filter by: ").strip())
    except ValueError:
        return print("Error: The year must be an integer.")

    if os.path.exists(input_path):
        try:
            with open(input_path, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                head = next(reader, None)
                heights = []
                for row in reader:
                    # Проверяем, что в строке достаточно данных (Name, Birthday, Height)
                    if len(row) >= 3:
                        try:
                            birthday_year = int(row[1].split(".")[-1])
                            height = int(row[2])
                            if birthday_year < search_year:
                                heights.append(height)
                                print(f"{row[0]}, {row[1]} matches the filter")
                        except (ValueError, IndexError):
                            continue
                if heights:
                    average_height = sum(heights) / len(heights)
                    print(f"Average height among suitable employees: {average_height} ")
                else:
                    print("There is no employees born before the search year")

        except Exception as e:
            print("Error: {e}")
    else:
        print("Error: The file does not exist.")


is_continue = True
while is_continue:
    print(" 1 - преобразование в формат CSV\n"
          " 2 - сохранение данных в CSV-файл\n"
          " 3 - добавление информации о новом сотруднике в JSON-файл\n"
          " 4 - добавление информации о новом сотруднике в CSV-файл\n"
          " 5 - вывод информации о сотруднике по имени json\n"
          " 6 - вывод информации о сотруднике по имени csv\n"
          " 7 - фильтр по языку json\n"
          " 8 - фильтр по языку csv\n"
          " 9 - фильтр по году json\n"
          " 10 - фильтр по году csv\n"
          " 11 - exit\n")

    user_choice = get_int_input("Enter action number: ")

    if user_choice == 1:
        input_path = os.path.join("jsons", "employees.json")
        output_path = "employees.csv"
        json_to_csv(input_path, "employees.csv")

    elif user_choice == 2:
        input_path = os.path.join("jsons", "employees.json")
        output_path = os.path.join("csvs", "employees.csv")
        save_file_csv(input_path, "employees.csv")

    elif user_choice == 3:
        input_path = os.path.join("jsons", "employees.json")
        add_new_employee_to_json(input_path)

    elif user_choice == 4:
        input_path = os.path.join("csv_data", "employees.csv")
        add_new_employee_to_csv(input_path)

    elif user_choice == 5:
        input_path = os.path.join("jsons", "employees.json")
        find_employee_in_json(input_path)

    elif user_choice == 6:
        input_path = os.path.join("csvs", "employees.csv")
        find_employee_in_csv(input_path)

    elif user_choice == 7:
        input_path = os.path.join("jsons", "employees.json")
        filter_employees_language_json(input_path)

    elif user_choice == 8:
        input_path = os.path.join("csvs", "employees.csv")
        filter_employees_language_csv(input_path)

    elif user_choice == 9:
        input_path = os.path.join("jsons", "employees.json")
        filter_year_json(input_path)

    elif user_choice == 10:
        input_path = os.path.join("csvs", "employees.csv")
        filter_year_csv(input_path)

    elif user_choice == 11:
        print("До свидания!")
        is_continue = False
