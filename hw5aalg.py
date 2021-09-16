import collections
import numpy

companies = []
avg_incomes = []
lower_then_avg = []
higher_then_avg = []


while True:
    name = input('Укажите название компании(для подведения итогов введите "q")\n\t: ')
    if name == 'q':
        break
    else:
        companies.append(name)
        first = float(input('Укажите прибыль за 1-ый квартал(тыс. рублей): '))
        second = float(input('Укажите прибыль за 2-ой квартал(тыс. рублей): '))
        third = float(input('Укажите прибыль за 3-ий квартал(тыс. рублей): '))
        fourth = float(input('Укажите прибыль за 4-ый квартал(тыс. рублей) '))
        avg_income = numpy.mean((first + second + third + fourth))
        avg_incomes.append(avg_income)

dict_of_incomes = dict(zip(companies, avg_incomes))
total_avg_for_incomes = numpy.mean(avg_incomes)

for key, value in dict_of_incomes.items():
    if value < total_avg_for_incomes:
        lower_then_avg.append(key)
    else:
        higher_then_avg.append(key)
print(f'Средняя прибыль {total_avg_for_incomes} тысяч рублей\n',
      f'Компании с прибылью выше средней: {higher_then_avg} \n',
      f'Компании с прибылью ниже среденей: {lower_then_avg}')
      

"""    Задача 2     """


a = input('Введите первое число: ')
b = input('Введите второе число: ')

c = hex(int(a, 16) + int(b, 16))
c1 = hex(int(a, 16) * int(b, 16))

c, c1 = list(c[2:].upper()), list(c1[2:].upper())

print(c)
print(c1)

# понимаю, что скорее всего решать эту задачу нужно было с помощью словарей,
# Нооооо я не удержался  ))))

