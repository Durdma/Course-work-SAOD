from typing import Callable, Iterator, Union, Optional
import operator

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
            print("Список пуст!")
            return

        tmp = self.head
        tmp.node.show_record()

        while tmp.right_node is not None:
            tmp.right_node.node.show_record()
            tmp = tmp.right_node

        return

    def __sort_records(self):
        pass


