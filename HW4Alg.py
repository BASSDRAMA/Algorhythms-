import requests
import cProfile
import timeit
import random

"""
Мне стало интересно и в качестве дополнения к домашней работе я измерил 
скорость открытия сайтов с помощью сипрофайлера 
Вот выдержки из итогового ответа 
def facebook():
    requests.get('https://facebook.com')


def google():
    requests.get('https://google.com')


def twitter():
    requests.get('https://twitter.com')


def vk():
    requests.get('https://vk.com')


def main():
    facebook()
    google()
    twitter()
    vk()


cProfile.run('main()')


1                         
0.000
0.000
0.423
0.423
main.py: 13(twitter) 


1
0.000
0.000
0.195
0.195
main.py: 17(vk)


1
0.000
0.000
1.476
1.476
main.py: 21(main)


1
0.000
0.000
0.389
0.389
main.py: 5(facebook)


1
0.000
0.000
0.469
0.469
main.py: 9(google)
"""


def counting(amount):
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


def main():
    counting(1000000)


cProfile.run('main()')


"""          Задача 2          """


def resheto(i):

    # Создаем массив с числами до границы включительно
    nums = []
    for item in range(i + 1):
        nums.append(item)

    # при таком заполнении инедксы чисел равны самим числам, что облегчает задачу
    # все составные числа надо заменить нулями + обернуть результат во множетсво = задача решена
    # 1 сразу меняем на 0, тк это не простое и не составное число
    nums[1] = 0

    # начнем с 2
    number = 2

    while number < i:
        multiple_number = number + number
        while multiple_number <= i:
            nums[multiple_number] = 0
            multiple_number += number
        number += 1

    nums = set(nums)
    nums.remove(0)
    print(nums)

# Я думаю, что сложность алгоритма можно ценить как О(n), тк алкгоритм линейный, мы перебираем числа одни за другими


value = 4000

time1 = timeit.timeit(f'resheto({value})',
                      setup='from __main__ import resheto',
                      number=1)

print(time1)

# для тысячи результат 0.0005, для двух - 0.0010, трех - 0,0016, четырех - 0.0022
# на сколько я понимаю, алгоритм и вправду линейный тк увеличение пропорционально
# на каждую 1000 чисел уходит примерно 0.00055 секунд













