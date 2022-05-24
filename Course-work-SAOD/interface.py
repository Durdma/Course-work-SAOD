from os import system
from typing import Callable, Iterator, Union, Optional


class MainMenuCLS:
    @staticmethod
    def name_app() -> None:
        system("cls")
        print("*" * 70)
        print("Регистрация постояльцев в гостинице")

    @staticmethod
    def main_menu() -> int:
        options = (
                    "1) Зарегистрировать нового постояльца",
                    "2) Удаление данных о постояльце",
                    "3) Просмотреть всех зарегистрированных постояльцев",
                    "4) Очистить данные о постояльцах",
                    "5) Найти постояльца по номеру паспорта",
                    "6) Найти постояльца по ФИО",
                    "7) Добавить новый гостиничный номер",
                    "8) Удалить сведения о гостиничном номере",
                    "9) Просмотреть все имеющиеся гостиничные номера",
                    "10) Очистить данные о гостиничных номерах",
                    "11) Найти гостиничный номер по «номеру гостиничного номера»",
                    "12) Найти гостиничный номер по фрагментам «Оборудования»",
                    "13) Зарегистрировать вселение постояльца",
                    "14) Зарегистрировать выселение постояльца",
                    "0) Выйти из приложения"
                  )

        print("*" * 70)
        print()
        print("Выберите опцию: ")

        for option in options:
            print(option)

        print("*" * 70)
        print()

        return len(options)


class AddNewVisitor:
    @staticmethod
    def name_menu() -> None:
        system("cls")
        print("*" * 70)
        print("Регистрация постояльцев в гостинице")
        print("*" * 70)


class AddNewRoom:
    @staticmethod
    def name_menu() -> None:
        system("cls")
        print("*" * 70)
        print("Регистрация номеров в гостинице")
        print("*" * 70)
