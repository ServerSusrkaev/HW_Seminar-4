# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
import random

n = int(input('Количество элементов 1-го множества: '))
m = int(input('Количество элементов 2-го множества: '))

firstSet = []
firstTemp = []

secondSet = []
secondTemp = []

for i in range(n):
    firstSet.append(random.randint(1, n))

for i in range(m):
    secondSet.append(random.randint(1, m))

for i in firstSet:
    if i not in firstTemp:
        firstTemp.append(i)
firstTemp.sort()

for i in secondSet:
    if i not in secondTemp:
        secondTemp.append(i)
secondTemp.sort()

print(firstSet)
print(firstTemp)


print(secondSet)
print(secondTemp)