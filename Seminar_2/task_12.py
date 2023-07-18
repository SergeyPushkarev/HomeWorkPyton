# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

import math

from random import randint
number1 = randint(0,1000)
number2 = randint(0,1000)

print(f"        [Загаданы числа: первое число {number1}; второе число {number2}]")
sum = number1 + number2
print(f"Сумма этих чисел: {sum}")
proizv = number1 * number2
print(f"Произведение этих чисел: {proizv}")
print()

print("Вычислим через дискриминант:")
d = sum*sum-4*proizv
sd = int(math.sqrt(d))
number1d = (sum + sd)//2
number2d = sum - number1

print(f"Первое число: {number1d}")
print(f"Второе число: {number2d}")
print()

print("Вычислим через цикл:")
for i in range(sum):
    for j in range(sum):
        if i * j == proizv and i + j == sum:
            number1c = i
            number2c = j
            i = sum
            j = sum

print(f"Первое число: {number1c}")
print(f"Второе число: {number2c}")