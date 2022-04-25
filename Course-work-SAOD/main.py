from typing import Callable, Iterator, Union, Optional

import interface as gui
import check_funcs as check
import hash_table_of_visitors as ht
import Visitor as vs

from os import system


def new_visitor(visitor_base) -> None:
    gui.AddNewVisitor.name_menu()
    tmp = vs.Visitor()

    tmp.passport = check.field_passport(input("Введите номер паспорта в формате NNNN-NNNNNN,"
                                              "где N - цифра: "))

    tmp.full_name = check.field_full_name(input("Введите полное ФИО: "))

    tmp.date_born = check.field_date_born(input("Введите год рождения"
                                                "Формат ввода: ДД/ММ/ГГГГ: "))

    tmp.address = check.field_address(input("Введите адрес проживания: "))

    tmp.goal = check.field_goal(input("Введите цель поездки: "))

    res = visitor_base.add_record(tmp)

    if res is True:
        print("Запись о новом постояльце успешно добавлена!")
        return
    elif res == tmp.passport:
        print("Запись с таким паспортным номером уже существует!")
        return

    print("Запись о новом пользователе не добавлена! Таблица заполнена!")
    return


def main():
    visitor_base = ht.HashTable()

    len_of_options = None

    while True:
        fl = False
        option = None

        while fl is False:
            gui.MainMenuCLS.name_app()
            len_of_options = gui.MainMenuCLS.main_menu()

            option = input("Введите номер действия: ")

            option, fl = check.choice(option, len_of_options)

            if fl is False:
                input('Нажмите "Enter", чтобы повторить ввод!')
                system("cls")

        if option == 0:
            break
        elif option == 1:
            new_visitor(visitor_base)
            input("OK")
        elif option == 2:
            pass
        elif option == 3:
            visitor_base.show_records()
            input("OK")
        elif option == 4:
            visitor_base.empty_table()
            input("OK")

        elif option == 5:
            tmp = visitor_base.get_record()
        elif option == 6:
            pass
        elif option == 7:
            pass
        elif option == 8:
            pass
        elif option == 9:
            pass
        elif option == 10:
            pass
        elif option == 11:
            pass
        elif option == 12:
            pass
        elif option == 13:
            pass
        elif option == 14:
            pass


if __name__ == "__main__":
    main()
