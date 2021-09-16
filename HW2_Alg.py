#задание 1


active_flag = True
while active_flag:
    operation_sign = input('(Для выхода введите 0). Укажите знак операции: ')
    if operation_sign == '0':
        print('Bye!')
        active_flag = False

    elif operation_sign in ('+', '-', '*', '/'):
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))

        if operation_sign == '+':
            print(f'{a} + {b} = {a + b}')
        elif operation_sign == '-':
            print(f'{a} - {b} = {a - b}')
        elif operation_sign == '*':
            print(f'{a} * {b} = {a * b}')
        elif operation_sign == '/':
            if b == 0:
                print('На ноль делить нельзя')
            else:
                print(f'{a} / {b} = {a / b}')
    else:
        print('Неверный знак операции')


#Задание 2

a = int(input('Введите число: '))
a_str = str(a)
i = 0
chet = 0
nechet = 0

for item in a_str:
    int_item = int(item)
    if int_item % 2 == 0:
        i += 1
        chet += 1
    else:
        i += 1
        nechet += 1

print(f'В числе {a} {chet} четных чисел и {nechet} нечетных')


#задание 3
a = int(input('Введите число: '))

a_str = str(a)
a_reversed = int(a_str[::-1])
print(a_reversed)


# Задание 4

number_of_n = int(input('Укажите количество элементов: '))
if number_of_n == 0:
    print(0)
elif number_of_n == 1:
    print(1)

x = 1
y = 0
for i in range(number_of_n):
    y += x
    x *= (-0.5)

print(y)


# Задание 5

for i in range(32, 128):
    i_chr = chr(i)
    print(f'{i_chr}', end='')
    if i % 10 == 0:
        print()


# Задание 6
import random

number = random.randrange(1, 101, 1)
a_flag = True
attempts = 10
while a_flag:
    answer = int(input('введите число: '))
    if answer == number:
        print(f'Вы угадали!!! Это число {number}')
        a_flag = False
    else:
        if answer > number:
            attempts -= 1
            print('Неправильно! Загаданное число меньше')
        elif answer < number:
            attempts -= 1
            print('Неправильно! Загаданное число больше')

    if attempts == 0:
        print(f'Вы проиграли! Загаданное число - {number}')
        a_flag = False



# Задание 7 1+2+...+n = n(n+1)/2

n = int(input('Введите число: '))

a = 0
b = n * (n+1)/2
i = 0

for item in range(n):
    i += 1
    a += i

print(f'{a} = {b}')


# Задание 8

posledovatelnost = int(input('Введите последовательность чисел: '))
search_number = int(input('Укажите число, которое нужно посчитать: '))

str_posled = str(posledovatelnost)
str_search_number = str(search_number)
i = 0
for item in str_posled:
    if item == str_search_number:
        i += 1

print(f'Цифра {search_number} встретилась {i} раз')


# Задание 9

list_of_numbers = []
list_of_ssums = []

a_flag = True
while a_flag:
    a = int(input('(нажмите 0, чтобы узнать результат.) Введите число: '))
    if a == 0:
        a_flag = False
        print('Вычисляю...')
    else:
        list_of_numbers.append(a)

i = 0
for item in list_of_numbers:
    ssum = 0
    while item != 0:
        d = item % 10
        ssum += d
        item = item // 10
    list_of_ssums.append(ssum)

max_ssum = max(list_of_ssums)
index_of_need_number = list_of_ssums.index(max_ssum)
serached_number = list_of_numbers[index_of_need_number]


print(f'Искомое число - {serached_number} сумма цифр равна {max_ssum}')















