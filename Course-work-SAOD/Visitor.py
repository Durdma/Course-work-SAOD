from dataclasses import dataclass


@dataclass
class Visitor:
    passport: str = ""
    full_name: str = ""
    date_born: str = ""
    address: str = ""
    goal: str = ""

    def show_visitor(self) -> None:
        print("*" * 70)
        print(f"Номер паспорта: {self.passport}")
        print(f"ФИО: {self.full_name}")
        print(f"Дата рождения: {self.date_born}")
        print(f"Адрес проживания: {self.address}")
        print(f"Цель приезда: {self.goal}")
        print("*" * 70)

