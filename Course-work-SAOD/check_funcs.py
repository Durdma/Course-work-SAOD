def check_choice(option, len_of_options):
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


