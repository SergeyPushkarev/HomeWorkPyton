#Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

def PrintNeedElements(listNumber, min, maxRange):
    print("[", end="")
    for i in range(len(listNumber)):
        if min < listNumber[i] < maxRange:
            print(f"({listNumber[i]}"+":"+str(i)+")", end=", " if i+1 != len(listNumber) else "")
        else:
            print(f"{listNumber[i]}", end=", " if i+1 != len(listNumber) else "")
    print("]")

minRange = int(input("Введите минимум: "))
maxRange = int(input("Введите максимум: "))

listNumber = [random.randint(0,100) for _ in range(15)]
print("\nНиже список чисел. Попадающие в диапазон выделены скобками с указанием индекса.")
PrintNeedElements(listNumber, minRange, maxRange)