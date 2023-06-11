import random

# Создаем список случайных чисел
numbers = [random.randint(-100, 100) for _ in range(10)]

# Инициализируем переменные для сумм и произведений
negative_sum = 0
even_sum = 0
odd_sum = 0
multiple_3_product = 1
min_index = max_index = 0
min_value = max_value = numbers[0]
between_positive_sum = 0
first_positive_index = last_positive_index = None

# Вычисляем суммы и произведения
for i, num in enumerate(numbers):
    if num < 0:
        negative_sum += num
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
    if i % 3 == 0:
        multiple_3_product *= num
    if num < min_value:
        min_value = num
        min_index = i
    if num > max_value:
        max_value = num
        max_index = i
    if num > 0:
        if first_positive_index is None:
            first_positive_index = i
        else:
            last_positive_index = i

if first_positive_index is not None and last_positive_index is not None:
    between_positive_sum = sum(numbers[first_positive_index+1:last_positive_index])

# Выводим результаты
print("Список чисел:", numbers)
print("Сумма отрицательных чисел:", negative_sum)
print("Сумма четных чисел:", even_sum)
print("Сумма нечетных чисел:", odd_sum)
print("Произведение элементов с индексами кратными 3:", multiple_3_product)
print("Произведение элементов между минимальным и максимальным элементом:",
      min(numbers[min_index:max_index+1]) if min_index <= max_index else 0)
print("Сумма элементов, находящихся между первым и последним положительными элементами:",
      between_positive_sum if between_positive_sum else 0)
# Задание 2
import random

# Создание случайного списка целых чисел
numbers = [random.randint(-100, 100) for _ in range(10)]
print("Исходный список:", numbers)

# Создание списка четных чисел
even_numbers = [num for num in numbers if num % 2 == 0]
print("Список четных чисел:", even_numbers)

# Создание списка нечетных чисел
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Список нечетных чисел:", odd_numbers)

# Создание списка отрицательных чисел
negative_numbers = [num for num in numbers if num < 0]
print("Список отрицательных чисел:", negative_numbers)

# Создание списка положительных чисел
positive_numbers = [num for num in numbers if num > 0]
print("Список положительных чисел:", positive_numbers)

