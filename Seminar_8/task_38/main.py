# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных
FILE_NAME = "Seminar_8\\task_38\\telephone_directory.txt"

def get_line(lineNo):
    file = open(FILE_NAME, "r", encoding="UTF-8")
    for i, line in enumerate(file, 1):
        if i == lineNo:
            return line
    else:
        return 0

def change_contact_attribute(changeLineList):
    dictAttribute = {1: "Имя", 2: "Фамилия", 3: "Отчество", 4: "Телефон", 5: "Комментарий"}
    print("Для изменения реквизитов, напишите новое значение атрибутов ниже.")
    print("Если атрибут остается без изменений, оставьте значение пустым. Для очистки используйте '-'")
    print(changeLineList)
    for i in range(1,len(changeLineList)):
        curentValue = input(f"{dictAttribute[i]} ({changeLineList[i]}): ")
        if len(curentValue) > 0:
            changeLineList[i] = curentValue
    return changeLineList

def change_contact():
    lines = count_lines()
    numCnangeLine = int(input("Введите порядковый номер контакта для изменения: "))
    changeLineOld = get_line(numCnangeLine)
    if changeLineOld == 0:
        print("Такого контакта не существует!")
        return
    changeLineList = list(changeLineOld.split())
    changeLineList = change_contact_attribute(changeLineList)

    fileOld = open(FILE_NAME, "r", encoding="UTF-8")
    fileOldStr = fileOld.read()
    fileOld.close()
    fileOldStr = fileOldStr.replace(changeLineOld," ".join(changeLineList)+"\n")
    
    fileNew = open(FILE_NAME, "w", encoding="UTF-8")
    fileNew.write(fileOldStr)
    fileNew.close()
    print("Был успешно изменен контакт: " + " ".join(changeLineList))

def delete_contact():
    lines = count_lines()
    numDeleteLine = int(input("Введите порядковый номер контакта для удаления: "))
    deleteLine = get_line(numDeleteLine)
    if deleteLine == 0:
        print("Такого контакта не существует!")
        return
    fileOld = open(FILE_NAME, "r", encoding="UTF-8")
    fileOldStr = fileOld.read()
    fileOld.close()
    fileOldStr = fileOldStr.replace("\n" + deleteLine if numDeleteLine == lines else deleteLine,"")

    if numDeleteLine < lines:
        diffRow = lines - numDeleteLine
        for i in range(diffRow):
            fileOldStr = fileOldStr.replace(f"{str(numDeleteLine+i+1)}. ", f"{str(numDeleteLine+i)}. ")

    fileNew = open(FILE_NAME, "w", encoding="UTF-8")
    fileNew.write(fileOldStr)
    fileNew.close()
    print("Был успешно удален контакт: " + deleteLine)

def find_contacts():
    keyword = input("Введите ключевое слово для поиска: ").lower()
    lines = count_lines()
    list_foundContacts = list()
    file = open(FILE_NAME, "r", encoding="UTF-8")
    for _ in range(lines):
        currentLine = file.readline()
        if keyword in currentLine.lower():
            list_foundContacts.append(currentLine)

    if len(list_foundContacts) > 0:
        print("Вот что удалось найти по вашему запросу:")
        for i in list_foundContacts:
            print(i,end="")
    else:
        print("По вашему запросу не удалось что-либо найти...")
    file.close()

def print_all_contact():
    lines = count_lines()
    file = open(FILE_NAME, "r", encoding="UTF-8")
    for _ in range(lines):
        print(file.readline(),end="")
    print()
    file.close()

def create_contact():
    lines = count_lines()
    file = open(FILE_NAME, "a", encoding="UTF-8")
    firstname = input("Введите имя: ") or "-"
    surname = input("Введите фамилию: ") or "-"
    patronymic = input("Введите отчество: ") or "-"
    telephone = input("Введите телефон: ") or "-"
    comment = input("Введите комментарий: ") or "-"

    file.write(f"\n{lines+1}. {firstname} {surname} {patronymic} {telephone} {comment}")
    file.close()

def count_lines():
    file = open(FILE_NAME, "r", encoding="UTF-8")
    lines = len(file.readlines())
    file.close()
    return lines

def show_list_commands():
    print("1. Вывести список команд.")
    print("2. Вывести все контакты.")
    print("3. Создать контакт.")
    print("4. Найти контакт(-ы).")
    print("5. Изменить контакт.")
    print("6. Удалить контакт.")
    print("0. Завершить работу с телефонным справочником.")

print("Список команд для работы с телефонным справочником:")
show_list_commands()

flagStop = False
while flagStop == False:
    command = int(input("\nВведите порядковый номер команды (1 - показать команды): "))
    if command == 1:
        show_list_commands()
    elif command == 2:
        print_all_contact()
    elif command == 3:
        create_contact()
    elif command == 4:
        find_contacts()
    elif command == 5:
        change_contact()
    elif command == 6:
        delete_contact()
    elif command == 0:
        flagStop = True
    else:
        print("\tОШИБКА: По этому номеру команды не найдено!")