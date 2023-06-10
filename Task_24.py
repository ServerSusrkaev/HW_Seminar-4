# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по 
# окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai 
# ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля 
# и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает 
# ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения максимального числа ягод, которое может 
# собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
import random

bushCount = int(input('Укажите количество кустов на грядке: '))

bush = []
for i in range(bushCount):
    bush.append(random.randint(1, 100))
print(bush)

summa = 0
maxBerry = 0
item = 1
bushNumber = 0

while item < len(bush) - 1:
    summa += bush[item - 1] + bush[item] + bush[item + 1]
    item += 1
    
    if summa > maxBerry:
        maxBerry = summa
        bushNumber = item
    
    print(summa, end=" ")
    summa = 0
    

print(f'При сборе ягод с кустов {bushNumber - 1} ⇐ {bushNumber} ⇒ {bushNumber + 1}, можно собрать максимальное количество ягод равное {maxBerry}')