def read_txt(filename):
    phone_book = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, "r", encoding="utf-8") as phb:
        for line in phb:
            if line != "\n":
                line = line.replace("\n", "")
                record = dict(
                    zip(fields, line.split(","))
                )  # dict(( (фамилия,Иванов),(имя, Точка),(номер,8928) ))
                phone_book.append(record)
    return phone_book


def write_txt(filename, phone_book):
    with open(filename, "w", encoding="utf-8") as phout:
        for i in range(len(phone_book)):
            s = ""
            for v in phone_book[i].values():
                s = s + v + ","
            phout.write(f"{s[:-1]}\n")


def print_result(phone_book):
    count = 0
    for user in phone_book:
        count += 1
        print(
            f"{count}. {user["Фамилия"].title()} {user["Имя"].title()}, телефон: {user["Телефон"]}. {user["Описание"].title()}"
        )


def find_by_lastname(filename, last_name):
    with open(filename, "r", encoding="utf-8") as phb:
        for line in phb:
            print(line)


def work_with_phonebook():
    choice = show_menu()  # Выводим меню на экран
    phone_book = read_txt(
        "phon.txt"
    )  # Формируем список из строк в телефонном справочнике
    while choice != 8:
        if choice == 1:
            print_result(phone_book)
    #     elif choice == 2:
    #         last_name = input("lastname: ")
    #         print(find_by_lastname(phone_book, last_name))
    #     elif choice == 3:
    #         number = input("number: ")
    #         print(find_by_number(phone_book, number))
    #     elif choice == 4:
    #         user_data = input("new user: ")
    #         add_user(phone_book, user_data)
    #         write_txt("phonebook.txt", phone_book)
    #     elif choice == 5:
    #         lastname = input("lastname: ")
    #         print(delete_by_lastname(phone_book, lastname))
    #     elif choice == 6:
    #         last_name = input("lastname: ")
    #         new_number = input("new  number: ")
    #         print(change_number(phone_book, last_name, new_number))
        choice = show_menu()


def show_menu():
    print(
        "\nВыберите необходимое действие:\n"
        "1. Отобразить весь справочник\n"
        "2. Найти абонента по фамилии\n"
        "3. Найти абонента по номеру телефона\n"
        "4. Добавить абонента в справочник\n"
        "5. Удалить абонента из справочника\n"
        "6. Изменить номер абонента из справочника\n"
        "7. Сохранить справочник в текстовом формате\n"
        "8. Закончить работу"
    )
    choice = int(input())
    return choice


work_with_phonebook()
# tkinter визуализации (import tkinter)
