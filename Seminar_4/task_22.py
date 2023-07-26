# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
from random import randint

lengthList1 = int(input("Введите длину первого списка чисел: "))
lengthList2 = int(input("Введите длину второго списка чисел: "))
list1 = list()
list2 = list()

maxLen = max(lengthList1, lengthList2)
for i in range(maxLen):
    if lengthList1 > i:
        list1.append(randint(0,10))
    if lengthList2 > i:
        list2.append(randint(0,10))

set1 = set(list1)
set2 = set(list2)
setIntersection = set1.intersection(set2)
sortedListIntersection = list(setIntersection) # списки с числами сортируются по возрастанию

print(f"Сгенерирован первый список чисел: \n{list1}")
print(f"Сгенерирован Второй список чисел: \n{list2}")
print(f"Пересечение чисел двух списков без повторений: \n{sortedListIntersection}")