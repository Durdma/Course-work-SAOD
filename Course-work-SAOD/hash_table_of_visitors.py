from typing import Callable, Iterator, Union, Optional, List

import Visitor as vs
import textAlgo as algo


# Singleton
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


# Хэш-таблица
class HashTable(metaclass=Singleton):

    def __init__(self):
        self.table = [vs.Visitor()] * 2000

    # Хэш функция №1
    @staticmethod
    def __hash_func_first(passport: str) -> int:
        coefficients = (59, 61, 71, 73, 79, 83, 89, 97, 101, 103)

        result = 0

        # Преобразование символов в код
        def _get_code() -> List[int]:
            # NNNN - NNNNNN code of numbers in [48:58]
            to_key = list()

            for number in passport:
                if number == "-":
                    continue

                to_key.append(ord(number))

            return to_key

        codes = _get_code()

        for index in range(len(codes)):
            result += codes[index] * coefficients[index]

        return result % 2000

    # Хэш функция №2
    def __hash_func_second(self, hashfunc: int) -> Union[bool, int]:
        i = 1

        while hashfunc <= len(self.table):
            hashfunc += i*11 + 3*i**2

            if self.table[hashfunc].passport != "" and self.table[hashfunc].passport != "Deleted":
                i += 1
                continue

            print(f"Итераций {i}")
            return hashfunc

        return False

    # Очистка хэш-таблицы
    def empty_table(self) -> None:
        self.table = [vs.Visitor()] * 2000
        print("База постояльцев очищена!")

    # Добавление записи в хэш-таблицу
    def add_record(self, visitor: vs.Visitor) -> bool:
        if self.__find_record(visitor.passport) is not False:
            return visitor.passport

        address = self.__hash_func_first(visitor.passport)

        if self.table[address].passport != "" and self.table[address] != "Deleted":
            address = self.__hash_func_second(address)

        if address is False:
            return False

        else:
            self.table[address] = visitor
            return True

    # TODO 1- Решить как и где обрабатывать пустое место
    # Получить запись из хэш таблицы по номеру паспорта
    def get_record(self, passport) -> Optional[vs.Visitor]:
        res = self.__find_record(passport)

        if res is False:
            return False

        return self.table[res]

    # Поиск записи по номеру паспорта в хэш-таблице
    def __find_record(self, passport: str) -> Union[int, bool]:
        address = self.__hash_func_first(passport)
        i = 0

        while address < len(self.table):
            address += i*11 + 3*i**2

            if self.table[address].passport == "Deleted":
                i += 1
                continue

            if self.table[address].passport == "":
                return False

            if self.table[address].passport == passport:
                return address

            i += 1

    # Удаление записи из хэш-таблицы по номеру паспорта
    def del_record(self, passport: str) -> Optional[bool]:
        address = self.__find_record(passport)

        if address is False:
            return False

        self.table[address] = vs.Visitor("Deleted")
        return

    # Поиск постояльцев по ФИО
    def find_fio(self, fio: str) -> List[vs.Visitor]:
        tmp = list()

        for visitor in self.table:
            if algo.search(visitor.full_name, fio):
                tmp.append(visitor)

        return tmp

    # Вывести всю хэш-таблицу
    def show_records(self) -> None:
        count = 0
        for record in self.table:
            if record.passport != "" and record.passport != "Deleted":
                record.show_visitor()
                count += 1

        if count == 0:
            print("База постояльцев пуста!")
            print("*" * 70)

        return
