from typing import Callable, Iterator, Union, Optional, Tuple

from re import match

choice_output = Union[
                        Callable[[], Optional[False]],
                        Tuple[int, True]
                     ]


def choice(option, len_of_options) -> choice_output:
    def _not_in_range() -> Optional[False]:
        print("Введенное число не соответсвует ни одному из номеров действий!")
        print("Повторите ввод!")
        return None, False

    def _not_int() -> Optional[False]:
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
        date_born = input("Некорректный ввод даты рождения! Повторите ввод!"
                          "Формат ввода: ДД/ММ/ГГГГ: ")

    return date_born


def field_address(address) -> str:
    while len(address) > 120:
        address = input("Количество символов превысило 60! "
                        "Повторите ввод адреса: ")

    return address


def field_goal(goal) -> str:
    while len(goal) > 255:
        goal = input("Количество символов превысило 120!"
                     "Повторите ввод цели приезда: ")

    return goal
