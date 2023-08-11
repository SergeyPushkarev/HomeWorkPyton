listPhrases = input("Введите стихотворение Винни-Пуха: ").split()
answer = "Парам пам-пам"
vowel = listPhrases[0].count("а")

for i in range(1,len(listPhrases)):
    if vowel != listPhrases[i].count("а"):
        answer = "Пам парам"
        i = len(listPhrases)

print(answer)