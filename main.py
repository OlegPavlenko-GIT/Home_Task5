# Задание №1. Задание 1
# В списке целых, заполненном случайными числами вычислить:
# Сумму отрицательных чисел;
# Сумму четных чисел;
# Сумму нечетных чисел;
# Произведение элементов с индексами кратными 3;
# Произведение элементов между минимальным и максимальным элементом;
# Сумму элементов, находящихся между первым и последним положительными элементами.
# Выполнение:
#
# Let's create a list of random numbers
import random
numbers = [random.randint(-100, 100) for _ in range(10)]
#
# Initialize variables for sums and products
negative_sum = 0
even_sum = 0
odd_sum = 0
multiple_3_product = 1
min_index = max_index = 0
min_value = max_value = numbers[0]
between_positive_sum = 0
first_positive_index = last_positive_index = None

# Calculate sums and products
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

# Get results
print("List of numbers:", numbers)
print("Sum of negative numbers:", negative_sum)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
print("The product of elements with multiple indices 3:", multiple_3_product)
print("Product of elements between minimum and maximum element:",
      min(numbers[min_index:max_index+1]) if min_index <= max_index else 0)
print("Sum of elements between the first and last positive elements:",
      between_positive_sum if between_positive_sum else 0)
#
# Задание #2
# Есть список целых, заполненный случайными числами. На основании данных этого массива нужно:
# Создать список целых, содержащий только четные числа из первого списка;
# Создать список целых, содержащий только нечетные числа из первого списка;
# Создать список целых, содержащий только отрицательные числа из первого списка;
# Создать список целых, содержащий только положительные числа из первого списка.
# Выполнение:
#
import random

# Let's create a list of integers
numbers = [random.randint(-100, 100) for _ in range(10)]
print("Initial list:", numbers)

# Let's create a list of even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print("List of even numbers:", even_numbers)

# Let's create a list of odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]
print("List of odd numbers:", odd_numbers)

# Let's create a list of negative numbers
negative_numbers = [num for num in numbers if num < 0]
print("List of negative numbers:", negative_numbers)

# Let's create a list of positive numbers
positive_numbers = [num for num in numbers if num > 0]
print("List of positive numbers:", positive_numbers)

