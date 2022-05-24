from typing import Callable, Iterator, Union, Optional, List

import Hotel_room as room
import textAlgo as algo


class Node(object):
    def __init__(self, input_room: room.HotelRoom = None, parent = None):
        self.node: room.HotelRoom = input_room
        self.left_node: Node = None
        self.right_node: Node = None
        self.parent: Node = parent
        self.height = 1

    def get_balance(self):
        left = self.left_node.height if self.left_node else 0
        right = self.right_node.height if self.right_node else 0
        return left - right

    def update_height(self):
        left = self.left_node.height if self.left_node else 0
        right = self.right_node.height if self.right_node else 0
        self.height = max(left, right) + 1

    def table(self):
        if self:
            if self.node.number is not None:
                self.node.show_room()
            if self.left_node is not None:
                self.left_node.table()
            if self.right_node is not None:
                self.right_node.table()

    def table_furniture(self, pattern: str, command: int):
        pattern = pattern.split(", ")
        if self:
            if self.node.number is not None:
                self.__search_furniture(pattern, command)
            if self.left_node is not None:
                self.left_node.__search_furniture(pattern, command)
            if self.right_node is not None:
                self.right_node.__search_furniture(pattern, command)

    def __search_furniture(self, pattern: list, command):
        if command == 0:
            for value in pattern:
                res = algo.search(self.node.furniture, value)
                if res is True:
                    return self.node.show_room()

        if command == 1:
            counter = 0

            for value in pattern:
                res = algo.search(self.node.furniture, value)
                if res is True:
                    counter += 1

            if counter == len(pattern):
                return self.node.show_room()

    def find(self, key):
        res = None
        if self.node is not None:
            if self.node.number == key:
                res = self
                print(f"Номер {res.node.number} найден!")
                return res
            if self.left_node is not None:
                res = self.left_node.find(key)
                if res is not None:
                    return res
            if self.right_node is not None:
                res = self.right_node.find(key)
                if res is not None:
                    return res

        else:
            return False

    def find_min(self):
        return self if not self.left_node else self.left_node.find_min()

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right_node is None and self.left_node is None:
            line = '%s' % self.node.number
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right_node is None:
            lines, n, p, x = self.left_node._display_aux()
            s = '%s' % self.node.number
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left_node is None:
            lines, n, p, x = self.right_node._display_aux()
            s = '%s' % self.node.number
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left_node._display_aux()
        right, m, q, y = self.right_node._display_aux()
        s = '%s' % self.node.number
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class RoomTree(metaclass=Singleton):
    def __init__(self):
        self.root: Node = None

    # Добавление нового листа в дерево
    def add_node(self, value: room.HotelRoom):
        if self.root is None:
            self.root = Node(value)
            return self.root
        else:
            return self.__restore_balance(self.__insert(self.root, value))

    def clear_tree(self):
        self.root = None
        return self.root

    def show_tree(self):
        if self.root is None:
            print("База пуста!")
            return

        self.root.display()

    def show_table(self):
        self.root.table()

    # Внутренний метод добавления, если корень не пуст
    @staticmethod
    def __insert(root: Node, value: room.HotelRoom):
        if value.number < root.node.number:
            if not root.left_node:
                root.left_node = Node(value, root)
                return root
            else:
                return RoomTree.__insert(root.left_node, value)
        else:
            if not root.right_node:
                root.right_node = Node(value, root)
                return root
            else:
                return RoomTree.__insert(root.right_node, value)

    def __restore_balance(self, noda: Node):
        if not noda:
            return

        height = noda.height
        noda.update_height()
        tmp = noda

        if noda.get_balance() == -2:
            if noda.right_node.get_balance() == 1:
                self.__right_rotation(noda.right_node)

            tmp = self.__left_rotation(noda)

        elif noda.get_balance() == 2:
            if noda.left_node.get_balance() == -1:
                self.__left_rotation(noda.left_node)

                tmp = self.__right_rotation(noda)

        if tmp.height != height or abs(tmp.get_balance()) > 1:
            self.__restore_balance(tmp.parent)

    def __right_rotation(self, noda: Node):
        tmp = noda.left_node
        noda.left_node = tmp.right_node

        if tmp.right_node:
            tmp.right_node.parent = noda

        tmp.right_node = noda
        tmp.parent = noda.parent
        noda.parent = tmp
        noda.update_height()
        tmp.update_height()
        buff = tmp.parent

        if not buff:
            self.root = tmp
        elif buff.left_node is noda:
            buff.left_node = tmp
        else:
            buff.right_node = tmp

        return tmp

    def __left_rotation(self, noda: Node):
        tmp = noda.right_node
        noda.right_node = tmp.left_node

        if tmp.left_node:
            tmp.left_node.parent = noda

        tmp.left_node = noda
        tmp.parent = noda.parent
        noda.parent = tmp
        noda.update_height()
        tmp.update_height()
        buff = tmp.parent

        if not buff:
            self.root = tmp
        elif buff.left_node is noda:
            buff.left_node = tmp
        else:
            buff.right_node = tmp

        return tmp

    def delete_node(self, key):
        if self.root is None:
            print("Удаление невозможно! Нет записей!")
            return

        noda = self.root.find(key)

        if not noda:
            print(f"Ошибка, записи с значением {key} не существует!")
            return

        if noda.left_node and noda.right_node:
            if noda.right_node.left_node is None:
                tmp = noda.right_node
                tmp.left_node = noda.left_node
                tmp.parent = noda.parent

                if noda.parent.left_node is noda:
                    noda.parent.left_node = tmp
                elif noda.parent.right_node is noda:
                    noda.parent.right_node = tmp
            return self.__restore_balance(tmp)

        if not noda.left_node and not noda.right_node:
            children = None
        elif not noda.left_node:
            children = noda.right_node
        else:
            children = noda.left_node

        tmp = noda.parent

        if children:
            children.parent = tmp

        if not tmp:
            self.root = children

        else:
            if tmp.left_node is noda:
                tmp.left_node = children
            else:
                tmp.right_node = children

        self.__restore_balance(tmp)

