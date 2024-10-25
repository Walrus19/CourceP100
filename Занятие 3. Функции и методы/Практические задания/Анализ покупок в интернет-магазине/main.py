# TODO Напишите функцию find_common_items
from socket import socket
from types import new_class


def find_common_items(last_week_purchases, current_week_purchases):
    intersection_set = set(last_week_purchases).intersection(current_week_purchases)
    rez = list(intersection_set)
    newList = rez
    newList.sort()
    return newList


last_week_items = ['книга', 'ноутбук', 'флешка', 'мышь']
current_week_items = ['ноутбук', 'флешка', 'наушники', 'монитор']


print(f"Общие товары: {find_common_items(last_week_items, current_week_items)}")  # TODO Распечатайте общие товары
