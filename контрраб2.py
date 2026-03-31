import random
import time


def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Базовый случай: массив из 0 или 1 элемента уже отсортирован
    pivot = arr[len(arr) // 2]  # Выбираем середину в качестве опорного элемента
    left = [x for x in arr if x < pivot]  # Массив элементов меньше опорного
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # Рекурсивно сортируем левую и правую части, объединяем все вместе
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Базовый случай: массив из 0 или 1 элемента уже отсортирован
    # Делим массив на две части
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    sorted_list = []
    i = j = 0
    # Сравниваем элементы левой и правой части и сливаем их в один массив
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


volume = {"маленький список(100 эл.)": 100, "большой список(3000эл.)": 3000}
sorting = [
    ("Quick Sort", quick_sort),
    ("Merge Sort", merge_sort),
    ("Bubble Sort", bubble_sort),
    ("Insertion Sort", insertion_sort),
    ("Selection Sort", selection_sort)
]
for label, size in volume.items():
    print(f" {label.upper()}")
    data = [random.randint(1, 5000) for _ in range(size)]

    for name, func in sorting:
        test_list = data.copy()

        start = time.perf_counter()
        func(test_list)
        end = time.perf_counter()

        print(f"{name:}: {end - start:.5f}сек.")
print(
    f"Вывод: в маленьких списках разница между сортировками небольшая, но quick sort и merge sort справляются быстрее всех\n"
    f"и с маленькими списками, и с большими списками. В маленьких списках разница между ними может быть около 0.00001 сек,\n"
    f"а в больших - примерно 0.001сек.")
