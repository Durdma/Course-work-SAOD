from dataclasses import dataclass


@dataclass
class Record:
    passport: str = ""
    number: str = ""


@dataclass
class CheckIn(Record):
    check_in_date: str = ""

    def show_record(self) -> None:
        print("*" * 70)
        print(f"Номер комнаты: {self.number}")
        print(f"Номер паспорта: {self.passport}")
        print(f"Дата заселения: {self.check_in_date}")
        print("*" * 70)


@dataclass
class Closing(Record):
    closing_date: str = ""

    def show_record(self) -> None:
        print("*" * 70)
        print(f"Номер комнаты: {self.number}")
        print(f"Номер паспорта: {self.passport}")
        print(f"Дата выселения: {self.closing_date}")
        print("*" * 70)
