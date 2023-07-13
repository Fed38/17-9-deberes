def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    position = len(arr)

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            position = mid
            right = mid - 1
        else:
            left = mid + 1

    return position


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Ввод последовательности чисел и целевого числа
sequence = input("Введите последовательность чисел через пробел: ").split()
target = int(input("Введите целевое число: "))

# Преобразование последовательности в список целых чисел
sequence = [int(num) for num in sequence]

# Сортировка списка
insertion_sort(sequence)

# Поиск позиции для целевого числа
position = binary_search(sequence, target)

# Вывод результата
if position < len(sequence):
    print("Позиция элемента:", position)
    print("Значение элемента:", sequence[position])
else:
    print("Целевое число больше всех элементов в последовательности")
