from dataclasses import dataclass


@dataclass
class Record:
    passport: str = ""
    number: str = ""
    registration_date: str = ""
    closing_date: str = ""

    def show_record(self) -> None:
        print("*" * 70)
        print(f"Номер паспорта: {self.passport}")
        print(f"Номер комнаты: {self.number}")
        print(f"Дата заселения: {self.registration_date}")
        print(f"Дата выселения: {self.closing_date}")
        print("*" * 70)
