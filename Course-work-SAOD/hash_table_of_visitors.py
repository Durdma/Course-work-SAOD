import Visitor


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class HashTable(metaclass=Singleton):

    def __init__(self):
        self.table = [Visitor.Visitor()] * 2000

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

        for index in range(len(codes)):
            result += codes[index] * coefficients[index]

        return result % 2000

    def __hash_func_second(self, hashfunc: int):
        i = 1

        while hashfunc <= len(self.table):
            hashfunc += 2 * i + 4 * i ** 2

            if self.table[hashfunc].passport != "":
                i += 1
                continue

            return hashfunc

        return False

    def empty_table(self):
        self.table = [Visitor.Visitor()] * 2000
        print("База постояльцев очищена!")

    def add_record(self, visitor: Visitor) -> bool:
        if self.__find_record(visitor.passport) is not False:
            return visitor.passport

        address = self.__hash_func_first(visitor.passport)

        if self.table[address].passport != "":
            address = self.__hash_func_second(address)

        if address is False:
            return False

        else:
            self.table[address] = visitor
            return True

    def get_record(self, passport):
        return self.table[self.__find_record(passport)]

    def __find_record(self, passport: str):
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
        address = self.__find_record(passport)

        if address is False:
            return False

        self.table[address] = Visitor.Visitor()

    def find_fio(self, fio: str):
        tmp = list()

        for visitor in self.table:
            if visitor.full_name == fio:
                tmp.append(visitor)



    def show_records(self):
        count = 0
        print("*" * 70)
        for record in self.table:
            if record.passport != "":
                print(f"Номер паспорта: {record.passport}\n ФИО: {record.full_name}\n Дата рождения: {record.date_born}\n"
                      f"Место жительства: {record.address}\n Цель приезда: {record.goal}")
                print("*" * 70)

                count += 1

        if count == 0:
            print("База постояльцев пуста!")
            print("*" * 70)

    # def show_one_visitor(self, passport):
    #     visitor =
