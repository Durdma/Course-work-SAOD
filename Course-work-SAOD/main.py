from typing import Callable, Iterator, Union, Optional

import interface as gui
import check_funcs as check
import hash_table_of_visitors as ht
import Visitor as vs
import RoomTree as rt
import Hotel_room as room
import Record as rec
import ListOfRecords as lor


from os import system


def del_visitor(record_base, room_base, visitor_base):
    passport = check.field_passport_check_in_out(input("Введите номер паспорта: "), visitor_base)
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

    buff = check.field_number_check_in_out(input("Введите номер комнаты: "), room_base)
    if buff is False:
        print(f"Апартаментов с таким номером нет в базе!"
              "Запись невозможна!")
        input("OK")
        return
    else:
        tmp.number = buff

    buff = check.field_passport_check_in_out(input("Введите номер паспорта: "), visitor_base)
    if buff is False:
        print("Постояльца с таким номером паспорта нет в базе!"
              "Запись невозможна!")
        input("OK")
        return
    else:
        tmp.passport = buff

    if command == 0:
        tmp.check_in_date = check.field_date_born(input("Введите дату заселения: "))
    else:
        tmp.closing_date = check.field_date_born(input("Введите дату выселения: "))

    record_base.add_record_in_out(tmp, room_base)
    input("OK")
    return


def new_room(room_base) -> None:
    gui.AddNewRoom.name_menu()
    tmp = room.HotelRoom()

    # TODO Облагородить приглашения к вводу
    tmp.number = check.field_number(input("Введите номер комнаты в формате ХХХХ: "))
    tmp.places = check.field_places(input("Введите количество мест: "))
    tmp.rooms = check.field_rooms(input("Введите количество комнат: "))
    tmp.bathroom = check.field_bathroom(input("Наличие санузла: "))
    tmp.furniture = check.field_furniture(input("Введите описание номера: "))

    if room_base.root is not None:
        if room_base.root.find(tmp.number) is not False:
            print("Апартаменты с таким номером уже есть в базе!")
            return
        else:
            res = room_base.add_node(tmp)

    else:
        room_base.add_node(tmp)

    input("OK")


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
    room_base = rt.RoomTree()
    record_base = lor.ListOfRecords()

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
            del_visitor(record_base, room_base, visitor_base)
            input("OK")
        elif option == 3:
            visitor_base.show_records()
            input("OK")
        elif option == 4:
            visitor_base.empty_table()
            record_base.del_all()
            room_base.zero_tree()
            input("OK")

        elif option == 5:
            visit = visitor_base.get_record(check.field_passport(input("Введите номер паспорта в формате NNNN-NNNNNN,"
                                                                     "где N - цифра: ")))
            if visit is False:
                print("Запись о постояльце с таким номером паспорта не найдена!")
            else:
                visit.show_visitor()
                tmp = record_base.find_by_passport(visit.passport)

                if tmp is not None:

                    if len(tmp) == 0:
                        print("Нет зарегистрированных номеров на этот паспорт!")
                    else:
                        print("Зарегистрированные номера: ")
                        for value in tmp:
                            print(f"{value}")

                else:
                    print("Нет зарегистрированных номеров на этот паспорт!")

            input("OK")
        elif option == 6:
            tmp = visitor_base.find_fio(check.field_full_name(input("Введите полное ФИО: ")))

            if len(tmp) != 0:
                for visitor in tmp:
                    visitor.show_visitor()
            else:
                print("Постояльцев с такими данными нет!")
            input("OK")

        elif option == 7:
            new_room(room_base)
            input("OK")
        elif option == 8:
            number = check.field_number_check_in_out(input("Номер для удаления: "), room_base)
            record_base.del_by_number(number)
            room_base.delete_node(number)
            room_base.show_tree()
            input("OK")
        elif option == 9:
            room_base.show_table()
            room_base.show_tree()
            input("OK")
        elif option == 10:
            room_base.clear_tree()
            record_base.del_all()
            input("OK")
            # TODO ошибка после удаления не работает self.head.numer в листе
        elif option == 11:
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
                                print(f"{value}    {visitor_base.get_record(value).full_name}")
                    else:
                        print("Ничего не найдено!")
            input("OK")
        elif option == 12:
            tmp = input("Введите описание: ")
            command = int(input("Полный поиск(1), частичный (0): "))
            if room_base.root is not None:
                room_base.root.table_furniture(tmp, command)
            else:
                print("База комнат пуста!")
            input("OK")
            # TODO добавление юзера с тем же паспортом в тот же номер без выезда, выезд тоже самое
        elif option == 13:
            new_record_check_in_out(room_base, visitor_base, record_base, 0)
            record_base.show_records()
            input("OK")
        elif option == 14:
            new_record_check_in_out(room_base, visitor_base, record_base, 1)
            record_base.show_records()
            input("OK")
        elif option == 15:
            record_base.show_records()
            input("OK")


if __name__ == "__main__":
    main()
