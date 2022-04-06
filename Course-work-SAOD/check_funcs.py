from re import match


def choice(option, len_of_options):
    def _not_in_range():
        print("Введенное число не соответсвует ни одному из номеров действий!")
        print("Повторите ввод!")
        return None, False

    def _not_int():
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


def field_passport(passport):
    pattern = r"^\d\d\d\d-\d\d\d\d\d\d$"

    while match(pattern, passport) is None:
        passport = input("Некорректный ввод номера паспорта! \n"
                         "Введите номер паспорта заново в формате NNNN-NNNNNN,"
                         "где N - цифра: ")

    return passport


def field_full_name(full_name):
    pattern = r"^[А-Яа-яA-Za-z ,.'-]+$"

    while match(pattern, full_name) is None and len(full_name) <= 60:
        full_name = input("Некорректный ввод ФИО! ФИО может содержать только буквы!"
                          "Повторите ввод: ")

    return full_name


def field_date_born(date_born):
    pattern = r"^(?<!\d)(?:0?[1-9]|[12][0-9]|3[01])-" \
              r"(?:0?[1-9]|1[0-2])-(?:19[0-9][0-9]|20[01][0-9]|20[2][012])(?!\d)$"

    while match(pattern, date_born) is None:
        date_born = input("Некорректный ввод даты рождения! Повторите ввод!"
                          "Формат ввода: ДД/ММ/ГГГГ: ")

    return date_born


def field_address(address):
    while len(address) > 60:
        address = input("Количество символов превысило 60! "
                        "Повторите ввод адреса: ")

    return address


def field_goal(goal):
    while len(goal) > 120:
        goal = input("Количество символов превысило 120!"
                     "Повторите ввод цели приезда: ")

    return goal
