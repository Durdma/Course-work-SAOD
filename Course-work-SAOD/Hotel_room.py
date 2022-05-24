from dataclasses import dataclass


@dataclass
class HotelRoom:
    number: str = ""
    places: int = 0
    rooms: int = 0
    bathroom: bool = False
    furniture: str = ""
    living: int = 0

    def show_room(self) -> None:
        print("*" * 70)
        print(f"Номер комнаты: {self.number}")
        print(f"Максимальное количество жильцов: {self.places}")
        print(f"Количество комнат: {self.rooms}")

        if self.bathroom is True:
            print("Наличие санузла: Есть")
        else:
            print("Наличие санузла: Нет")

        print(f"Оборудование: {self.furniture}")
        print(f"Проживает {self.living}")
        print("*" * 70)
