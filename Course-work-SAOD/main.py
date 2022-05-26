from typing import Callable, Iterator, Union, Optional

import interface as gui
import check_funcs as check
import hash_table_of_visitors as ht
import Visitor as vs
import RoomTree as rt
import Hotel_room as room
import Record as rec
import ListOfRecrods_v2 as lr2

from os import system


def find_visitor_by_passport(visitor_base, room_base) -> None:
    visit = visitor_base.get_record(check.field_passport(input("Введите номер паспорта в формате NNNN-NNNNNN,"
                                                               "где N - цифра: ")))
    if visit is False:
        print("Запись о постояльце с таким номером паспорта не найдена!")
    else:
        visit.show_visitor()
        tmp = room_base.root.find_passport(visit.passport)

        if tmp[0] is True:
            if tmp[1] is None:
                print("Нет зарегистрированных номеров на этот паспорт!")
            else:
                print("Зарегистрированные номера: ")
                print(f"{tmp[1]}")

        else:
            print("Нет зарегистрированных номеров на этот паспорт!")


def find_room_by_number(room_base, record_base, visitor_base) -> None:
    number = check.field_number(input("Введите номер: "))

    if room_base.root is None:
        print("Ничего не найдено!")
    else:
        if room_base.root.find(number) is False:
            print("Ничего не найдено!")
        else:
            res = room_base.root.find(number)
            res.node.show_room()

            buff = record_base.find_by_number(number)

            if buff is not None:
                buff = list(buff)
                if len(buff) == 0:
                    print("Ничего не найдено!")

                else:
                    for value in buff:
                        if visitor_base.get_record(value) is not False:
                            print(f"{value}    {visitor_base.get_record(value).full_name}")
                        else:
                            print("Ошибка при выводе, пустое поле в хэше!")
            else:
                print("Ничего не найдено!")


def del_visitor(record_base, room_base, visitor_base) -> None:
    passport = check.field_passport_check_in_out(input("Введите номер паспорта в формате NNNN-NNNNNN, где N - цифра: "),
                                                 visitor_base)
    if passport is False:
        print("Постояльца с таким номером паспорта нет в базе!"
              "Запись невозможна!")
        input("OK")
        return
    else:
        record_base.del_record(passport, room_base)
        visitor_base.del_record(passport)
        return


def new_record_check_in_out(room_base, visitor_base, record_base, command) -> None:
    if command == 0:
        tmp = rec.CheckIn()
    else:
        tmp = rec.Closing()

    # number - number
    number = check.field_number_check_in_out(input("Введите номер апартаментов в формате LNNN \n"
                                                   "Где L может быть: \n"
                                                   "Л - люкс апартаменты; \n"
                                                   "П - полулюкс апартаменты; \n"
                                                   "М - многоместные апартаменты; \n"
                                                   "О - обычные апартаменты. \n"
                                                   "NNN - номер от 000 до 999: "), room_base)
    if number is False:
        print(f"Апартаментов с таким номером нет в базе! \n"
              "Запись невозможна!")
        input("OK")
        return
    else:
        # комната существует
        # passport - passport
        passport = check.field_passport_check_in_out(input("Введите номер паспорта в формате NNNN-NNNNNN, где N - "
                                                           "цифра: "), visitor_base)

        if passport is False:
            print("Постоялец с таким номером паспорта не зарегистрирован!")
            input("OK")
            return
        else:
            if command == 0:
                res = room_base.root.find_passport(passport)
                if res[0] is True:
                    print(f"Постоялец с таким номером паспорта уже живет в номере {res[1]}")
                    input("OK")
                    return
                else:
                    # нигде не живет
                    living = room_base.root.find_number_living(number)
                    if living is not False:
                        if len(living) >= room_base.root.find(number).node.places:
                            print("Апартаменты заполнены! Заселение невозможно!")
                            input("OK")
                            return
                        else:
                            tmp.number = number
                            tmp.passport = passport
                            tmp.check_in_date = check.field_date_born(input("Введите дату заселения в формате "
                                                                            "ДД-ММ-ГГГГ: "))
                            room_base.root.update_living(passport, number, command)
                            record_base.add_record(tmp)
                            input("OK")
                            return
                    else:
                        print("Непредвиденная ошибка!")
                        input("OK")
                        return
            if command == 1:
                if passport in room_base.root.find_number_living(number):
                    tmp.number = number
                    tmp.passport = passport
                    tmp.closing_date = check.field_date_born(input("Введите дату выселения в формате ДД-ММ-ГГГГ: "))
                    room_base.root.update_living(passport, number, command)
                    record_base.add_record(tmp)
                    input("OK")
                    return
                else:
                    print(f"Постоялец с паспортным номером {passport} не проживает в номере {number}")
                    input("OK")
                    return
    #
    # number = check.field_passport_check_in_out(input("Введите номер паспорта: "), visitor_base)
    # if number is False:
    #     print("Постояльца с таким номером паспорта нет в базе!"
    #           "Запись невозможна!")
    #     input("OK")
    #     return
    # else:
    #     tmp.passport = number
    #
    # if command == 0:
    #     tmp.check_in_date = check.field_date_born(input("Введите дату заселения: "))
    # else:
    #     tmp.closing_date = check.field_date_born(input("Введите дату выселения: "))
    #
    # record_base.add_record_in_out(tmp, room_base)
    input("OK")
    return


