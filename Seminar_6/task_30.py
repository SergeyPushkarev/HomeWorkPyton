#Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.

def FillProgression(a1, d ,n):
    print(f"a1 = {a1}")
    listProgression = [a1]
    for i in range(2,n+1):
        an = a1 + (i-1) * d
        listProgression.append(an)
        print(f"a{i} = {an}")
    return listProgression

def PrintProgression(listProgression):
    for i in range(len(listProgression)):
        print(f"a{i+1} = {listProgression[i]}")


a1 = int(input("Введите первый элемент: "))
d = int(input("Введите шаг: "))
n = int(input("Введите количество элементов: "))

listProgression = FillProgression(a1, d, n)
#print()
#PrintProgression(listProgression)