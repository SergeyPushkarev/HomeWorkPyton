# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных
FILE_NAME = "Seminar_8\\task_38\\telephone_directory.txt"

def count_lines(): # считает сколько всего строк в файле
    file = open(FILE_NAME, "r", encoding="UTF-8")
    lines = len(file.readlines())
    file.close()
    return lines

def get_line(lineNo): # возвращает строку по номеру строки
    file = open(FILE_NAME, "r", encoding="UTF-8")
    for i, line in enumerate(file, 1):
        if i == lineNo:
            return line
    else:
        return 0

def change_contact_attribute(changeLineList): # здесь меняем атрибуты контакта в передаваемом списке
    dictAttribute = {1: "Имя", 2: "Фамилия", 3: "Отчество", 4: "Телефон", 5: "Комментарий"}
    print("Для изменения реквизитов, напишите новое значение атрибутов ниже.")
    print("Если атрибут остается без изменений, оставьте значение пустым. Для очистки используйте '-'")
    for i in range(1,len(changeLineList)):
        curentValue = input(f"{dictAttribute[i]} ({changeLineList[i]}): ")
        if len(curentValue) > 0:
            changeLineList[i] = curentValue
    return changeLineList

def change_contact(): # меняем атрибуты контакта в этой функции
    lines = count_lines()
    numCnangeLine = int(input("Введите порядковый номер контакта для изменения: "))
    changeLineOld = get_line(numCnangeLine)
    if changeLineOld == 0:
        print("Такого контакта не существует!")
        return
    changeLineList = list(changeLineOld.split()) # преобразуем в список строку нужного контакта
    changeLineList = change_contact_attribute(changeLineList) # изменим нужные атрибуты этого контакта

    fileOld = open(FILE_NAME, "r", encoding="UTF-8")
    fileOldStr = fileOld.read()
    fileOld.close()
    fileOldStr = fileOldStr.replace(changeLineOld," ".join(changeLineList) if numCnangeLine == lines else " ".join(changeLineList)+"\n") # изменим нашу строку во всем файле
    
    fileNew = open(FILE_NAME, "w", encoding="UTF-8")
    fileNew.write(fileOldStr) # перезаписываем файл с изменениями
    fileNew.close()
    print("Был успешно изменен контакт: " + " ".join(changeLineList))

def delete_contact(): # удаляем контакт в этой функции
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
        diffRow = lines - numDeleteLine # посчитаем сколько строк нужно поправить
        for i in range(diffRow): # поправим порядковые номера в файле из-за сдвига
            fileOldStr = fileOldStr.replace(f"{str(numDeleteLine+i+1)}. ", f"{str(numDeleteLine+i)}. ") # изменим текущий номер на -1

    fileNew = open(FILE_NAME, "w", encoding="UTF-8")
    fileNew.write(fileOldStr)
    fileNew.close()
    print("Был успешно удален контакт: " + deleteLine)

def find_contacts(): # ищем контакт(-ы) в этой фукнции
    keyword = input("Введите ключевое слово для поиска: ").lower()
    lines = count_lines()
    list_foundContacts = list()
    file = open(FILE_NAME, "r", encoding="UTF-8")
    for _ in range(lines):
        currentLine = file.readline()
        if keyword in currentLine.lower(): # здесь ищем ключевое слово во всей строке
            list_foundContacts.append(currentLine) # добавляем в доп. список найденные контакты

    if len(list_foundContacts) > 0:
        print("Вот что удалось найти по вашему запросу:")
        for i in list_foundContacts:
            print(i,end="")
    else:
        print("По вашему запросу не удалось что-либо найти...")
    file.close()

def print_all_contact(): # выводим все контакты в этой функции
    lines = count_lines()
    file = open(FILE_NAME, "r", encoding="UTF-8")
    for _ in range(lines):
        print(file.readline(),end="")
    print()
    file.close()

def create_contact(): # создаем контакт в этой функции
    lines = count_lines()
    file = open(FILE_NAME, "a", encoding="UTF-8")
    firstname = input("Введите имя: ") or "-" # по умолчанию заполняем "-", если ничего не указали, чтобы не нарушить целостность списка по количеству элементов в строке
    surname = input("Введите фамилию: ") or "-"
    patronymic = input("Введите отчество: ") or "-"
    telephone = input("Введите телефон: ") or "-"
    comment = input("Введите комментарий: ") or "-"

    file.write(f"\n{lines+1}. {firstname} {surname} {patronymic} {telephone} {comment}")
    file.close()

def show_list_commands(): # показываем список команд в этой функции
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