# TODO реализовать функцию count
def count(list, meaning):
    c = 0
    for item in list_items:
        if item == meaning:
            c += 1
    return c


list_items = [1, 2, "3", 1]
print(count(list_items, 1) == list_items.count(1))  # True
print(count(list_items, 3) == list_items.count(3))  # True
