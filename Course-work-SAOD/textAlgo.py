from collections import defaultdict

import Hotel_room as room
import RoomTree as tree


def forming_table(pattern):
    """ Формируем массив d."""
    d = [len(pattern) for i in range(1105)]
    new_p = pattern[::-1]

    for i in range(len(new_p)):
        if d[ord(new_p[i])] != len(new_p):
            continue
        else:
            d[ord(new_p[i])] = i
    return d


def search(field: str, pattern: str):
    """ Поиск Бойера - Мура."""

    field = field.lower()
    pattern = pattern.lower()

    d = forming_table(pattern)
    # x - начало прохода по string
    # j - проход по pattern
    # k - проход по string
    len_pattern = x = j = k = len(pattern)
    # число смещений
    counter = 0

    while x <= len(field) and j > 0:
        if pattern[j - 1] == field[k - 1]:
            j -= 1
            k -= 1
        else:
            x += d[ord(field[k - 1])]
            k = x
            j = len_pattern
            counter += 1

    if j <= 0:
        return True
    else:
        return False
