from typing import Callable, Iterator, Union, Optional, Tuple

from re import match

import hash_table_of_visitors as ht
import RoomTree as rt


def choice(option, len_of_options) -> tuple:
    def _not_in_range() -> Optional[bool]:
        print("Введенное число не соответствует ни одному из номеров действий!")
        print("Повторите ввод!")
        return None, False

    def _not_int() -> Optional[bool]:
        print("Введенная строка не является числом! Повторите ввод!")
        print("Повторите ввод!")
        return None, False

    try:
        option = int(option)

        if (len_of_options - 1) < option or option < 0:
            return _not_in_range()

        return option, True

    except ValueError:
        return _not_int()


def field_passport(passport) -> str:
    pattern = r"^\d\d\d\d-\d\d\d\d\d\d$"

    while match(pattern, passport) is None:
        passport = input("Некорректный ввод номера паспорта! \n"
                         "Введите номер паспорта заново в формате NNNN-NNNNNN,"
                         "где N - цифра: ")

    return passport


def field_full_name(full_name) -> str:
    pattern = r"^[А-Яа-яA-Za-z ,.'-]+$"

    while match(pattern, full_name) is None and len(full_name) <= 60:
        full_name = input("Некорректный ввод ФИО! ФИО может содержать только буквы!"
                          "Повторите ввод: ")

    return full_name


def field_date_born(date_born) -> str:
    pattern = r"^(?<!\d)(?:0?[1-9]|[12][0-9]|3[01])-" \
              r"(?:0?[1-9]|1[0-2])-(?:19[0-9][0-9]|20[01][0-9]|20[2][012])(?!\d)$"

    while match(pattern, date_born) is None:
        date_born = input("Некорректный ввод даты! Повторите ввод!"
                          "Формат ввода: ДД-ММ-ГГГГ: ")

    return date_born


def field_address(address) -> str:
    while len(address) > 120 or address == "":
        if address == "":
            address = input("Введите адрес проживания: ")
        elif len(address) > 120:
            address = input("Количество символов превысило 120! "
                            "Повторите ввод адреса: ")

    return address


def field_goal(goal) -> str:
    while len(goal) > 255 or goal == "":
        if goal == "":
            goal = input("Введите цель приезда: ")
        elif len(goal) > 255:
            goal = input("Количество символов превысило 255!"
                         "Повторите ввод цели приезда: ")

    return goal


def field_number(number) -> str:
    pattern = r"^[ЛПОМ][0-9][0-9][0-9]+$"

    while match(pattern, number) is None:
        number = input("Введите номер апартаментов в формате LNNN \n"
                       "Где L может быть: \n"
                       "Л - люкс апартаменты; \n"
                       "П - полулюкс апартаменты; \n"
                       "М - многоместные апартаменты; \n"
                       "О - обычные апартаменты. \n"
                       "NNN - номер от 000 до 999: ")

    return number


def field_places(places) -> int:
    while True:
        try:
            places = int(places)
            if places <= 0:
                print("Введенное число должно быть больше нуля! Повторите ввод!")
                places = input("Введите количество мест в апартаментах: ")
                continue
            return places
        except ValueError:
            print("Некорректный ввод количества мест в апартаментах! Повторите ввод")
            places = input("Введите количество мест в апартаментах: ")


def field_rooms(rooms) -> int:
    while True:
        try:
            rooms = int(rooms)
            if rooms <= 0:
                print("Введенное число должно быть больше нуля! Повторите ввод!")
                rooms = input("Введите количество комнат в апартаментах: ")
                continue
            return rooms
        except ValueError:
            print("Некорректный ввод количества комнат в апартаментах! Повторите ввод")
            rooms = input("Введите количество комнат в апартаментах: ")


def field_bathroom(bath) -> bool:
    while True:
        if bath == "Есть":
            return True
        if bath == "Нет":
            return False
        if bath != "Есть" or bath != "Нет":
            print("Введенное значение не соответствует ни одному из вариантов ответа!"
                  "Повторите ввод!")
            bath = input("Наличие санузла (Есть/Нет): ")


def field_furniture(furn) -> str:
    while len(furn) > 512 or furn == "":
        if len(furn) > 512:
            furn = input("Количество символов превысило 512!"
                         "Повторите ввод описания номера: ")
        elif furn == "":
            furn = input("Заполните описание апартаментов: ")

    return furn


def field_number_check_in_out(number, room_base: rt.RoomTree):
    res = field_number(number)
    if room_base.root is not None:
        if room_base.root.find(number) is not None:
            return res

    return False


def field_passport_check_in_out(passport, visitor_base: ht.HashTable):
    res = field_passport(passport)

    if visitor_base.get_record(res) is not False:
        return res

    return False