def new_room(room_base) -> None:
    tmp = room.HotelRoom()

    tmp.number = check.field_number(input("Введите номер апартаментов в формате LNNN \n"
                                          "Где L может быть: \n"
                                          "Л - люкс апартаменты; \n"
                                          "П - полулюкс апартаменты; \n"
                                          "М - многоместные апартаменты; \n"
                                          "О - обычные апартаменты. \n"
                                          "NNN - номер от 000 до 999: "))
    tmp.places = check.field_places(input("Введите количество мест в апартаментах: "))
    tmp.rooms = check.field_rooms(input("Введите количество комнат в апартаментах: "))
    tmp.bathroom = check.field_bathroom(input("Наличие санузла (Есть/Нет): "))
    tmp.furniture = check.field_furniture(input("Заполните описание апартаментов \n"
                                                "(перечислите через запятую, что есть в номере): "))

    if room_base.root is not None:
        if room_base.root.find(tmp.number) is not False:
            print("Апартаменты с таким номером уже есть в базе!")
            return
        else:
            room_base.add_node(tmp)

    else:
        room_base.add_node(tmp)

    input("OK")


def new_visitor(visitor_base) -> None:
    tmp = vs.Visitor()

    tmp.passport = check.field_passport(input("Введите номер паспорта в формате NNNN-NNNNNN,"
                                              "где N - цифра: "))

    tmp.full_name = check.field_full_name(input("Введите полное ФИО: "))

    tmp.date_born = check.field_date_born(input("Введите год рождения"
                                                "Формат ввода: ДД-ММ-ГГГГ: "))

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
    room_base = rt.RoomTree()
    record_base = lr2.ListOfRecords()

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
            gui.MainMenuCLS.name_menu(option)
            new_visitor(visitor_base)
            input("OK")

        elif option == 2:
            gui.MainMenuCLS.name_menu(option)
            del_visitor(record_base, room_base, visitor_base)
            input("OK")

        elif option == 3:
            gui.MainMenuCLS.name_menu(option)
            visitor_base.show_records()
            input("OK")

        elif option == 4:
            gui.MainMenuCLS.name_menu(option)
            visitor_base.empty_table()
            record_base.del_all()
            room_base.zero_tree()
            input("OK")

        elif option == 5:
            gui.MainMenuCLS.name_menu(option)
            find_visitor_by_passport(visitor_base, room_base)
            input("OK")

        elif option == 6:
            gui.MainMenuCLS.name_menu(option)
            tmp = visitor_base.find_fio(check.field_full_name(input("Введите часть ФИО: ")))

            if len(tmp) != 0:
                for visitor in tmp:
                    visitor.show_visitor()
            else:
                print("Постояльцев с такими данными нет!")
            input("OK")

        elif option == 7:
            gui.MainMenuCLS.name_menu(option)
            new_room(room_base)
            input("OK")

        elif option == 8:
            gui.MainMenuCLS.name_menu(option)
            number = check.field_number_check_in_out(input("Номер для удаления: "), room_base)
            record_base.del_by_number(number)
            room_base.delete_node(number)
            room_base.show_tree()
            input("OK")

        elif option == 9:
            gui.MainMenuCLS.name_menu(option)
            room_base.show_table()
            room_base.show_tree()
            input("OK")

        elif option == 10:
            gui.MainMenuCLS.name_menu(option)
            room_base.clear_tree()
            record_base.del_all()
            input("OK")

        elif option == 11:
            gui.MainMenuCLS.name_menu(option)
            find_room_by_number(room_base, record_base, visitor_base)
            input("OK")

        elif option == 12:
            gui.MainMenuCLS.name_menu(option)
            tmp = input("Введите описание: ")
            command = int(input("Полный поиск(1), частичный (0): "))
            if room_base.root is not None:
                room_base.root.table_furniture(tmp, command)
            else:
                print("База комнат пуста!")
            input("OK")

        elif option == 13:
            gui.MainMenuCLS.name_menu(option)
            new_record_check_in_out(room_base, visitor_base, record_base, 0)
            record_base.show_records()
            input("OK")

        elif option == 14:
            gui.MainMenuCLS.name_menu(option)
            new_record_check_in_out(room_base, visitor_base, record_base, 1)
            record_base.show_records()
            input("OK")

        elif option == 15:
            gui.MainMenuCLS.name_menu(option)
            record_base.show_records()
            input("OK")


if __name__ == "__main__":
    main()
