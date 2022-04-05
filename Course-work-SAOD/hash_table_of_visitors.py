import Visitor


class HashTable:

    def __init__(self):
        self.table = [Visitor.Visitor()] * 2000

    @property
    def show_all_visitors(self):
        return [visitor for visitor in self.table if visitor.passport != ""]

    @property
    def empty_table(self):
        return [Visitor.Visitor()] * 2000

    def get_visitor(self, address):
        return self.table[address]

    @staticmethod
    def __hash_func_first(passport: str) -> int:
        coefficients = (11, 13, 17, 19, 23, 29, 31, 37, 41, 43)

        result = 0

        def _get_code():
            # NNNN - NNNNNN code of numbers in [48:58]
            to_key = list()

            for number in passport:
                if number == "-":
                    continue

                to_key.append(ord(number))

            return to_key

        codes = _get_code()

        for index in range(codes):
            result += codes[index] * coefficients[index]

        return result

    def __hash_func_second(self, hashfunc: int):
        i = 1

        while hashfunc <= len(self.table):
            hashfunc += 2 * i + 4 * i ** 2

            if self.table[hashfunc].passport != "":
                i += 1
                continue

            return hashfunc

        return False

    def add_record(self, visitor: Visitor) -> bool:
        address = self.__hash_func_first(visitor.passport)

        if self.table[address].passport != "":
            address = self.__hash_func_second(address)

        if address is False:
            return False

        else:
            self.table[address] = visitor
            return True

    def find_record(self, passport: str):
        address = self.__hash_func_first(passport)
        i = 0

        while address < len(self.table):
            address += 2 * i + 4 * i ** 2

            if self.table[address].passport == "":
                return False

            if self.table[address].passport == passport:
                return address

            i += 1

    def del_record(self, passport: str) -> bool:
        address = self.find_record(passport)

        if address is False:
            return False

        self.table[address] = Visitor.Visitor()

    def find_fio(self, fio: str):
        return [(visitor.full_name, visitor.passport) for visitor in self.table if visitor.full_name == fio]
