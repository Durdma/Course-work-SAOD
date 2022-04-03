class Visitor:
    def __init__(self):
        self.__passport = None
        self.__full_name = ""
        self.__date_born = None
        self.__address = ""
        self.__goal = ""

    # Start of Getters
    @property
    def get_passport(self):
        return self.__passport

    @property
    def get_full_name(self):
        return self.__full_name

    @property
    def get_date_born(self):
        return self.__date_born

    @property
    def get_address(self):
        return self.__address

    @property
    def get_goal(self):
        return self.__goal

    # End of Getters

    # Start of Setters

    def set_passport(self, in_passport):
        return self.__passport

    def set_full_name(self, in_full_name):
        return self.__full_name

    def set_date_born(self, in_date_born):
        return self.__date_born

    def set_address(self, in_address):
        return self.__address

    def set_goal(self, in_goal):
        return self.__goal

    # End of Setters
