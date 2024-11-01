# TODO написать функцию index
def index(list_, value):
    list_index = [i for i, num in enumerate(list_) if num == value]
    if not list_index:
        raise ValueError("Значение не найдено")
    return list_index

if __name__ == '__main__':
    list_items = [1, 2, "3", 1]
    print(index(list_items, 1) == [0, 3])  # True
