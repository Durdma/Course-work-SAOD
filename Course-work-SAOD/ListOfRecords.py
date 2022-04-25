from typing import Callable, Iterator, Union, Optional

import Record as rec


class Node:
    def __init__(self, record: rec.Record = None):
        self.node: rec.Record = record
        self.left_node: Node = None
        self.right_node: Node = None


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class ListOfRecords(metaclass=Singleton):

    def __init__(self):
        self.head: Node = None

    def add_record(self, record: rec.Record) -> None:
        if self.head is None:
            self.head.node = record
            return

        tmp = self.head
        buff = Node(record)

        while tmp.right_node is not None:
            tmp = tmp.right_node

        tmp.right_node = buff
        buff.left_node = tmp
        return

    def show_records(self) -> None:
        if self.head is None:
            print("Список пуст!")
            return

        tmp = self.head

        while tmp.right_node is not None:
            tmp.right_node.node.show_record()
            tmp = tmp.right_node

        return




