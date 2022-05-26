from typing import Callable, Iterator, Union, Optional
import operator
from collections import defaultdict

import Record as rec
import RoomTree as rt
# import Hotel_room as room
# import hash_table_of_visitors as ht
# import Visitor as vs

# Кастомный тип для записей
T = Union[rec.Record, rec.CheckIn, rec.Closing]


class Node:
    def __init__(self, record: T = None):
        self.node: T = record
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

    def add_record(self, record: T) -> None:
        if self.head is None:
            self.head = Node(record)
            return

        if self.head.node is None:
            self.head = Node(record)
            return

        tmp = self.head
        buff = Node(record)

        while tmp.right_node is not None:
            tmp = tmp.right_node

        tmp.right_node = buff
        buff.left_node = tmp
        self.__sort_list()
        return

    def del_all(self):
        self.head = None
        return

    def __sort_list(self):
        buff_list = list()
        buff_list.append(self.head)

        tmp = self.head

        while tmp.right_node is not None:
            buff_list.append(tmp.right_node)
            tmp = tmp.right_node

        if len(buff_list) == 1:
            return
        else:
            buff_list = self.__merge_sort(buff_list)
            for index in range(len(buff_list)):
                buff_list[index].left_node = None
                buff_list[index].right_node = None
            self.head = buff_list[0]

            tmp = self.head

            for index in range(1, len(buff_list), 1):
                tmp.right_node = buff_list[index]
                tmp.right_node.left_node = tmp
                tmp = tmp.right_node

    @staticmethod
    def __merge_sort(merge_list: list[Node], compare=operator.lt):
        if len(merge_list) < 2:
            return merge_list[:]
        else:
            mid = int(len(merge_list) / 2)
            left = ListOfRecords.__merge_sort(merge_list[:mid], compare)
            right = ListOfRecords.__merge_sort(merge_list[mid:], compare)
            return ListOfRecords.__merge(left, right, compare)

    @staticmethod
    def __merge(left: list[Node], right: list[Node], compare):
        result = list()
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if compare(left[i].node.number, right[j].node.number):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result

    def show_records(self) -> None:
        if self.head is None:
            print("Список записей о заселении и выселении пуст!")
            return

        if self.head.node is None:
            print("Список записей о заселении и выселении пуст!")
            return

        tmp = self.head
        tmp.node.show_record()

        while tmp.right_node is not None:
            tmp.right_node.node.show_record()
            tmp = tmp.right_node

        return

    def del_record(self, passport, room_base: rt.RoomTree):
        tmp = self.head

        if self.head is None:
            print("Удаление невозможно список записей о заселении и выселении пуст!")
            return

        if self.head.node.passport == passport:
            self.head.node = self.head.right_node
            self.head.left_node = None

        while tmp.right_node is not None:
            if tmp.right_node.node.passport == passport:
                if isinstance(tmp.right_node.node, rec.CheckIn):
                    room_base.root.find(tmp.right_node.node.number).node.living += 1
                    if tmp.right_node.right_node is not None:
                        tmp.right_node.right_node.left_node = tmp
                        tmp.right_node = tmp.right_node.right_node
                    else:
                        tmp.right_node = None
                if isinstance(tmp.right_node.node, rec.Closing):
                    room_base.root.find(tmp.right_node.node.number).node.living -= 1
                    if tmp.right_node.right_node is not None:
                        tmp.right_node.right_node.left_node = tmp
                        tmp.right_node = tmp.right_node.right_node
                    else:
                        tmp.right_node = None

            tmp = tmp.right_node

        return

    def find_by_passport(self, passport):
        if self.head is None:
            print("Список записей о заселении и выселении пуст!")
            return

        if self.head.node is None:
            print("Список записей о заселении и выселении пуст!")
            return

        buff = list()

        if self.head.node.passport == passport:
            buff.append(self.head.node.number)

        tmp = self.head

        while tmp.right_node is not None:
            if tmp.right_node.node.passport == passport:
                buff.append(tmp.right_node.node.number)

            tmp = tmp.right_node

        return buff

    def del_by_number(self, number):
        if self.head is None:
            print("Удаление невозможно! Список записей о заселении и выселении пуст!")
            return

        if self.head.node is None:
            print("Удаление невозможно! Список записей о заселении и выселении пуст!")
            return

        if self.head.node.number == number:
            self.head.node = self.head.right_node
            self.head.left_node = None

        tmp = self.head

        while tmp.right_node is not None:
            if tmp.right_node.node.number == number:
                if tmp.right_node.right_node is not None:
                    tmp.right_node.right_node.left_node = tmp
                    tmp.right_node = tmp.right_node.right_node
                else:
                    tmp.right_node = None

        return

    def find_by_number(self, number):
        if self.head is None:
            print("Список записей о заселении и выселении пуст!")
            return

        if self.head.node is None:
            print("Список записей о заселении и выселении пуст!")
            return

        buff: list[T] = list()

        if self.head.node.number == number:
            buff.append(self.head.node)

        tmp = self.head

        while tmp.right_node is not None:
            if tmp.right_node.node.number == number:
                buff.append(tmp.right_node.node)
            tmp = tmp.right_node

        res = defaultdict(int)

        for value in buff:
            if isinstance(value, rec.CheckIn):
                res[value.passport] += 1
            if isinstance(value, rec.Closing):
                res[value.passport] -= 1

        return {value.passport for value in buff if res[value.passport] == 1}