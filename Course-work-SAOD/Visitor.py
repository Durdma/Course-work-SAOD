from dataclasses import dataclass


@dataclass
class Visitor:
    passport: str = ""
    full_name: str = ""
    date_born: str = ""
    address: str = ""
    goal: str = ""
    room: int = None

