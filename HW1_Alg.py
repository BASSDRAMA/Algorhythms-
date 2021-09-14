
# Задание 1

number = int(input('Enter number: '))

last = number % 10
first = number // 100
middle = (number // 10) % 10

print(f' sum = ',  last + first + middle, ',\n'
      'product of numbers = ', last * middle * first)


# Задание 2

a = 5
b = 6
z = a & b
y = a | b
x = a ^ b

a1 = a << 2
a2 = a >>2

print(f'a&b =', z)
print(f'a|b =', y)
print(f'a^b =', x)
print(f'a<<2 =', a1)
print(f'a>>2 =', a2)



# Задание 3
print('y = kx + b')
print('Введите координаты первой точки: ')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))

print('Введите координаты второй точки: ')
x2 = float(input('x2 = '))
y2 = адщфе(input('y2 = '))

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

print(f'y = {k}x + {b}')

# Задание 4

#random.randrange(start, stop, step) - возвращает случайно выбранное число из последовательност
import random

x1 = int(input('Укажите начало границы: '))
x2 = int(input('Укажите конец границы: '))
a = random.randrange(x1, x2, 1)
print(a)

y1 = float(input('Укажите начало границы: '))
y2 = float(input('Укажите конец границы: '))
b = random.uniform(y1, y2)
print(round(b, 3))

z1 = ord(input('Укажите начало границы(буква): '))
z2 = ord(input('Укажите конец границы(буква): '))
c = random.randrange(z1, z2, 1)
print(chr(c))



#Задание 5-6 для английского алфавита

x = ord(input('Введите первую букву: '))
y = ord(input('Введите вторую букву: '))
z = int(input('Введите номер буквы: '))
x = x - ord('a') + 1
y = y - ord('a') + 1
xy1 = abs(x - y) - 1
z = ord('a') + z - 1

print(f'Позиции букв:', x, y, 'между буквами:', xy1, '\nВаша буква:', chr(z))


#Задание 7


a = int(input('Введите длину первой стороны: '))
b = int(input('Введите длину второй стороны: '))
c = int(input('Введите длину третьей стороны: '))

if a + b <= c or a + c <= b or c + b <= a:
    print('Такой треугольник не может существовать')
elif a != b and a != c and b != c:
    print('Этот треугольник разносторонний')
elif a == b == c:
    print('Этот Треугольник равносторонний')
else:
    print('Этот треугольник равнобедренный')


y = int(input('Укажите год: '))
if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
    print('Год обычный')
else:
    print('Год високосный')


#Задание 9

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = int(input('Введите третье число: '))

if x > y > z or z > y > x:
    print(f'{y} - среднее число')
elif y > x > z or z > x > y:
    print(f'{x} - среднее число')
elif x == z or x == y or z == y:
    print('невозможно определдить среднее число')
else:
    print(f'{z} - среднее число')















































