#Задание 1

answer = {}
for n in range(2, 10):
    answer[n] = []
    for f in range(2, 100):
        if f % n == 0:
            answer[n].append(f)

    print(f'Для числа {n} кратны - {len(answer[n])}. Кратные числа: {answer[n]}.')
        

#Задание 2
numbers_list = list(range(2, 100))
divisors_list = list(range(2, 10))

for item in divisors_list:
    counter = 0
    needed_list = []
    for num in numbers_list:
        if num % item == 0:
            counter += 1
            needed_list.append(num)
    print(f'Числа, кратные {item} : {needed_list}')


import random
amount = int(input('Введите количество элемнтов массива: '))
nums = []
indexes_array = []
while amount:
    nums.append(random.randint(0, 1000))
    amount -= 1

for item in nums:
    if item % 2 == 0:
        indexes_array.append(nums.index(item))

print(nums)
print(indexes_array)



#Задача 3

import random
amount = int(input('Введите количество элемнтов массива: '))
nums = []
while amount:
    nums.append(random.randint(0, 1000))
    amount -= 1

max_n_index = nums.index(max(nums))
min_n_index = nums.index(min(nums))
min_n = nums[min_n_index]
max_n = nums[max_n_index]
print(nums)

nums[min_n_index] = max_n
nums[max_n_index] = min_n

print(nums)


# Задача 4
#Определить, какое число в массиве встречается чаще всего.

import random
amount = int(input('Введите количество элемнтов массива: '))
nums = []
while amount:
    nums.append(random.randint(0, 15))
    amount -= 1

max_index = 0
for item in nums:
    if nums.count(max_index) < nums.count(item):
        max_index = nums.index(item)

print(f'Число {nums[max_index]} встречается {nums.count(max_index)} раз')



# Задача 5
import random
amount = int(input('Введите количество элемнтов массива: '))
nums = []
while amount:
    nums.append(random.randint(-100, 15))
    amount -= 1

nums.append(0)
nums_sorted = sorted(nums)
asked_num = nums_sorted[nums_sorted.index(0) - 1]
nums.remove(0)
print(nums)
print(f'{asked_num} - максимальное отрицательное число')



# Задача 6

import random
amount = int(input('Введите количество элемнтов массива: '))
# Создание массива указанного размера
nums = []
while amount:
    nums.append(random.randint(0, 1001))
    amount -= 1
print(nums)

# Вычисление индексов максимального и минимального значений
max_n_index = nums.index(max(nums))
min_n_index = nums.index(min(nums))
print(nums[min_n_index], nums[max_n_index])

sum_between_max_and_min = 0 # переменная, в которой будут суммироваться подходящие элементы

for item in nums:
    item_index = nums.index(item)
    # для случае, где максимальное значение в массиве стоит после минимального
    if max_n_index > min_n_index:
        if min_n_index < item_index < max_n_index:
            sum_between_max_and_min += nums[item_index]
    # если наоборот, минимальное после максимального
    else:
        if max_n_index < item_index < max_n_index:
            sum_between_max_and_min += nums[item_index]
print(sum_between_max_and_min)


# Задача 7

import random
amount = int(input('Введите количество элемнтов массива: '))
# Создание массива указанного размера
nums = []
while amount:
    nums.append(random.randint(0, 1001))
    amount -= 1
print(nums)

# Создание массива, в котором будут храниться минимальные числа
nums_with_minimals = []

# Определяем первое минимальное число, кладем его в массив с ответом и выкидываем из основного
min1 = nums[nums.index(min(nums))]
nums_with_minimals.append(min1)
nums.remove(nums[nums.index(min(nums))])

# Определяем второе минимальное число
min2 = nums[nums.index(min(nums))]
nums_with_minimals.append(min2)

print(nums_with_minimals)


# Задача 8

import numpy as np


# Функция для заполнения одномерных массивов
def creating_arrays(array, amount):
    inside_amount = amount
    sum_of_nums = 0
    while inside_amount > 0:
        enter = int(input('Введите число: '))
        array.append(enter)
        sum_of_nums += enter
        inside_amount -= 1
    if inside_amount == 0:
        array.append(sum_of_nums)


# Создание и заполнение
a1, a2, a3, a4 = [], [], [], []
creating_arrays(a1, 4)
creating_arrays(a2, 4)
creating_arrays(a3, 4)
creating_arrays(a4, 4)

# Вывод в соответствии условиям
output = np.vstack((a1, a2, a3, a4))
print(output)


# Задача 9

import numpy as np
a1, a2, a3, a4 = [1, 2, 4, 5], [2, 4, 5, 6], [7, 8, 9, 1], [2, 3, 4, 5]
b = np.vstack((a1, a2, a3, a4))
print(b)

list_of_minimals = []
list_of_minimals.append((min(b[:, 0])))
list_of_minimals.append((min(b[:, 1])))
list_of_minimals.append((min(b[:, 2])))
list_of_minimals.append((min(b[:, 3])))
print(max(list_of_minimals))








