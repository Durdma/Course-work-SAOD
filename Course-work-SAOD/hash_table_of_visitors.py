class HashTable:
    def __init__(self):
        self.table = [{}] * 2000

    def __hash_func(self, passport: str) -> int:
        coefficients = (11, 13, 17, 19, 23, 29, 31, 37, 41, 43)

        result = 0

        def get_code():
            # NNNN - NNNNNN code of numbers in [48:58]
            to_key = list()

            for number in passport:
                if number == "-":
                    continue

                to_key.append(ord(number))

            return to_key

        codes = get_code()

        for index in range(codes):
            result += codes[index] * coefficients[index]

        return result

    def add_new_record(self):
        pass

