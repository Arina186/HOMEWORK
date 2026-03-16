# task 1
import os, platform

print(f"Operational system: {platform.system()} {os.name}") #имя операционной системы
print(f"Current working directory: {os.getcwd()}") #путь до текущей папки

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
        count = 0 # сколько файлов в папке
        total_size = 0 # для размера в гб
        for file in current_files:
            if file.count(".") == 1:
                file_parts = file.split(".")
                if file_parts[0] != "" and file_parts[1] != "" and file_parts[1] == ext:
                    file_path = os.path.join(os.getcwd(), file)
                    total_size += os.path.getsize(file_path)
                    count += 1
                    replaced_file_path = os.path.join(os.getcwd(), new_folder_name, file) #file - новое имя файла
                    os.replace(file,replaced_file_path)
        if count > 0:
           size_file = total_size/1024**3
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
    #Проверяем наличие и переименовываем
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"File {target_file} was renamed to {new_file}")
    else:
        print(f"File {target_file} was not found in {folder_of_file}")

#task 2



