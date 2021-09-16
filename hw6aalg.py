import random
import sys

# 2 урок 4 задача
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

""" считаем память """

member1 = sys.getsizeof(number_of_n) + sys.getsizeof(x) + sys.getsizeof(y)
print(f'В программе задействовано {member1} байт памяти')


# 2 урок 6 задача

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

""" считаем память """

member2 = sys.getsizeof(number) + sys.getsizeof(a_flag) + sys.getsizeof(attempts)
print(f'В программе задействовано {member1} байт памяти')


# урок 2 Задание 7
# названия переменных изменены на корявые, чтобы не было конфликта с прердыдущими задачами

n_n = int(input('Введите число: '))

a_a = 0
b_b = n * (n+1)/2
i_i = 0

for item in range(nn):
    i_i += 1
    a_a += i_i

print(f'{a_a} = {b_b}')

""" считаем память """

member3 = sys.getsizeof(n_n) + sys.getsizeof(a_a) + sys.getsizeof(i_i)
print(f'В программе задействовано {member1} байт памяти')